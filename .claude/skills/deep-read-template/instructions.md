# Instructions: Deep Read Template

## Overview

This procedure guides systematic extraction from source documents into structured reports that can be:
- Validated against ground truth
- Referenced during wiki updates
- Used by other agents
- Reviewed by domain experts

**Time investment:** 30-60 minutes per document (depending on length)  
**Output quality:** High fidelity, fully traceable

---

## Prerequisites

Before starting:
- [ ] Document is accessible (file path confirmed)
- [ ] Ground truth data loaded (if applicable)
- [ ] Output location determined
- [ ] Template or gold standard example available for reference

---

## Procedure

### Phase 1: Pre-Read Assessment

**Goal:** Understand document scope before detailed extraction

1. **Read the abstract/introduction** (first 2-3 pages)
   - What is this document about?
   - What data does it contain?
   - What time period/experiments does it cover?

2. **Skim the structure** (headings, figures, tables)
   - Count major sections
   - Identify data-bearing tables and figures
   - Note which sections have extractable information

3. **Check ground truth** (if applicable)
   - Which entities/experiments does this document relate to?
   - What fields are already populated?
   - What fields are missing that this doc might fill?

4. **Write the header**
   ```
   DOCUMENT: [Title]
   AUTHORS: [Authors]
   DATE: [Publication date]
   SOURCE: [Journal/Report number]
   RELATES TO: [Entity IDs or experiment names]
   
   GROUND TRUTH STATUS BEFORE READING:
   - [Field name]: [complete / partial / missing]
   - [Field name]: [complete / partial / missing]
   ```

---

### Phase 2: Section-by-Section Extraction

**Goal:** Read methodically, extract everything relevant

For each major section:

1. **Read the full section** word-for-word
   - Do not skim
   - Do not rely on memory from previous readings

2. **Extract facts as you go**
   - Numeric values with units
   - Qualitative observations
   - Methods and conditions
   - Uncertainties or ranges

3. **Cite precisely**
   - Table numbers: "Table 3, row 5"
   - Figure numbers: "Figure 7(b)"
   - Page numbers: "p. 42, middle paragraph"

4. **Flag issues immediately**
   - Contradictions with ground truth
   - Missing units
   - Ambiguous terminology
   - Data that doesn't match expected ranges

**Example extraction format:**
```
--- [FIELD_NAME] ---

GROUND TRUTH: [Current value if any]

DOCUMENT SAYS: [Value] [units]
  Location: [Table X / Figure Y / p. Z]
  Context: [Any important qualifiers]

UNIT CONVERSION: [If needed]
  Document: [X] [unit1]
  Standard: [Y] [unit2]
  Formula: [Conversion formula]

CROSS-CHECK:
  ✓ Matches GT [within tolerance]
  OR
  ⚠️ MISMATCH: GT=[X], Doc=[Y], Diff=[Z]%
  Explanation: [Why this might differ]
```

---

### Phase 3: Document Structure Guide

**Goal:** Guidance for future reads or automated extraction

Write a section describing:

**EXTRACT (priority content):**
- Table 1: [What it contains, which columns matter]
- Table 3: [What it contains, which columns matter]
- Figure 5: [What data is shown]

**SKIP (not relevant):**
- Section 2.1: [Why it's not relevant]
- Tables 7-9: [Why they're not needed]

**AMBIGUOUS (needs human judgment):**
- Figure 8: [What's unclear, what would resolve it]

---

### Phase 4: Summary & Validation

**Goal:** Verify completeness and flag issues

1. **Completeness check**
   - [ ] Every table mentioned in assessment was processed
   - [ ] Every figure with data was reviewed
   - [ ] All numeric values have units
   - [ ] All citations are specific (not "the paper")

2. **Cross-validation summary**
   ```
   VALIDATION RESULTS:
   - Fields matching GT: [count]
   - Fields with mismatches: [count] (see details above)
   - New fields populated: [count]
   - Fields still missing: [count]
   ```

3. **Key findings**
   - What are the 3-5 most important data points from this document?
   - Any surprises or non-obvious findings?
   - What questions does this document answer?
   - What questions remain open?

4. **Contradictions and discrepancies**
   - List all mismatches with ground truth
   - For each, note:
     - Magnitude of difference
     - Possible explanations (methodology, timing, measurement technique)
     - Recommendation (update GT / keep GT / investigate further)

---

## Output Format

Save as: `[output_directory]/[document_short_name]_extraction.txt`

**Required sections:**
1. HEADER (document metadata + GT status)
2. CRITICAL CONTEXT (scope and pitfalls)
3. PER-FIELD EXTRACTION (one section per field)
4. DOCUMENT STRUCTURE GUIDE (what to extract/skip)
5. VALIDATION SUMMARY (completeness and cross-checks)
6. KEY FINDINGS (insights and open questions)

---

## Validation Checklist

Before finalizing:

- [ ] Output file follows template structure
- [ ] Every numeric value has a citation
- [ ] Every numeric value has explicit units
- [ ] Contradictions are explained, not ignored
- [ ] Ground truth status is documented
- [ ] Output is human-readable and agent-parseable

---

## Common Pitfalls

**❌ Skipping sections** → Always read word-for-word  
**❌ Vague citations** → Always cite specific tables/figures/pages  
**❌ Missing units** → Never extract a number without its unit  
**❌ Silent overwrites** → Always flag GT mismatches  
**❌ Memory-based extraction** → Always re-read the actual text

---

## Example Use

```
User: "Read HWR-411 and extract IFA-563 data"

Agent:
1. Reads .claude/skills/deep-read-template/instructions.md
2. Follows Phase 1-4 procedure
3. Writes data/extraction/hwr411_extraction.txt
4. Reports: "Extraction complete. Found 23 data points, 2 GT mismatches flagged."
```

---

## Customization Guide

To adapt this skill for your domain:

1. **Update field names** in the per-field extraction examples
2. **Add domain-specific validation rules** (e.g., "density must be 10-11 g/cm³")
3. **Specify output format** for your schema (JSON, CSV, markdown table, etc.)
4. **Add tool scripts** if needed (e.g., `extract_table.py`, `convert_units.py`)
5. **Create gold standard example** in your domain for reference
