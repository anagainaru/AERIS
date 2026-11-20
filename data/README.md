# Data Directory

This directory contains input datasets, ground truth data, and extracted information.

---

## Purpose

The `data/` directory serves as the **data layer** for the agent:

- **Input data**: Raw datasets to be analyzed
- **Ground truth**: Validated reference data for cross-validation
- **Extracted data**: Structured outputs from source documents
- **Intermediate data**: Processing artifacts

---

## Typical Organization

```
data/
├── ground_truth/       # Validated reference data (read-only)
├── raw/                # Unprocessed input files
├── processed/          # Cleaned/transformed data
├── extracted/          # Outputs from deep-read/extraction skills
└── README.md           # This file
```

**Customize this structure** based on your domain needs.

---

## Data Management Guidelines

### Ground Truth
- Keep ground truth in a separate subdirectory
- Consider making it read-only (add to immutability hook)
- Version control or backup regularly
- Document provenance (where did this data come from?)

### Large Files
- Add to `.gitignore` if files are large (>10MB)
- Consider external storage (S3, shared drive) with local copies
- Document how to obtain data if not committed

### Sensitive Data
- **Never commit** sensitive data to git
- Use `.env` files for credentials (gitignored)
- Document access procedures in this README

---

## Data Formats

Document the formats used in your project:

- **[Format 1]**: [Description, example file]
- **[Format 2]**: [Description, example file]

---

## Schema Documentation

If your data follows a schema, document it here or link to schema files:

- Schema file: `data/schema.json` or similar
- Field descriptions
- Valid ranges
- Units and conventions

---

## Usage in Agent Workflow

The agent should:
1. Read ground truth at session start (if applicable)
2. Cross-validate extracted values against ground truth
3. Never overwrite ground truth without explicit confirmation
4. Flag discrepancies for human review

See CLAUDE.md for the full data validation workflow.
