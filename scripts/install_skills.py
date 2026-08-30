#!/usr/bin/env python3
"""Install the canonical skills for Claude Code, Codex, or both."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


AGENT_DIRS = {
    "claude": Path(".claude/skills"),
    "codex": Path(".codex/skills"),
}


def install(source_root: Path, target: Path, agent: str, force: bool) -> list[Path]:
    agents = tuple(AGENT_DIRS) if agent == "both" else (agent,)
    installed: list[Path] = []
    for agent_name in agents:
        destination_root = target / AGENT_DIRS[agent_name]
        destination_root.mkdir(parents=True, exist_ok=True)
        for skill in sorted(path for path in source_root.iterdir() if path.is_dir()):
            destination = destination_root / skill.name
            if destination.exists():
                if not force:
                    raise FileExistsError(
                        f"{destination} already exists; rerun with --force to replace it"
                    )
                shutil.rmtree(destination)
            shutil.copytree(skill, destination)
            installed.append(destination)
    return installed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=("claude", "codex", "both"), default="both")
    parser.add_argument("--target", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    repository = Path(__file__).resolve().parents[1]
    for path in install(repository / "skills", args.target.resolve(), args.agent, args.force):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
