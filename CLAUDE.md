# CLAUDE.md — [AGENT_NAME]

<!-- 
INSTRUCTIONS FOR DOMAIN SCIENTISTS:
Replace all [PLACEHOLDERS] in this template with your domain-specific information.
Delete any sections marked OPTIONAL if they don't apply to your project.
Keep the MANDATORY sections - these are critical for agent operation.
-->

This file provides guidance to Claude Code when working in `[path/to/this/agent/]`.

---

## Identity & Domain

**[AGENT_NAME]** — [Short identity/role description]

This agent researches [DOMAIN_AREA] under [SPECIFIC_CONDITIONS]. Core topics:

- **[Topic Area 1]:** [specific subtopics, methods, phenomena]
- **[Topic Area 2]:** [specific subtopics, methods, phenomena]
- **[Topic Area 3]:** [specific subtopics, methods, phenomena]
- **Platforms/Facilities:** [experimental facilities, reactors, instruments]
- **Codes/Tools:** [simulation codes, analysis software, frameworks]
- **Regulatory context (OPTIONAL):** [standards, constraints, compliance requirements]
- **Instruments/Methods:** [characterization techniques, measurement tools]

---

## Project Overview

[2-3 paragraph description of the research project]

[Paragraph 1: What is being studied and why]

[Paragraph 2: Key research questions or objectives]

[Paragraph 3 (OPTIONAL): Context - how this fits into larger research program]

---

## Repository Structure

<!-- Update this tree to match your actual folder structure -->

```
[agent-name]/
├── CLAUDE.md              # This file — agent instructions
├── AGENTS.md              # Agent documentation (OPTIONAL)
├── README.md              # Project overview for humans
│
├── .claude/               # Claude-specific configuration
│   ├── settings.json      # Hooks, permissions, configuration
│   ├── settings.local.json # Local overrides (gitignored)
│   ├── skills/            # Custom capabilities
│   ├── hooks/             # Event-driven automation (OPTIONAL)
│   ├── commands/          # Slash commands (OPTIONAL)
│   ├── memory/            # Persistent context (OPTIONAL)
│   └── knowledge/         # Domain rules & procedures (OPTIONAL)
│
├── .mcp.json              # MCP tool integrations (OPTIONAL)
│
├── wiki/                  # THE KNOWLEDGE BASE
│   ├── index.md           # Master catalog — read FIRST every query
│   ├── hot.md             # Recent context cache (~500 words)
│   ├── overview.md        # Project structure and layers
│   ├── glossary.md        # Domain terminology (OPTIONAL)
│   ├── [section-1]/       # Domain-organized pages
│   ├── [section-2]/       # Domain-organized pages
│   └── log.md             # Change log (OPTIONAL)
│
├── data/                  # Input datasets, ground truth
│   ├── [dataset_name].xlsx/csv  # Primary data files
│   └── schema_keywords/   # Extraction templates (OPTIONAL)
│
├── raw/                   # READ-ONLY extracted sources (OPTIONAL)
│   └── [platform]/        # Organized by source platform
│
├── scripts/               # Automation utilities
│   └── [pipeline_scripts] # Data processing, validation
│
├── reports/               # Generated outputs
│   └── [query_id]/        # Per-query research outputs
│
├── papers/                # Reference materials (OPTIONAL)
└── notebooks/             # Jupyter notebooks (OPTIONAL)
```

**Key directory roles:**
- `wiki/` — [describe purpose and organization]
- `data/` — [describe what data is stored here]
- `raw/` (if applicable) — [describe source material policy: READ-ONLY, immutable, etc.]
- `reports/` — [describe output conventions]
- `scripts/` — [describe automation purpose]

---

## Source Pipeline — MANDATORY for every new [document type]

<!-- This is the standard 3-track pipeline pattern. Adjust as needed. -->

**Every [document type] added to `[source_folder]/` MUST go through this pipeline before being considered ingested.**

```
[source_folder]/[file]
   │
   ├─ Track 1: [Deep-read skill/process name]
   │            Agent reads with [tool/method], cross-references against [ground truth]
   │            Produces: [output_file_location]
   │            Contains: [what sections/content]
   │
   ├─ Track 2: [Automated extraction tool]
   │            Pipeline: [tool_name] ([installation/command])
   │            Produces: [output_location]
   │            Contains: [structured markdown, tables, equations, figures]
   │
   └─ Track 3: [Validation/cross-check]
                Cross-validates against: [ground_truth_source]
                Produces: [validation_output]
                Policy: [how to handle mismatches - flag, investigate, update]
```

### Track 1: [Deep-Read Process Name]

[Describe the manual/agent-driven deep-read process]

**Output format:** `[path/pattern]`

**Required sections:**
1. [Section name]: [purpose]
2. [Section name]: [purpose]
3. [Section name]: [purpose]

**Template:** `[path/to/gold_standard_template]`

### Track 2: [Automated Extraction]

[Describe automated extraction tool and process]

**Installation:** `[installation command]`

**Usage:** `[command with flags]`

**Output location:** `[path/pattern]`

### Track 3: [Validation/Ground Truth Cross-Check]

[Describe validation process]

**Ground truth source:** `[file/database path]`

**Cross-check policy:** 
- [How to handle mismatches]
- [When to update ground truth]
- [When to flag for human review]

---

## MANDATORY Agent Workflow (every task, no exceptions)

```
1. READ FIRST — before any task:
   ├── [memory/README.md or equivalent]     → [what this contains]
   ├── [memory/handoff.md]                  → [current work state]
   ├── [wiki/hot.md]                        → [recent context cache]
   ├── [wiki/index.md]                      → [catalog of all pages]
   └── [wiki/overview.md]                   → [project structure]

2. DRILL IN as the task requires:
   ├── [wiki/sources/<paper>.md]            for any [document] mentioned
   ├── [data/ground_truth.xlsx]             for [data type] facts
   ├── [wiki/[section]/<page>.md]           for [topic] background
   └── [memory/domain-constants.md]         for [specific values/parameters]

3. DO THE WORK
   ├── Use wiki knowledge before re-reading raw [documents]
   ├── Cross-reference numeric claims against [ground_truth_source]
   ├── Cross-check qualitative claims against [source_location]
   └── Flag contradictions — never silently overwrite

4. WRITE FINDINGS BACK
   ├── New [document]    → [Track 1/2/3 pipeline location]
   ├── New insight       → [wiki/concepts/<Concept>.md]
   ├── Open question     → [wiki/questions/<Q>.md]
   ├── [Data correction] → [data/file.xlsx] + re-run [validation script]
   └── Session synthesis → append to [wiki/log.md], refresh [wiki/hot.md]

5. MANDATORY SESSION CLOSE (every substantive session)
   ├── Update [sessions/TODO.md or equivalent] — mark done/in-progress
   ├── Update [memory/handoff.md] with current work state
   ├── Refresh [wiki/hot.md] if wiki was changed
   └── Append to [wiki/log.md] (new entries at TOP)
```

---

## Skills (OPTIONAL)

<!-- List custom skills in .claude/skills/ -->

The agent has access to these custom capabilities:

### Input/Ingestion Skills
- **[skill-name]**: [what it does, when to use it]
- **[skill-name]**: [what it does, when to use it]

### Output/Analysis Skills
- **[skill-name]**: [what it does, when to use it]
- **[skill-name]**: [what it does, when to use it]

### Utility Skills
- **[skill-name]**: [what it does, when to use it]

---

## Hooks & Automation (OPTIONAL)

<!-- Describe any hooks configured in .claude/settings.json -->

### Active Hooks

**UserPromptSubmit:**
- [Hook name]: [what it does]

**PreToolUse:**
- [Hook name]: [what it blocks/enforces]

**PostToolUse:**
- [Hook name]: [what it auto-commits/validates]

**Stop:**
- [Hook name]: [what it checks/warns about]

**SessionStart/SessionEnd:**
- [Hook name]: [what it initializes/compiles]

---

## Hard Rules (non-negotiable)

<!-- Critical constraints the agent MUST follow -->

### Immutability Rules
- **[folder]/ is READ-ONLY** — never edit files here; a PreToolUse hook denies edits
- [Other immutability constraints]

### Naming Conventions
- [File naming pattern]: `[pattern_example]`
- [Folder naming pattern]: `[pattern_example]`
- [ID generation]: `[pattern_example]`

### Output Requirements
- [Every X must produce Y]
- [Format requirements]
- [Validation requirements]

### Citation Requirements
- Cite wiki pages as: `[[Page Name]]`
- Cite source documents as: `(Source: [path])`
- [Other citation requirements]

### Git/Version Control
- [Commit message format]
- [What gets committed vs gitignored]
- [Branch naming conventions]

---

## Memory System (OPTIONAL)

<!-- If using persistent memory -->

The agent maintains persistent context in `[memory/]`:

- **[memory/handoff.md]**: Current work state, pending items
- **[memory/hot.md]**: Recent session summary (~500 words)
- **[memory/behavior.md]**: User-corrected behaviors to maintain
- **[memory/domain-constants.md]**: Verified numerical values
- **[memory/open-questions.md]**: Active research gaps
- **[memory/environment.md]**: Tool/skill usage notes

**Update policy:** [When and how to update memory files]

---

## Citation Framework

This agent uses a **dual-citation system** to ensure all facts are traceable to their sources.

### Citation Format

**Every numeric value or claim must use:**

```markdown
[VALUE] [UNIT] [n] ([[Wiki-Page-Name]])
```

**Example:**
```markdown
The density is 10.5 g/cm³ [1] ([[PyC-Properties]])
```

**Components:**
- `[n]` - Primary citation (original source document)
- `([[Wiki-Page-Name]])` - Secondary citation (compiled wiki page)

### Citation Registry

**papers/corpus-meta.csv** - Central registry of all sources
```csv
citekey,authors,year,title,source_type,source_id,file_path
paper1,Smith et al.,2024,Study of X,journal,doi:10.xxxx,raw/papers/paper1.pdf
```

**papers/citemaps/** - Per-source citation maps
```tsv
cite_num	location	description
1	L145-147	Temperature measurement
2	Table 3	Density values
```

### Numeric Value Protocol

When reporting ANY numeric value, you MUST:

1. **Explicit units**: Always specify (e.g., "10.5 g/cm³" not "10.5")
2. **Source citation**: Include [n] and ([[Page]])
3. **Source location**: Cite specific table/figure/page
4. **Cross-validation**: Check against ground truth, flag mismatches
5. **Unit conversions**: Document formula and show both values
6. **Context**: State conditions (temperature, composition, etc.)

**Domain-specific conversions** (CUSTOMIZE):
- [UNIT_A] → [UNIT_B]: [CONVERSION_FORMULA]
- [UNIT_C] → [UNIT_D]: [CONVERSION_FORMULA]

### Enforcement

**Hooks automatically check:**
- `cite-presence-guard.py` (PostToolUse) - Warns if wiki pages lack citations
- `verify-numeric-provenance.sh` (Stop) - Validates numeric citations when wiki/sources/ changes

**Manual verification:**
```bash
python scripts/cite_resolve.py wiki/
```

### Workflow

**During ingestion:**
1. Extract fact from source
2. Assign citation number [n]
3. Create citemap entry in papers/citemaps/<source>.tsv
4. Write to wiki with dual citation
5. Run cite_resolve.py to verify

**Disable if not using:**
Set in `.claude/settings.json`:
```json
"PostToolUse": {
  "cite-presence-guard": { "enabled": false }
}
```

See `papers/README.md` for complete documentation.

---

## Domain-Specific Guidelines

<!-- Add domain-specific rules, conventions, terminology -->

### [Domain Topic 1]

[Specific guidance for this topic area]

**Key concepts:**
- [Concept]: [definition/constraint]
- [Concept]: [definition/constraint]

**Common pitfalls:**
- [Pitfall]: [how to avoid]

### [Domain Topic 2]

[Specific guidance for this topic area]

---

## CLI Commands (OPTIONAL)

<!-- Custom slash commands if implemented -->

- `/[command-name]` — [what it does]
- `/[command-name]` — [what it does]

---

## Tools & Integrations (OPTIONAL)

### MCP Servers

<!-- If using MCP tools, list them -->

- **[mcp-server-name]**: [what tools it provides, when to use]

### External Tools

- **[tool-name]**: [purpose, installation, usage]

---

## Checkpoint Protocol (OPTIONAL)

<!-- If implementing structured output tracking like fuel-agent -->

Every response writes these artifacts:

### Per-turn JSON — `[checkpoints/<query_id>/turn_NNN.json]`

```json
{
  "turn": 1,
  "timestamp": "[ISO8601]",
  "reasoning": "[why these tools were called]",
  "tool_decisions": [],
  "tool_results": []
}
```

### Summary JSON — `[checkpoints/<query_id>/summary.json]`

```json
{
  "operation": "query",
  "session_id": "[query_id]",
  "context": "[user prompt]",
  "final_answer": "[summary]",
  "output_files": [],
  "execution_status": "complete"
}
```

**Enforcement:** [Which hooks enforce this, how it's validated]

---

## Legacy & Migration Notes (OPTIONAL)

<!-- If there are deprecated systems or ongoing migrations -->

[Describe what's legacy, what's current, where new work should go]

---

## Quick Start for New Sessions

**Every session, start with:**
1. Read `[wiki/hot.md]` — recent context
2. Read `[wiki/index.md]` — find relevant pages
3. Check `[memory/handoff.md or TODO]` — what's pending
4. Do your work following the MANDATORY workflow above
5. Update memory and close properly

**Common tasks:**
- To ingest a new [document]: Follow the Source Pipeline
- To answer a question: Read wiki first, cite sources
- To add new knowledge: Update relevant wiki pages
- To report a finding: Write to `[reports/]` with proper naming

---

## References

<!-- Link to related documentation -->

- Main README: [README.md]
- Wiki schema: [wiki/wiki-schema.md] (OPTIONAL)
- [Other key documentation]
