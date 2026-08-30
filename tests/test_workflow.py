from __future__ import annotations

import importlib.util
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "skills/python-uv-gh-workflow/scripts/workflow.py"
SPEC = importlib.util.spec_from_file_location("workflow", MODULE_PATH)
workflow = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(workflow)


class WorkflowTests(unittest.TestCase):
    def test_materialize_issue_body_injects_traceability(self) -> None:
        body = "#{{ISSUE_NUMBER}} {{PYTEST_MARKER}} {{FOCUSED_TEST_COMMAND}}"
        rendered = workflow.materialize_issue_body(body, 42)
        self.assertEqual(rendered, "#42 issue_42 uv run pytest -m issue_42 -v")

    def test_ensure_marker_adds_pytest_section(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pyproject.toml"
            path.write_text('[project]\nname = "example"\nversion = "0.1.0"\n')
            self.assertTrue(workflow.ensure_marker(path, 7))
            self.assertIn("issue_7: tests providing traceability", path.read_text())
            self.assertFalse(workflow.ensure_marker(path, 7))

    def test_ensure_marker_appends_to_existing_multiline_markers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pyproject.toml"
            path.write_text(
                '[tool.pytest.ini_options]\nmarkers = [\n    "slow: slow tests",\n]\n'
            )
            workflow.ensure_marker(path, 19)
            text = path.read_text()
            self.assertIn('"slow: slow tests"', text)
            self.assertIn("issue_19: tests providing traceability", text)

    def test_ensure_marker_appends_to_existing_inline_markers(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pyproject.toml"
            path.write_text('[tool.pytest.ini_options]\nmarkers = ["slow: slow tests"]\n')
            workflow.ensure_marker(path, 20)
            text = path.read_text()
            self.assertIn('"slow: slow tests",', text)
            self.assertIn("issue_20: tests providing traceability", text)
            tomllib.loads(text)

    def test_ensure_marker_detects_existing_inline_registration(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pyproject.toml"
            path.write_text(
                '[tool.pytest.ini_options]\nmarkers = ["issue_20: existing trace"]\n'
            )
            self.assertFalse(workflow.ensure_marker(path, 20))

    def test_checkpoint_preserves_unmanaged_claude_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "CLAUDE.md"
            path.write_text("# Project rules\n\nNever remove this.\n")
            fields = {"Active issue": "#3 — Example", "Phase": "RED"}
            workflow.write_checkpoint(path, fields)
            workflow.write_checkpoint(path, {**fields, "Phase": "GREEN"})
            text = path.read_text()
            self.assertIn("Never remove this.", text)
            self.assertEqual(text.count(workflow.CHECKPOINT_START), 1)
            self.assertIn("**Phase:** GREEN", text)
            self.assertTrue(workflow.clear_checkpoint(path))
            self.assertIn("Never remove this.", path.read_text())
            self.assertNotIn(workflow.CHECKPOINT_START, path.read_text())


if __name__ == "__main__":
    unittest.main()
