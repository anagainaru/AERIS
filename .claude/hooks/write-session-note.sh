#!/usr/bin/env bash
# Write Session Note (SessionEnd Hook)
# Compiles session summary when exiting
# Triggered on /exit, /quit, or Ctrl-D

set -euo pipefail

# Configuration
SESSIONS_DIR="sessions/notes"
TODAY=$(date +%Y-%m-%d)
SESSION_FILE="$SESSIONS_DIR/$TODAY.md"

# Create sessions directory if needed
mkdir -p "$SESSIONS_DIR"

# Generate session note
echo "📝 Generating session note..." >&2

cat > "$SESSION_FILE" <<HEADER
# Session Note - $TODAY

**Date:** $TODAY
**Generated:** $(date +"%Y-%m-%d %H:%M:%S")

---

## Session Summary

HEADER

# Try to gather information about what was done
# This is a basic version - customize based on your needs

# Check if there were wiki changes
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if ! git diff --quiet wiki/ 2>/dev/null || ! git diff --cached --quiet wiki/ 2>/dev/null; then
        echo "### Wiki Changes" >> "$SESSION_FILE"
        echo "" >> "$SESSION_FILE"
        echo '```' >> "$SESSION_FILE"
        git status --short wiki/ >> "$SESSION_FILE" 2>/dev/null || true
        echo '```' >> "$SESSION_FILE"
        echo "" >> "$SESSION_FILE"
    fi
fi

# Check if there were file changes
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
        echo "### Files Modified" >> "$SESSION_FILE"
        echo "" >> "$SESSION_FILE"
        echo '```' >> "$SESSION_FILE"
        git status --short >> "$SESSION_FILE" 2>/dev/null || true
        echo '```' >> "$SESSION_FILE"
        echo "" >> "$SESSION_FILE"
    fi
fi

# Add placeholders for manual completion
cat >> "$SESSION_FILE" <<FOOTER

---

## Work Completed

[FILL IN: What was accomplished this session]

-
-
-

---

## Key Decisions

[FILL IN: Important choices made and rationale]

-
-

---

## Discoveries

[FILL IN: Non-obvious findings or insights]

-
-

---

## Next Steps

[FILL IN: What to work on next]

- [ ]
- [ ]
- [ ]

---

## Notes

[FILL IN: Any other context or reminders]

FOOTER

echo "✓ Session note written: $SESSION_FILE" >&2
echo "" >&2
echo "📌 Complete the session note by filling in:" >&2
echo "   • Work Completed" >&2
echo "   • Key Decisions" >&2
echo "   • Discoveries" >&2
echo "   • Next Steps" >&2
echo "" >&2

exit 0
