#!/usr/bin/env python3
"""
Numeric Value Provenance Verifier

Scans wiki pages for numeric values and verifies they have:
1. Explicit units
2. Citation to source [n]
3. Proper formatting

CUSTOMIZE the patterns and rules for your domain.

Usage:
    python scripts/verify_numbers.py [directory]

Exit codes:
    0 - All numeric values properly cited
    1 - Issues found (warnings, not errors)
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

# Configuration - CUSTOMIZE THESE
WIKI_DIRS_TO_CHECK = [
    "wiki/sources",
    "wiki/entities",
    "wiki/[SECTION_WITH_DATA]",  # Replace with your sections
]

# Files to skip
SKIP_FILES = {"index.md", "hot.md", "overview.md", "README.md", "glossary.md"}

# Numeric patterns to detect
# Add domain-specific patterns
NUMERIC_PATTERNS = [
    # Basic number with optional units: "10.5 g/cm³", "1200 °C"
    r'\b(\d+\.?\d*)\s*([a-zA-Z°µ/³²]+)',
    # Range: "10-20 GPa"
    r'\b(\d+)-(\d+)\s*([a-zA-Z°µ/³²]+)',
    # Scientific notation: "1.5e-3 kg"
    r'\b(\d+\.?\d*[eE][+-]?\d+)\s*([a-zA-Z°µ/³²]+)',
]

def should_check_file(file_path: Path) -> bool:
    """Determine if file should be checked."""
    if file_path.name in SKIP_FILES:
        return False

    file_str = str(file_path)
    for check_dir in WIKI_DIRS_TO_CHECK:
        if check_dir in file_str:
            return True

    return False

def extract_numeric_values(content: str, file_path: Path) -> List[Tuple[int, str]]:
    """Extract lines with numeric values."""
    matches = []

    for line_num, line in enumerate(content.split('\n'), 1):
        # Skip markdown headers, code blocks, citations themselves
        if line.strip().startswith('#'):
            continue
        if line.strip().startswith('```'):
            continue
        if line.strip().startswith('[') and line.strip().endswith(']'):
            continue

        # Check if line contains numeric value
        has_number = False
        for pattern in NUMERIC_PATTERNS:
            if re.search(pattern, line):
                has_number = True
                break

        if has_number:
            matches.append((line_num, line.strip()))

    return matches

def check_line_has_citation(line: str) -> dict:
    """Check if line has proper citation."""
    # Check for [n] numeric citation
    has_numeric_cite = bool(re.search(r'(?<!\[)\[(\d+)\](?!\])', line))

    # Check for [[wiki-page]] citation
    has_wiki_cite = bool(re.search(r'\[\[([^\]]+)\]\]', line))

    # Check for explicit source mention (fallback)
    has_source_mention = bool(re.search(r'(according to|from|source:|ref:)', line, re.IGNORECASE))

    return {
        "has_numeric_cite": has_numeric_cite,
        "has_wiki_cite": has_wiki_cite,
        "has_source_mention": has_source_mention,
        "has_any_citation": has_numeric_cite or has_wiki_cite or has_source_mention,
    }

def check_file(file_path: Path) -> List[dict]:
    """Check a file for numeric values without proper citations."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [{"type": "error", "message": f"Could not read file: {e}"}]

    issues = []

    # Extract lines with numeric values
    numeric_lines = extract_numeric_values(content, file_path)

    if not numeric_lines:
        # No numeric values, nothing to check
        return []

    # Check each line
    for line_num, line in numeric_lines:
        citation_status = check_line_has_citation(line)

        if not citation_status["has_any_citation"]:
            issues.append({
                "type": "missing_citation",
                "file": str(file_path),
                "line": line_num,
                "content": line[:100],  # Truncate long lines
                "severity": "warning",
            })

    return issues

def check_directory(dir_path: Path) -> Tuple[int, List[dict]]:
    """Check all markdown files in directory."""
    total_files = 0
    all_issues = []

    if not dir_path.exists():
        return 0, []

    for md_file in dir_path.rglob("*.md"):
        if not should_check_file(md_file):
            continue

        total_files += 1
        issues = check_file(md_file)
        all_issues.extend(issues)

    return total_files, all_issues

def main():
    """Main entry point."""
    # Determine what to check
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        if not target.exists():
            print(f"Error: {target} not found")
            sys.exit(1)
        check_paths = [target]
    else:
        check_paths = [Path(d) for d in WIKI_DIRS_TO_CHECK if Path(d).exists()]

    if not check_paths:
        print("No directories to check")
        sys.exit(0)

    # Check all paths
    total_files = 0
    all_issues = []

    for path in check_paths:
        if path.is_file():
            if should_check_file(path):
                total_files += 1
                all_issues.extend(check_file(path))
        elif path.is_dir():
            files, issues = check_directory(path)
            total_files += files
            all_issues.extend(issues)

    # Report results
    print(f"Checked {total_files} files")
    print()

    if not all_issues:
        print("✓ All numeric values have proper provenance")
        sys.exit(0)

    # Group issues by type
    missing_citations = [i for i in all_issues if i["type"] == "missing_citation"]

    if missing_citations:
        print(f"⚠️  {len(missing_citations)} numeric values without citations:")
        print()

        for issue in missing_citations[:10]:  # Show first 10
            print(f"  {issue['file']}:{issue['line']}")
            print(f"    {issue['content']}")
            print()

        if len(missing_citations) > 10:
            print(f"  ... and {len(missing_citations) - 10} more")
            print()

    print("Recommendation:")
    print("  Add citations to numeric values: [VALUE] [UNIT] [n] ([[Source-Page]])")
    print()

    # Exit 1 to indicate issues found (but not a hard error)
    sys.exit(1)

if __name__ == "__main__":
    main()
