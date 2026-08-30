# Python uv BDD workflows

Portable skills for turning requirements into traceable GitHub issues and delivering them with
Python, `uv`, pytest, BDD acceptance criteria, TDD, explicit safety evidence, and per-issue version
increments.

The repository is agent-agnostic. The canonical skills live in `skills/` and can be installed for
Claude Code, Codex, or both:

```bash
uv run python scripts/install_skills.py --agent both --target /path/to/project
```

This installs the same skill definitions into `.claude/skills/` and `.codex/skills/`; there are no
separate implementations to drift apart.

## Skills

- `python-uv-gh-workflow`: create, start, test, implement, verify, version and finish GitHub issues.
- `suggest-architecture-diagram`: turn a specification or issue set into a concise Mermaid diagram
  and a short list of design questions.

GitHub Issues are the requirements source of truth. A managed block in `CLAUDE.md` records only the
active issue, current TDD phase, last verification result and next action.

## Requirements

- `uv`
- `git`
- authenticated GitHub CLI (`gh auth status`)
- a Python project with `pyproject.toml`

## Validation

```bash
uv run python -m unittest discover -s tests -v
```

Tests and coverage provide evidence, not a guarantee of clinical safety. Intended-use validation,
risk management, human review and applicable regulatory controls remain separate responsibilities.

