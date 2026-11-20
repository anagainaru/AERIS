#!/usr/bin/env python3
"""
Validate agent directory structure.

Checks that all required files and directories exist for proper agent operation.
Reports missing items and provides guidance on fixing them.

Usage:
    python scripts/validate_structure.py

Exit codes:
    0 - All required items present
    1 - Missing required items
"""

import sys
from pathlib import Path
from typing import List, Tuple

# Required files (path, description)
REQUIRED_FILES = [
    ("CLAUDE.md", "Main agent instructions"),
    ("README.md", "Project documentation"),
    (".gitignore", "Git ignore patterns"),
    ("wiki/index.md", "Wiki catalog"),
    ("wiki/hot.md", "Recent context cache"),
    ("wiki/overview.md", "Project structure overview"),
    (".claude/settings.json", "Agent configuration"),
    (".claude/memory/handoff.md", "Work state tracking"),
]

# Required directories (path, description)
REQUIRED_DIRS = [
    ("wiki", "Knowledge base"),
    ("data", "Input datasets"),
    ("reports", "Generated outputs"),
    ("scripts", "Automation utilities"),
    (".claude", "Claude configuration"),
    (".claude/skills", "Custom capabilities"),
    (".claude/hooks", "Event-driven automation"),
    (".claude/memory", "Persistent context"),
]

# Optional but recommended files
OPTIONAL_FILES = [
    (".mcp.json", "MCP tool integrations"),
    ("AGENTS.md", "Agent registry"),
    (".claude/skills/README.md", "Skills documentation"),
]

def check_required_files() -> Tuple[List[str], List[str]]:
    """Check required files exist."""
    missing = []
    present = []

    for file_path, description in REQUIRED_FILES:
        path = Path(file_path)
        if path.exists():
            present.append(f"✓ {file_path} ({description})")
        else:
            missing.append(f"✗ {file_path} - {description}")

    return present, missing

def check_required_dirs() -> Tuple[List[str], List[str]]:
    """Check required directories exist."""
    missing = []
    present = []

    for dir_path, description in REQUIRED_DIRS:
        path = Path(dir_path)
        if path.is_dir():
            present.append(f"✓ {dir_path}/ ({description})")
        else:
            missing.append(f"✗ {dir_path}/ - {description}")

    return present, missing

def check_optional_files() -> List[str]:
    """Check which optional files are present."""
    present = []

    for file_path, description in OPTIONAL_FILES:
        path = Path(file_path)
        if path.exists():
            present.append(f"  {file_path} ({description})")

    return present

def check_hooks() -> Tuple[int, List[str]]:
    """Check hooks configuration."""
    hooks_dir = Path(".claude/hooks")
    issues = []

    if not hooks_dir.exists():
        return 0, ["No hooks directory"]

    hook_files = list(hooks_dir.glob("*.sh"))
    for hook in hook_files:
        if not hook.stat().st_mode & 0o111:
            issues.append(f"  ⚠️  {hook.name} is not executable (run: chmod +x {hook})")

    return len(hook_files), issues

def check_skills() -> Tuple[int, List[str]]:
    """Check skills configuration."""
    skills_dir = Path(".claude/skills")
    issues = []

    if not skills_dir.exists():
        return 0, ["No skills directory"]

    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]

    for skill in skill_dirs:
        if not (skill / "skill.md").exists():
            issues.append(f"  ⚠️  {skill.name} missing skill.md")
        if not (skill / "instructions.md").exists():
            issues.append(f"  ⚠️  {skill.name} missing instructions.md")

    return len(skill_dirs), issues

def main():
    """Main validation."""
    print("=" * 60)
    print("Agent Structure Validation")
    print("=" * 60)
    print()

    # Check required items
    print("Required Files:")
    present_files, missing_files = check_required_files()
    for item in present_files:
        print(f"  {item}")
    print()

    print("Required Directories:")
    present_dirs, missing_dirs = check_required_dirs()
    for item in present_dirs:
        print(f"  {item}")
    print()

    # Check optional items
    optional = check_optional_files()
    if optional:
        print("Optional Files Present:")
        for item in optional:
            print(f"  {item}")
        print()

    # Check hooks
    num_hooks, hook_issues = check_hooks()
    print(f"Hooks: {num_hooks} found")
    if hook_issues:
        for issue in hook_issues:
            print(issue)
    print()

    # Check skills
    num_skills, skill_issues = check_skills()
    print(f"Skills: {num_skills} found")
    if skill_issues:
        for issue in skill_issues:
            print(issue)
    print()

    # Report missing required items
    all_missing = missing_files + missing_dirs

    if all_missing:
        print("=" * 60)
        print("MISSING REQUIRED ITEMS")
        print("=" * 60)
        print()
        for item in all_missing:
            print(f"  {item}")
        print()
        print("Run the following to create missing items:")
        print()

        for file_path, _ in REQUIRED_FILES:
            if any(file_path in m for m in missing_files):
                print(f"  touch {file_path}")

        for dir_path, _ in REQUIRED_DIRS:
            if any(dir_path in m for m in missing_dirs):
                print(f"  mkdir -p {dir_path}")

        print()
        print("Then fill in content according to TEMPLATE_GUIDE.md")
        print()
        sys.exit(1)

    else:
        print("=" * 60)
        print("✓ ALL REQUIRED ITEMS PRESENT")
        print("=" * 60)
        print()
        print("Agent structure is valid!")

        if hook_issues or skill_issues:
            print()
            print("Note: Some warnings were found above. Review and fix if needed.")
            sys.exit(0)

        sys.exit(0)

if __name__ == "__main__":
    main()
