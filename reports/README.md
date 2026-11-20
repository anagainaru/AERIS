# Reports Directory

This directory contains generated outputs from agent queries and analyses.

---

## Purpose

The `reports/` directory stores:

- Analysis outputs (figures, tables, data files)
- Research findings
- Formatted deliverables (presentations, documents)
- Per-query artifacts

---

## Organization

### Option 1: By Query ID (Recommended)
```
reports/
├── query_20261116_143022/
│   ├── figure1.png
│   ├── data.csv
│   └── analysis.txt
└── query_20261116_150315/
    └── results.json
```

Each query gets its own directory with a timestamped ID.

### Option 2: By Topic
```
reports/
├── formation-energies/
├── band-structures/
└── phase-diagrams/
```

Organize by research topic or analysis type.

### Option 3: By Date
```
reports/
├── 2026-11-16/
└── 2026-11-15/
```

Organize by date for temporal tracking.

**Choose one** and stick with it. Document your choice here.

---

## Naming Conventions

If using query IDs:
- Format: `query_YYYYMMDD_HHMMSS`
- Generated automatically by hooks (if configured)
- Linked to checkpoint and conversation history

If using descriptive names:
- Use kebab-case: `reaction-energy-uo2-u3si2`
- Include date prefix: `2026-11-16-reaction-energy`
- Keep names under 50 characters

---

## File Types

Document what file types you typically generate:

- **Figures**: PNG, PDF, SVG
- **Data**: CSV, JSON, HDF5
- **Documents**: LaTeX, Markdown, DOCX
- **Code**: Python scripts, Jupyter notebooks

---

## Archival Policy

- **Keep:** [How long reports are kept, what gets archived]
- **Clean:** [When to clean up old reports]
- **Backup:** [Backup strategy if reports are critical]

---

## Usage in Agent Workflow

The agent should:
1. Create a new subdirectory for each query/analysis
2. Write all outputs to that subdirectory
3. Use consistent naming (query_ID or descriptive)
4. Update checkpoint/summary with output file paths

See CLAUDE.md for the full output protocol.
