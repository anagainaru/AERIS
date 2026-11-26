#!/usr/bin/env python3
"""
Citation Presence Guard Hook (PostToolUse)

Warns when wiki pages are written without proper citations.
Non-blocking - the edit stands, but you get a warning on stderr.

Checks for:
- [n] numeric citations
- [[wiki-page]] secondary citations
- Proper citation format

Customize PAGE_TYPES_REQUIRING_CITATIONS to match your wiki structure.
"""

import sys
import json
import re
from pathlib import Path

# Configuration: Which page types require citations
# Customize these patterns based on your wiki structure
PAGE_TYPES_REQUIRING_CITATIONS = [
    "wiki/concepts/",      # Concept pages
    "wiki/entities/",      # Entity pages
    "wiki/sources/",       # Source pages
    "wiki/[SECTION_1]/",   # Your domain sections
    "wiki/[SECTION_2]/",
    "wiki/[SECTION_3]/",
]

# Pages that are exempt from citation requirements
EXEMPT_PAGES = {
    "index.md",
    "hot.md",
    "overview.md",
    "glossary.md",
    "README.md",
}

def file_requires_citations(file_path: str) -> bool:
    """Check if this file type requires citations."""
    path = Path(file_path)

    # Exempt pages
    if path.name in EXEMPT_PAGES:
        return False

    # Check if file matches any citation-required pattern
    file_str = str(path)
    for pattern in PAGE_TYPES_REQUIRING_CITATIONS:
        if pattern in file_str:
            return True

    return False

def check_citations(content: str) -> dict:
    """Check if content has proper citations."""
    # Look for [n] numeric citations
    numeric_pattern = r'(?<!\[)\[(\d+)\](?!\])'
    numeric_cites = re.findall(numeric_pattern, content)

    # Look for [[wiki-page]] citations
    wiki_pattern = r'\[\[([^\]]+)\]\]'
    wiki_cites = re.findall(wiki_pattern, content)

    # Check for citation section at end
    has_references = bool(re.search(r'^##?\s+References?\s*$', content, re.MULTILINE | re.IGNORECASE))

    return {
        "has_numeric": len(numeric_cites) > 0,
        "has_wiki": len(wiki_cites) > 0,
        "has_references_section": has_references,
        "numeric_count": len(numeric_cites),
        "wiki_count": len(wiki_cites),
    }

def main():
    """Main hook entry point."""
    # Read tool use from stdin (Claude hook protocol)
    try:
        tool_use = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        # Not valid JSON, exit quietly
        sys.exit(0)

    tool_name = tool_use.get("tool_name", "")

    # Only check Write and Edit operations
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    # Get file path
    params = tool_use.get("params", {})
    file_path = params.get("file_path", "")

    if not file_path:
        sys.exit(0)

    # Check if this file requires citations
    if not file_requires_citations(file_path):
        sys.exit(0)

    # Get content
    content = ""
    if tool_name == "Write":
        content = params.get("content", "")
    elif tool_name == "Edit":
        content = params.get("new_string", "")

    if not content:
        sys.exit(0)

    # Check for citations
    results = check_citations(content)

    # Warn if no citations found
    if not results["has_numeric"] and not results["has_wiki"]:
        print("⚠️  CITATION WARNING", file=sys.stderr)
        print("", file=sys.stderr)
        print(f"File: {file_path}", file=sys.stderr)
        print("", file=sys.stderr)
        print("This wiki page was saved without citations.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Expected format:", file=sys.stderr)
        print("  • Numeric citations: [1], [2], [3]", file=sys.stderr)
        print("  • Wiki citations: ([[Page-Name]])", file=sys.stderr)
        print("  • Dual format: [1] ([[Page-Name]])", file=sys.stderr)
        print("", file=sys.stderr)
        print("Consider adding:", file=sys.stderr)
        print("  1. Citations for claims: 'Value is X [1] ([[Source-Page]])'", file=sys.stderr)
        print("  2. References section at bottom", file=sys.stderr)
        print("", file=sys.stderr)
        print("The edit was saved (non-blocking warning).", file=sys.stderr)
        print("", file=sys.stderr)
        # Exit 0 - warning only, don't block
        sys.exit(0)

    # Citation found, exit quietly
    sys.exit(0)

if __name__ == "__main__":
    main()
