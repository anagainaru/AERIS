---
name: deep-read-template
description: Methodical section-by-section document reading with structured extraction and cross-validation
triggers:
  - "When ingesting a new [document type] into the knowledge base"
  - "When user asks to 'deep read' or 'extract from' a document"
  - "Before adding any new source document to the wiki"
---

# Skill: Deep Read Template

## Purpose

This skill provides a **methodical, structured approach** to reading and extracting information from source documents. It ensures:

- Complete coverage (nothing missed)
- Cross-validation against ground truth
- Structured, reusable output
- Consistent extraction quality

## When to Use

- **Every new document** added to the project
- When you need to extract specific data points systematically
- When re-reading a document to resolve contradictions
- When building or updating entity/concept pages from a source

## Customization for Your Domain

This is a **template skill** — customize it for your specific document types:

1. Update the document types in the frontmatter triggers
2. Modify the output format in `instructions.md`
3. Add domain-specific validation rules
4. Adjust the per-field guidance for your data schema

## Input

- **Document path**: Path to the file to read (PDF, markdown, Excel, etc.)
- **Ground truth reference** (optional): Path to validation data
- **Output path**: Where to write the extraction report

## Output

A structured extraction report containing:

1. **Header**: Document citation, target entities
2. **Critical context**: What the document IS/IS NOT, extraction pitfalls
3. **Per-field extraction**: For each data field:
   - Current known values
   - Terms used in this document
   - Units and conversions
   - Cross-validation notes
4. **Document structure guide**: What to extract vs skip
5. **Findings summary**: Key data points, contradictions, gaps

## Quality Markers

✅ **Good extraction:**
- Every section of document was read
- Numeric values cite specific tables/figures
- Units are explicit and conversions shown
- Contradictions with ground truth are flagged
- Output follows template structure

❌ **Incomplete extraction:**
- Skipped sections
- Vague references ("the paper says...")
- Missing units
- Silent overwriting of ground truth
- Free-form prose instead of structured output

## See Also

- `instructions.md` for detailed step-by-step procedure
- Example outputs in `[data/schema_keywords/]` or similar
- Gold standard template: `[path/to/best_example]`
