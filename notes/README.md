# Session Notes

Automatically generated session summaries created on `/exit`.

---

## Purpose

Session notes provide:
- **Daily record** of work completed
- **Decisions log** with rationale
- **Discoveries** that were non-obvious
- **Next steps** for continuity

---

## Format

Each file: `YYYY-MM-DD.md`

**Structure:**
```markdown
# Session Note - YYYY-MM-DD

## Session Summary
[Auto-generated: file changes, wiki updates]

## Work Completed
[Manual: what was accomplished]

## Key Decisions
[Manual: choices made and why]

## Discoveries
[Manual: non-obvious findings]

## Next Steps
[Manual: actionable items for next session]

## Notes
[Manual: other context]
```

---

## Workflow

**Automatic (on `/exit`):**
1. SessionEnd hook generates file
2. Fills in file changes automatically
3. Adds placeholders for manual sections

**Manual (complete the note):**
1. Fill in "Work Completed"
2. Document "Key Decisions"
3. Note "Discoveries"
4. List "Next Steps"

---

## Usage

**View today's session:**
```bash
cat sessions/notes/$(date +%Y-%m-%d).md
```

**Edit today's session:**
```bash
# Fill in the manual sections
vim sessions/notes/$(date +%Y-%m-%d).md
```

**Review recent sessions:**
```bash
ls -t sessions/notes/ | head -5
```

---

## Integration with Memory

**After completing a session note:**
1. Update `.claude/memory/handoff.md` with next steps
2. Update `wiki/hot.md` if wiki changed
3. Commit the session note for team visibility (optional)

---

## Disable Automatic Generation

To disable automatic session notes:

Edit `.claude/settings.json`:
```json
"SessionEnd": {
  "write-session-note": {
    "enabled": false
  }
}
```

---

## Customization

The session note template can be customized in:
`.claude/hooks/write-session-note.sh`

Add custom sections, change format, or integrate with other tools.
