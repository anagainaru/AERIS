#!/usr/bin/env bash
# Wiki Change Detector (Stop Hook)
# Detects if wiki/ was modified and reminds to update hot.md

set -euo pipefail

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    # Not a git repo, skip check
    exit 0
fi

# Check if wiki/ has uncommitted changes
if git diff --quiet wiki/ && git diff --cached --quiet wiki/; then
    # No changes, exit quietly
    exit 0
fi

# Wiki was modified
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >&2
echo "📝 WIKI CHANGES DETECTED" >&2
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >&2
echo "" >&2
echo "The wiki/ directory was modified this session." >&2
echo "" >&2

# Show what changed
echo "Changes:" >&2
git status --short wiki/ >&2
echo "" >&2

# Remind to update hot.md
echo "📌 REMEMBER TO UPDATE:" >&2
echo "   • wiki/hot.md - Add recent changes" >&2
echo "   • wiki/index.md - Run build_index.py if structure changed" >&2
echo "" >&2
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >&2

# Exit 0 - warning only, don't block
exit 0
