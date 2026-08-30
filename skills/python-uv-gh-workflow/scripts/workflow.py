#!/usr/bin/env python3
"""Deterministic helpers for the Python/uv GitHub issue workflow."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path


CHECKPOINT_START = "<!-- python-uv-gh-workflow:start -->"
CHECKPOINT_END = "<!-- python-uv-gh-workflow:end -->"
ISSUE_URL_RE = re.compile(r"/issues/(\d+)(?:$|[/?#])")


class WorkflowError(RuntimeError):
    pass


def run(command: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise WorkflowError(f"command failed ({' '.join(command)}): {detail}")
    return result.stdout.strip()


def gh(args: list[str], repo: str | None = None) -> str:
    command = ["gh", *args]
    if repo:
        command.extend(["--repo", repo])
    return run(command)


def issue_marker(number: int) -> str:
    if number < 1:
        raise WorkflowError("issue number must be positive")
    return f"issue_{number}"


def materialize_issue_body(body: str, number: int) -> str:
    marker = issue_marker(number)
    return (
        body.replace("{{ISSUE_NUMBER}}", str(number))
        .replace("{{PYTEST_MARKER}}", marker)
        .replace("{{FOCUSED_TEST_COMMAND}}", f"uv run pytest -m {marker} -v")
    )


def create_issue(title: str, body_file: Path, repo: str | None) -> dict[str, object]:
    if not body_file.is_file():
        raise WorkflowError(f"body file not found: {body_file}")
    original = body_file.read_text()
    url = gh(["issue", "create", "--title", title, "--body-file", str(body_file)], repo)
    match = ISSUE_URL_RE.search(url)
    if not match:
        raise WorkflowError(f"could not determine issue number from gh output: {url}")
    number = int(match.group(1))
    rendered = materialize_issue_body(original, number)
    if rendered != original:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as temporary:
            temporary.write(rendered)
            rendered_path = Path(temporary.name)
        try:
            gh(["issue", "edit", str(number), "--body-file", str(rendered_path)], repo)
        finally:
            rendered_path.unlink(missing_ok=True)
    marker = issue_marker(number)
    return {
        "number": number,
        "url": url,
        "marker": marker,
        "focused_command": f"uv run pytest -m {marker} -v",
    }


def view_issue(number: int, repo: str | None) -> dict[str, object]:
    raw = gh(
        [
            "issue",
            "view",
            str(number),
            "--json",
            "number,title,body,state,url,labels,milestone,assignees",
        ],
        repo,
    )
    return json.loads(raw)


def list_issues(state: str, repo: str | None) -> list[dict[str, object]]:
    raw = gh(
        [
            "issue",
            "list",
            "--state",
            state,
            "--limit",
            "100",
            "--json",
            "number,title,state,url,labels",
        ],
        repo,
    )
    return json.loads(raw)


def ensure_marker(pyproject: Path, number: int) -> bool:
    if not pyproject.is_file():
        raise WorkflowError(f"pyproject.toml not found: {pyproject}")
    marker = issue_marker(number)
    description = f"{marker}: tests providing traceability for GitHub issue #{number}"
    text = pyproject.read_text()
    if re.search(rf"[\"']{re.escape(marker)}\s*:", text):
        return False

    section_match = re.search(r"(?m)^\[tool\.pytest\.ini_options\]\s*$", text)
    entry = f'    "{description}",\n'
    if not section_match:
        suffix = "" if text.endswith("\n") else "\n"
        text += suffix + f'\n[tool.pytest.ini_options]\nmarkers = [\n{entry}]\n'
        pyproject.write_text(text)
        return True

    section_start = section_match.end()
    next_section = re.search(r"(?m)^\[[^\n]+\]\s*$", text[section_start:])
    section_end = section_start + next_section.start() if next_section else len(text)
    section = text[section_start:section_end]
    markers_match = re.search(r"(?ms)^markers\s*=\s*\[(.*?)\]", section)
    if markers_match:
        insertion = section_start + markers_match.end(1)
        content = markers_match.group(1)
        prefix = ""
        if content.strip() and not content.rstrip().endswith(","):
            prefix += ","
        if content and not content.endswith("\n"):
            prefix += "\n"
        text = text[:insertion] + prefix + entry + text[insertion:]
    else:
        text = text[:section_start] + f'\nmarkers = [\n{entry}]' + text[section_start:]
    pyproject.write_text(text)
    return True


def render_checkpoint(fields: dict[str, str]) -> str:
    ordered = (
        "Active issue",
        "Issue URL",
        "Branch",
        "Pytest marker",
        "Phase",
        "Current version",
        "Target version",
        "Last verified command",
        "Last result",
        "Next action",
    )
    lines = [CHECKPOINT_START, "## Active Python issue workflow", ""]
    lines.extend(f"- **{name}:** {fields.get(name, '—')}" for name in ordered)
    lines.extend(["", CHECKPOINT_END])
    return "\n".join(lines)


def write_checkpoint(path: Path, fields: dict[str, str]) -> None:
    current = path.read_text() if path.exists() else ""
    block = render_checkpoint(fields)
    pattern = re.compile(
        rf"{re.escape(CHECKPOINT_START)}.*?{re.escape(CHECKPOINT_END)}", re.DOTALL
    )
    if pattern.search(current):
        updated = pattern.sub(block, current)
    else:
        separator = "\n\n" if current.strip() else ""
        updated = current.rstrip() + separator + block + "\n"
    path.write_text(updated)


def clear_checkpoint(path: Path) -> bool:
    if not path.exists():
        return False
    current = path.read_text()
    pattern = re.compile(
        rf"\n*{re.escape(CHECKPOINT_START)}.*?{re.escape(CHECKPOINT_END)}\n?", re.DOTALL
    )
    updated, count = pattern.subn("\n", current)
    if count:
        path.write_text(updated.rstrip() + ("\n" if updated.strip() else ""))
    return bool(count)


def bump_version(part: str, project: Path) -> str:
    return run(["uv", "version", "--bump", part, "--short"], cwd=project)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="area", required=True)

    issue = sub.add_parser("issue")
    issue_sub = issue.add_subparsers(dest="action", required=True)
    create = issue_sub.add_parser("create")
    create.add_argument("--title", required=True)
    create.add_argument("--body-file", required=True, type=Path)
    create.add_argument("--repo")
    view = issue_sub.add_parser("view")
    view.add_argument("number", type=int)
    view.add_argument("--repo")
    listing = issue_sub.add_parser("list")
    listing.add_argument("--state", choices=("open", "closed", "all"), default="open")
    listing.add_argument("--repo")

    marker = sub.add_parser("marker")
    marker_sub = marker.add_subparsers(dest="action", required=True)
    ensure = marker_sub.add_parser("ensure")
    ensure.add_argument("number", type=int)
    ensure.add_argument("--pyproject", type=Path, default=Path("pyproject.toml"))

    checkpoint = sub.add_parser("checkpoint")
    checkpoint_sub = checkpoint.add_subparsers(dest="action", required=True)
    set_cp = checkpoint_sub.add_parser("set")
    set_cp.add_argument("number", type=int)
    set_cp.add_argument("--title", required=True)
    set_cp.add_argument("--url", default="—")
    set_cp.add_argument("--branch", required=True)
    set_cp.add_argument("--phase", choices=("RED", "GREEN", "REFACTOR", "VERIFY"), required=True)
    set_cp.add_argument("--current-version", default="—")
    set_cp.add_argument("--target-version", default="—")
    set_cp.add_argument("--last-command", default="—")
    set_cp.add_argument("--last-result", default="—")
    set_cp.add_argument("--next-action", required=True)
    set_cp.add_argument("--file", type=Path, default=Path("CLAUDE.md"))
    clear_cp = checkpoint_sub.add_parser("clear")
    clear_cp.add_argument("--file", type=Path, default=Path("CLAUDE.md"))

    version = sub.add_parser("version")
    version_sub = version.add_subparsers(dest="action", required=True)
    bump = version_sub.add_parser("bump")
    bump.add_argument("part", choices=("patch", "minor", "major"))
    bump.add_argument("--project", type=Path, default=Path.cwd())
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.area == "issue" and args.action == "create":
        print(json.dumps(create_issue(args.title, args.body_file, args.repo), indent=2))
    elif args.area == "issue" and args.action == "view":
        print(json.dumps(view_issue(args.number, args.repo), indent=2))
    elif args.area == "issue" and args.action == "list":
        print(json.dumps(list_issues(args.state, args.repo), indent=2))
    elif args.area == "marker" and args.action == "ensure":
        changed = ensure_marker(args.pyproject, args.number)
        print(json.dumps({"marker": issue_marker(args.number), "registered": changed}))
    elif args.area == "checkpoint" and args.action == "set":
        write_checkpoint(
            args.file,
            {
                "Active issue": f"#{args.number} — {args.title}",
                "Issue URL": args.url,
                "Branch": args.branch,
                "Pytest marker": issue_marker(args.number),
                "Phase": args.phase,
                "Current version": args.current_version,
                "Target version": args.target_version,
                "Last verified command": args.last_command,
                "Last result": args.last_result,
                "Next action": args.next_action,
            },
        )
        print(args.file)
    elif args.area == "checkpoint" and args.action == "clear":
        print(json.dumps({"cleared": clear_checkpoint(args.file)}))
    elif args.area == "version" and args.action == "bump":
        print(bump_version(args.part, args.project.resolve()))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except WorkflowError as error:
        raise SystemExit(str(error)) from error
