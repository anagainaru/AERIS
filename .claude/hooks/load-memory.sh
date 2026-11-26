#!/usr/bin/env bash
# Load Memory Hook
# Displays key memory files at session start
#
# CUSTOMIZE THIS: Adjust which files to display and their order

set -euo pipefail

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 SESSION START - Loading Context"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Display handoff file if it exists
if [ -f ".claude/memory/handoff.md" ]; then
    echo "📌 CURRENT WORK STATE (from .claude/memory/handoff.md):"
    echo ""
    cat .claude/memory/handoff.md
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
fi

# Display hot context if it exists
if [ -f "wiki/hot.md" ]; then
    echo "🔥 RECENT CONTEXT (from wiki/hot.md):"
    echo ""
    head -n 20 wiki/hot.md
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
fi

# Reminder to read key files
echo "💡 REMEMBER TO READ:"
echo "   - wiki/index.md (catalog of all knowledge)"
echo "   - wiki/overview.md (project structure)"
echo "   - .claude/memory/handoff.md (current work state)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

exit 0
