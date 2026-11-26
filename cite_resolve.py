#!/usr/bin/env python3
"""
Citation verification script.

Validates that all citations in wiki pages resolve to actual sources.
Checks both [n] numeric citations and [[wiki-page]] links.

Usage:
    python scripts/cite_resolve.py wiki/section/page.md
    python scripts/cite_resolve.py wiki/  # Check all pages

Exit codes:
    0 - All citations resolve
    1 - Broken citations found
"""

import sys
import re
import csv
from pathlib import Path
from typing import List, Dict, Set, Tuple

# Configuration
CORPUS_META = Path("papers/corpus-meta.csv")
CITEMAPS_DIR = Path("papers/citemaps")
WIKI_DIR = Path("wiki")

def load_corpus_meta() -> Dict[str, Dict]:
    """Load citation registry."""
    if not CORPUS_META.exists():
        return {}

    sources = {}
    with open(CORPUS_META, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sources[row['citekey']] = row
    return sources

def load_citemap(citekey: str) -> Set[int]:
    """Load citation numbers for a source."""
    citemap_file = CITEMAPS_DIR / f"{citekey}.tsv"
    if not citemap_file.exists():
        return set()

    citations = set()
    with open(citemap_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            try:
                citations.add(int(row['cite_num']))
            except (ValueError, KeyError):
                continue
    return citations

def extract_numeric_citations(content: str) -> List[int]:
    """Extract [n] style citations from markdown."""
    # Match [1], [2], etc. but not [[wiki-links]]
    pattern = r'(?<!\[)\[(\d+)\](?!\])'
    matches = re.findall(pattern, content)
    return [int(m) for m in matches]

def extract_wiki_citations(content: str) -> List[str]:
    """Extract [[wiki-page]] style citations from markdown."""
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    return matches

def check_numeric_citations(citations: List[int], sources: Dict[str, Dict]) -> List[str]:
    """Check if numeric citations resolve."""
    errors = []

    if not citations:
        return errors

    # Build complete set of valid citation numbers across all sources
    all_valid_cites = set()
    for citekey in sources.keys():
        all_valid_cites.update(load_citemap(citekey))

    # Check each citation
    for cite_num in set(citations):
        if cite_num not in all_valid_cites:
            errors.append(f"[{cite_num}] not found in any citemap")

    return errors

def check_wiki_citations(citations: List[str]) -> List[str]:
    """Check if wiki page citations resolve."""
    errors = []

    if not citations:
        return errors

    for wiki_cite in set(citations):
        # Check if page exists
        # Try multiple locations since we don't know the section
        found = False

        # Check root level
        if (WIKI_DIR / f"{wiki_cite}.md").exists():
            found = True

        # Check all subdirectories
        for section_dir in WIKI_DIR.iterdir():
            if section_dir.is_dir():
                if (section_dir / f"{wiki_cite}.md").exists():
                    found = True
                    break

        if not found:
            errors.append(f"[[{wiki_cite}]] - page not found in wiki/")

    return errors

def check_file(file_path: Path, sources: Dict[str, Dict]) -> Tuple[int, List[str]]:
    """Check citations in a single file."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return 0, [f"Could not read file: {e}"]

    # Extract citations
    numeric_cites = extract_numeric_citations(content)
    wiki_cites = extract_wiki_citations(content)

    total_cites = len(set(numeric_cites)) + len(set(wiki_cites))

    # Check both types
    errors = []
    errors.extend(check_numeric_citations(numeric_cites, sources))
    errors.extend(check_wiki_citations(wiki_cites))

    return total_cites, errors

def check_directory(dir_path: Path, sources: Dict[str, Dict]) -> Tuple[int, int, List[Tuple[Path, List[str]]]]:
    """Recursively check all markdown files in directory."""
    total_files = 0
    total_cites = 0
    all_errors = []

    for md_file in dir_path.rglob("*.md"):
        # Skip index and special pages
        if md_file.name in {"index.md", "hot.md", "overview.md", "README.md"}:
            continue

        total_files += 1
        cites, errors = check_file(md_file, sources)
        total_cites += cites

        if errors:
            all_errors.append((md_file, errors))

    return total_files, total_cites, all_errors

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/cite_resolve.py <file_or_directory>")
        print()
        print("Examples:")
        print("  python scripts/cite_resolve.py wiki/concepts/MyPage.md")
        print("  python scripts/cite_resolve.py wiki/")
        sys.exit(1)

    target = Path(sys.argv[1])

    if not target.exists():
        print(f"Error: {target} not found")
        sys.exit(1)

    # Load sources
    print("Loading citation registry...")
    sources = load_corpus_meta()

    if not sources:
        print("⚠️  No corpus-meta.csv found. Cannot verify numeric citations.")
        print("   Create papers/corpus-meta.csv to enable full verification.")
        print()

    # Check target
    if target.is_file():
        print(f"Checking: {target}")
        print()
        cites, errors = check_file(target, sources)

        if errors:
            print("❌ BROKEN CITATIONS FOUND")
            print()
            for error in errors:
                print(f"  • {error}")
            print()
            sys.exit(1)
        else:
            print(f"✓ All citations resolve ({cites} unique citations)")
            sys.exit(0)

    elif target.is_dir():
        print(f"Checking directory: {target}")
        print()
        total_files, total_cites, all_errors = check_directory(target, sources)

        print(f"Checked {total_files} files with {total_cites} unique citations")
        print()

        if all_errors:
            print("❌ BROKEN CITATIONS FOUND")
            print()
            for file_path, errors in all_errors:
                print(f"  {file_path}:")
                for error in errors:
                    print(f"    • {error}")
                print()
            print(f"Total: {len(all_errors)} files with errors")
            sys.exit(1)
        else:
            print("✓ All citations resolve")
            sys.exit(0)

    else:
        print(f"Error: {target} is neither a file nor directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
