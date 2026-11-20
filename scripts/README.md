# Scripts

Automation utilities for maintaining the agent's knowledge base and data pipeline.

---

## Available Scripts

### `build_index.py`
**Purpose:** Rebuild `wiki/index.md` from wiki pages  
**Usage:** `python scripts/build_index.py`  
**When to run:** After adding/removing wiki pages

### `validate_structure.py`
**Purpose:** Check that required files and directories exist  
**Usage:** `python scripts/validate_structure.py`  
**When to run:** After initial setup, or when troubleshooting

---

## Adding New Scripts

1. Create script in `scripts/`
2. Add shebang: `#!/usr/bin/env python3`
3. Make executable: `chmod +x scripts/yourscript.py`
4. Document usage in this README
5. Add to relevant workflow in `CLAUDE.md`

---

## Script Conventions

- **Language:** Python 3.11+ (use stdlib when possible)
- **Style:** Follow project conventions (see .claude/rules/ if applicable)
- **Error handling:** Fail loudly with clear error messages
- **Output:** Print progress to stdout, errors to stderr
- **Idempotent:** Safe to run multiple times

---

## Common Script Patterns

### Pipeline Scripts
```python
# Read source → Process → Write output
# Always validate input before processing
# Always write to temp file, then rename (atomic)
```

### Validation Scripts
```python
# Check conditions → Report findings
# Exit 0 if valid, exit 1 if invalid
# Print specific failures, not just "validation failed"
```

### Build Scripts
```python
# Scan input → Generate output
# Skip unchanged files (efficiency)
# Write metadata (date generated, source files)
```

---

## Dependencies

If scripts need external packages, document them here:

```bash
# Install dependencies
pip install -r requirements.txt
```

Create `requirements.txt` if needed.
