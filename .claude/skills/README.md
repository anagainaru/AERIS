# Skills

Skills are packaged procedures that the agent can invoke to perform complex, multi-step tasks.

---

## What is a Skill?

A skill is a self-contained capability with:
- Clear trigger conditions (when to use it)
- Step-by-step instructions
- Input/output specifications
- Quality checks or validation steps

---

## Creating a New Skill

### 1. Create a directory
```bash
mkdir .claude/skills/my-skill-name
```

### 2. Create `skill.md` with frontmatter
```markdown
---
name: my-skill-name
description: One-line description of what this skill does
triggers:
  - "When user asks to [action]"
  - "When you need to [capability]"
---

# Skill: [Name]

[Detailed description of the skill's purpose and when to use it]
```

### 3. Create `instructions.md` with procedure
```markdown
# Instructions: [Skill Name]

## Overview
[What this skill does, inputs, outputs]

## Procedure

### Step 1: [Action]
[Detailed instructions]

### Step 2: [Action]
[Detailed instructions]

## Validation
[How to verify the skill worked correctly]

## Common Issues
[Known pitfalls and how to avoid them]
```

---

## Naming Conventions

- Use kebab-case: `deep-read-file`, `wiki-ingest`, `answer-query`
- Be specific: `coating-db-ingest` not just `ingest`
- Use verbs: `export-sessions`, `validate-data`

---

## Skill Composition

Skills can call other skills:
- **Foundational skills**: Low-level capabilities (fetch, parse, validate)
- **Workflow skills**: Compose multiple skills into pipelines
- **Domain skills**: High-level, domain-specific procedures

Example hierarchy:
```
qe-electronic-structure (workflow)
├── qe-dos (analysis)
│   ├── qe-setup-calc (foundation)
│   └── fetch-mp-structure (foundation)
└── qe-bands (analysis)
    └── qe-setup-calc (foundation)
```

---

## Example Skills in This Template

- **deep-read-template**: Generic document reading and extraction pattern

---

## Best Practices

1. **Single responsibility**: One skill, one clear purpose
2. **Composable**: Skills should work together
3. **Validated**: Include checks that output is correct
4. **Documented**: Clear triggers and usage examples
5. **Tested**: Try the skill on real data before committing

---

## Invoking Skills

Skills are invoked via the Skill tool:
```
Skill(skill="skill-name", args="optional arguments")
```

Or directly in chat:
```
/skill-name [arguments]
```

---

## Common Skill Patterns

### Ingestion Skills
Extract data from source documents into structured format
- Input: Source file path
- Output: Structured data, validation report
- Example: `deep-read-template`

### Analysis Skills
Perform calculations or computations
- Input: Data files, parameters
- Output: Results, figures, tables
- Example: `compute-formation-energy`

### Export Skills
Convert or format data for external use
- Input: Internal data structures
- Output: Reports, presentations, data files
- Example: `export-latex-report`

### Workflow Skills
Orchestrate multiple steps
- Input: High-level goal
- Output: Complete analysis or deliverable
- Example: `full-characterization-pipeline`

---

## For Domain Scientists

Start with the `deep-read-template` example and customize it for your domain:

1. Copy the template directory
2. Rename to match your use case
3. Update the frontmatter (name, description, triggers)
4. Customize the instructions for your document types
5. Add domain-specific validation steps
6. Test on sample documents
