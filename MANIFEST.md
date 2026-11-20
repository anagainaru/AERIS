# Skeleton Agent Template - Manifest

This document lists all files included in the minimal skeleton agent template.

**Created:** 2026-11-16  
**Version:** 1.0 (Minimal)

---

## Template Contents

### Core Documentation
```
CLAUDE.md                   - Main agent instructions (FILLABLE)
README.md                   - Project overview for humans (FILLABLE)
TEMPLATE_GUIDE.md           - Step-by-step setup instructions
MANIFEST.md                 - This file (inventory)
.gitignore                  - Git ignore patterns
```

### Claude Configuration
```
.claude/
├── settings.json           - Hooks and permissions config
├── hooks/
│   ├── immutability-guard.sh    - Prevents writes to protected dirs
│   └── load-memory.sh           - Loads memory at session start
├── memory/
│   └── handoff.md               - Work state tracking (FILLABLE)
└── skills/
    ├── README.md                - Skills documentation
    └── deep-read-template/
        ├── skill.md             - Skill metadata (CUSTOMIZABLE)
        └── instructions.md      - Detailed procedure (CUSTOMIZABLE)
```

### Knowledge Base
```
wiki/
├── index.md                - Catalog of all pages (AUTO-GENERATED)
├── hot.md                  - Recent context cache (UPDATE EACH SESSION)
└── overview.md             - Project structure guide (FILLABLE)
```

### Automation Scripts
```
scripts/
├── README.md               - Scripts documentation
├── build_index.py          - Rebuild wiki index (executable)
└── validate_structure.py   - Check agent setup (executable)
```

### Data & Reports
```
data/
└── README.md               - Data organization guide (CUSTOMIZABLE)

reports/
└── README.md               - Reports structure guide (CUSTOMIZABLE)
```

### MCP Integration
```
.mcp.json                   - MCP server configuration (OPTIONAL)
```

---

## File Types by Purpose

### Fillable Templates
Files with [PLACEHOLDERS] to replace:
- CLAUDE.md
- README.md
- wiki/overview.md
- wiki/hot.md
- .claude/memory/handoff.md

### Customizable Examples
Working examples to modify for your domain:
- .claude/skills/deep-read-template/skill.md
- .claude/skills/deep-read-template/instructions.md
- .claude/hooks/immutability-guard.sh (PROTECTED_DIRS array)
- data/README.md (organization structure)
- reports/README.md (naming conventions)

### Use As-Is
Files that work without modification:
- .gitignore
- .claude/hooks/load-memory.sh
- scripts/build_index.py
- scripts/validate_structure.py
- .claude/skills/README.md
- scripts/README.md
- TEMPLATE_GUIDE.md

### Auto-Generated
Files created by scripts:
- wiki/index.md (rebuilt by build_index.py)

---

## Comparison to Full Agent Patterns

This minimal template includes:
- ✅ Core documentation (CLAUDE.md, README.md)
- ✅ Basic hooks (2: immutability, session start)
- ✅ One example skill (deep-read-template)
- ✅ Wiki foundation (index, hot, overview)
- ✅ Memory system (handoff.md)
- ✅ Pipeline scripts (2: build_index, validate_structure)
- ✅ MCP template (disabled by default)

Not included (available in full agents):
- ❌ Checkpoint protocol (fuel-agent pattern)
- ❌ Citation framework (cvd-agent pattern)
- ❌ Session export (qe-agent pattern)
- ❌ Observability system (cvd-agent pattern)
- ❌ Multiple validation hooks
- ❌ Behavior.md, domain-constants.md, open-questions.md
- ❌ .claude/commands/ slash commands
- ❌ .claude/knowledge/ procedures

Scientists can add these incrementally as needed.

---

## Setup Time Estimate

- **Minimal setup:** 15 minutes (fill placeholders, basic test)
- **Complete customization:** 1-2 hours (custom skills, wiki structure, first pages)
- **Production ready:** 4-8 hours (full knowledge base, tested workflows)

---

## Next Steps After Setup

1. **Validate:** `python scripts/validate_structure.py`
2. **Customize:** Follow TEMPLATE_GUIDE.md
3. **Test:** Launch Claude and try basic queries
4. **Populate:** Add first source documents and wiki pages
5. **Iterate:** Refine skills and workflows for your domain

---

## Version History

**v1.0 (2026-11-16) - Minimal Template**
- Core documentation
- 2 essential hooks
- 1 example skill (deep-read)
- Wiki foundation
- Basic memory system
- 2 pipeline scripts
- MCP template

Future versions may include:
- Standard template (adds more hooks, skills)
- Full template (complete observability, checkpointing)
- Domain-specific variants (materials, nuclear, chemistry)
