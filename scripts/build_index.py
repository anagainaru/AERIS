#!/usr/bin/env python3
"""
Build wiki/index.md from all wiki pages.

Scans wiki/ directory for .md files, extracts metadata, and generates
a structured index showing all available knowledge.

Usage:
    python scripts/build_index.py

Output:
    wiki/index.md (overwrites existing)
"""

import os
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict

# Configuration
WIKI_DIR = Path("wiki")
INDEX_FILE = WIKI_DIR / "index.md"
EXCLUDE_FILES = {"index.md", "hot.md", "overview.md"}

def extract_title(content: str, filename: str) -> str:
    """Extract title from markdown file (first # heading or filename)."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return filename.replace('.md', '').replace('-', ' ').title()

def extract_description(content: str) -> str:
    """Extract first paragraph as description."""
    # Skip frontmatter if present
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    # Skip title
    content = re.sub(r'^#\s+.+\n+', '', content, flags=re.MULTILINE)
    # Get first non-empty line
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return lines[0] if lines else "No description"

def scan_wiki_pages() -> Dict[str, List[Dict]]:
    """Scan wiki directory and organize pages by section."""
    sections = {}

    if not WIKI_DIR.exists():
        return sections

    # Scan all subdirectories
    for section_dir in WIKI_DIR.iterdir():
        if not section_dir.is_dir():
            continue

        section_name = section_dir.name.replace('-', ' ').replace('_', ' ').title()
        pages = []

        for md_file in section_dir.glob("*.md"):
            if md_file.name in EXCLUDE_FILES:
                continue

            try:
                content = md_file.read_text(encoding='utf-8')
                pages.append({
                    'name': md_file.stem,
                    'title': extract_title(content, md_file.stem),
                    'description': extract_description(content),
                    'path': md_file.relative_to(WIKI_DIR)
                })
            except Exception as e:
                print(f"Warning: Could not read {md_file}: {e}")

        if pages:
            sections[section_name] = sorted(pages, key=lambda p: p['title'])

    # Also scan root level files
    root_pages = []
    for md_file in WIKI_DIR.glob("*.md"):
        if md_file.name in EXCLUDE_FILES or md_file.name == 'index.md':
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
            root_pages.append({
                'name': md_file.stem,
                'title': extract_title(content, md_file.stem),
                'description': extract_description(content),
                'path': md_file.relative_to(WIKI_DIR)
            })
        except Exception as e:
            print(f"Warning: Could not read {md_file}: {e}")

    if root_pages:
        sections['General'] = sorted(root_pages, key=lambda p: p['title'])

    return sections

def generate_index(sections: Dict[str, List[Dict]]) -> str:
    """Generate index.md content."""
    total_pages = sum(len(pages) for pages in sections.values())
    timestamp = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# Wiki Index",
        "",
        f"**Last updated:** {timestamp}",
        f"**Total pages:** {total_pages}",
        "",
        "> 📖 **READ THIS FIRST** every session to understand what knowledge is available.",
        "",
        "## Overview",
        "",
        "This wiki contains compiled domain knowledge organized by topic. The agent reads this catalog to locate relevant information before answering questions.",
        "",
        "---",
        "",
        "## Sections",
        ""
    ]

    # Add sections
    for section_name in sorted(sections.keys()):
        pages = sections[section_name]
        lines.append(f"### {section_name}")
        lines.append(f"*{len(pages)} pages*")
        lines.append("")

        for page in pages:
            # Truncate long descriptions
            desc = page['description']
            if len(desc) > 100:
                desc = desc[:97] + "..."
            lines.append(f"- [[{page['title']}]] — {desc}")

        lines.append("")

    # Add footer
    lines.extend([
        "---",
        "",
        "## Special Pages",
        "",
        "- [[hot]] — Recent context cache (~500 words, updated each session)",
        "- [[overview]] — Project structure and organization",
        "",
        "---",
        "",
        "## Usage Notes",
        "",
        "**For the agent:**",
        "1. Read this index.md FIRST every session",
        "2. Identify which pages are relevant to the user's query",
        "3. Read ALL relevant pages (not just one)",
        "4. Cite pages as [[Page Name]] in responses",
        "",
        "**For domain scientists:**",
        "- Run `python scripts/build_index.py` to regenerate this file",
        "- Add new pages to appropriate section directories",
        "- Keep page descriptions concise and searchable",
        ""
    ])

    return "\n".join(lines)

def main():
    """Main entry point."""
    print("Building wiki index...")

    # Scan pages
    sections = scan_wiki_pages()

    if not sections:
        print("Warning: No wiki pages found")
        print("Create some pages in wiki/ subdirectories first")
        return

    # Generate index
    content = generate_index(sections)

    # Write atomically (write to temp, then rename)
    temp_file = INDEX_FILE.with_suffix('.tmp')
    temp_file.write_text(content, encoding='utf-8')
    temp_file.replace(INDEX_FILE)

    total_pages = sum(len(pages) for pages in sections.values())
    print(f"✓ Index built: {total_pages} pages across {len(sections)} sections")
    print(f"  Output: {INDEX_FILE}")

if __name__ == "__main__":
    main()
