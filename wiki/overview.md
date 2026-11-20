# Project Overview

> 📚 High-level explanation of how this knowledge base is organized

---

## Purpose

This wiki serves as the **compiled knowledge layer** for [AGENT_NAME]. It contains:

- Domain concepts and methods
- Facts about [entities/experiments/platforms]
- Extracted information from source documents
- Open research questions
- Cross-comparisons and analyses

---

## Organization Philosophy

### Compilation, Not Archival

This wiki contains **compiled insights**, not complete source documents. Each page:
- Synthesizes information from multiple sources
- Cites original references
- Highlights contradictions or gaps
- Provides context for interpretation

Raw source documents live in `[raw/]` or `[papers/]` and remain immutable.

### Topic-Centric Structure

Pages are organized by **topic/concept**, not by source document. A single paper may contribute facts to dozens of wiki pages across different sections.

---

## Sections

### [Section 1 Name]
**Purpose:** [What this section covers]  
**Contains:** [Types of pages in this section]  
**Use when:** [When to read pages in this section]

### [Section 2 Name]
**Purpose:** [What this section covers]  
**Contains:** [Types of pages in this section]  
**Use when:** [When to read pages in this section]

### [Section 3 Name]
**Purpose:** [What this section covers]  
**Contains:** [Types of pages in this section]  
**Use when:** [When to read pages in this section]

---

## Page Types

### Concept Pages
- Explain domain concepts, methods, phenomena
- Example: `[Concept-Name].md`
- Cite multiple sources
- Highlight current understanding and open questions

### Entity Pages
- Facts about specific specimens, experiments, platforms
- Example: `[Entity-ID].md`
- Often include data tables
- Link to related entities

### Source Pages
- Per-document summaries
- Combine extraction analysis + validation
- Located in `wiki/sources/`
- Used as reference during ingestion

### Question Pages
- Open research questions
- Current hypotheses
- What would resolve the question
- Located in `wiki/questions/`

---

## Knowledge Layers

The agent's knowledge comes from **three layers**:

1. **Ground truth data** (`data/`)
   - Primary datasets, validated facts
   - Cross-reference authority for numeric values

2. **Compiled wiki** (`wiki/`)
   - Synthesized knowledge from all sources
   - Agent reads this layer first

3. **Raw sources** (`[raw/]` or `[papers/]`)
   - Original documents (PDFs, reports)
   - READ-ONLY, immutable
   - Consulted only when wiki doesn't have enough detail

---

## Update Protocol

When new information is added:

1. **Extract** from source document (via deep-read or pipeline)
2. **File** to appropriate wiki pages by topic
3. **Cross-reference** against existing knowledge
4. **Flag** contradictions for human review
5. **Update** this index and hot.md

---

## For Domain Scientists

**Adding new knowledge:**
- New concepts → Create concept page in relevant section
- New entities → Create entity page with standard template
- New sources → Run through source pipeline (see CLAUDE.md)

**Maintaining quality:**
- Every claim must cite a source
- Contradictions should be documented, not hidden
- Update `wiki/hot.md` after each session
- Rebuild `wiki/index.md` when structure changes
