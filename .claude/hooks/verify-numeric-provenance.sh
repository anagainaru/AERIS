#!/usr/bin/env bash
# Numeric Provenance Verifier (Stop Hook)
# Runs verification when wiki/sources/ changes
# Checks that numeric values have citations and source locations

set -euo pipefail

# Configuration: Which directories to check for numeric values
# Customize these paths based on your wiki structure
CHECK_DIRS=("wiki/sources" "wiki/entities" "wiki/[SECTION_WITH_DATA]")

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    # Not a git repo, skip check
    exit 0
fi

# Check if any monitored directories changed
changed=false
for dir in "${CHECK_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        if ! git diff --quiet "$dir/" 2>/dev/null || ! git diff --cached --quiet "$dir/" 2>/dev/null; then
            changed=true
            break
        fi
    fi
done

if [ "$changed" = false ]; then
    # No changes to monitored dirs
    exit 0
fi

# Check if verification script exists
if [ ! -f "scripts/verify_numbers.py" ]; then
    echo "⚠️  wiki/sources/ changed but scripts/verify_numbers.py not found" >&2
    echo "   Skipping numeric provenance check" >&2
    exit 0
fi

echo "🔍 Running numeric provenance check..." >&2
echo "" >&2

# Run verification
if python scripts/verify_numbers.py; then
    echo "✓ All numeric values have proper provenance" >&2
else
    echo "" >&2
    echo "⚠️  Some numeric values lack proper citations" >&2
    echo "   Review warnings above and add citations" >&2
    echo "" >&2
fi

# Exit 0 - warning only, don't block
exit 0
