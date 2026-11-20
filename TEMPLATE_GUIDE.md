# Skeleton Agent Template - Setup Guide

Welcome! This guide will walk you through customizing the skeleton agent template for your research domain.

---

## Quick Start (15 minutes)

1. **Copy the template**
   ```bash
   cp -r skeleton-agent my-agent-name
   cd my-agent-name
   ```

2. **Run validation**
   ```bash
   python scripts/validate_structure.py
   ```
   Should show all required items present.

3. **Fill in placeholders** (see detailed steps below)

4. **Test with Claude**
   ```bash
   claude
   ```
   Try: "Read wiki/index.md and tell me about this project"

---

## Step-by-Step Customization

### Step 1: Fill in CLAUDE.md

Open `CLAUDE.md` and replace all `[PLACEHOLDERS]`:

**Identity & Domain section:**
- `[AGENT_NAME]` → Your agent's name
- `[DOMAIN_AREA]` → What you're researching
- `[SPECIFIC_CONDITIONS]` → Specific focus or constraints
- `[Topic Area 1-3]` → Your core research topics
- `[Platforms/Facilities]` → Experimental facilities or tools
- `[Codes/Tools]` → Software you use

**Project Overview section:**
- Write 2-3 paragraphs describing your research

**Repository Structure section:**
- Update the directory tree to match your actual structure
- Add or remove sections as needed

**Source Pipeline section:**
- Replace `[document type]`, `[source_folder]`, `[tool/method]`
- Describe your actual 3-track pipeline or modify the structure
- Update Track 1/2/3 details for your domain

**MANDATORY Agent Workflow section:**
- Replace `[memory/handoff.md]` paths with your actual memory file locations
- Update the "READ FIRST" list with your actual file paths

**Delete OPTIONAL sections** that don't apply to your project.

---

### Step 2: Fill in README.md

Open `README.md` and replace:

- `[AGENT_NAME]` → Your agent's name
- `[domain area]` → Your research domain
- `[Research area 1-3]` → Specific research areas
- `[version]` → Python version requirement
- `[installation commands]` → Actual install commands
- `[description of task]` and `[Example prompt]` → Real usage examples

---

### Step 3: Configure Hooks

**Option A: Use the provided hooks (recommended)**

1. Open `.claude/hooks/immutability-guard.sh`
2. Update `PROTECTED_DIRS` array:
   ```bash
   PROTECTED_DIRS=("raw" "data/ground_truth" "papers")
   ```
3. Add your actual read-only directories

**Option B: Disable hooks**

1. Remove or comment out hooks in `.claude/settings.json`
2. Delete `.claude/hooks/` directory if not using

**Option C: Add custom hooks**

1. See `.claude/hooks/` examples
2. Add new hooks to `.claude/settings.json`
3. Make them executable: `chmod +x .claude/hooks/your-hook.sh`

---

### Step 4: Customize the Deep-Read Skill

1. Navigate to `.claude/skills/deep-read-template/`

2. Open `skill.md` and update:
   - `triggers:` → Your actual document types
   - `description:` → Domain-specific description

3. Open `instructions.md` and customize:
   - **Phase 2**: Update field names for your data schema
   - **Output format**: Adjust for your specific extraction format
   - Add domain-specific validation rules

4. **Optional**: Rename the skill
   ```bash
   mv .claude/skills/deep-read-template .claude/skills/my-domain-deep-read
   ```
   Update the `name:` in skill.md to match

---

### Step 5: Set Up Wiki Structure

1. **Decide on sections** (topic areas in your domain)
   ```bash
   mkdir wiki/section-1
   mkdir wiki/section-2
   mkdir wiki/section-3
   ```

2. **Update wiki/index.md**
   - Replace `[Section 1-3 Name]` with your actual sections
   - Add placeholder page entries

3. **Update wiki/overview.md**
   - Describe what each section covers
   - Explain your organization philosophy

4. **Create your first pages**
   ```bash
   # Example concept page
   cat > wiki/section-1/my-concept.md << 'EOF'
   # My Concept
   
   [Description of the concept]
   
   ## Key Points
   - Point 1
   - Point 2
   
   ## References
   [Citation 1]
   EOF
   ```

5. **Rebuild the index**
   ```bash
   python scripts/build_index.py
   ```

---

### Step 6: Configure MCP Integration (Optional)

Only if you're using MCP tools:

1. Open `.mcp.json`
2. Replace `example-server` with your actual MCP server
3. Update `command`, `args`, and `env` variables
4. Remove `"disabled": true` to enable

If NOT using MCP:
- Delete `.mcp.json` or leave it as a template

---

### Step 7: Set Up Data Directory

1. **Organize your data**
   ```bash
   mkdir data/ground_truth
   mkdir data/raw
   mkdir data/extracted
   ```

2. **Update data/README.md**
   - Document your data organization
   - Describe formats and schemas
   - Note any sensitive data policies

3. **Add to immutability guard** (if ground truth should be read-only)
   ```bash
   # In .claude/hooks/immutability-guard.sh
   PROTECTED_DIRS=("data/ground_truth")
   ```

---

### Step 8: Initialize Memory System

1. **Update .claude/memory/handoff.md**
   - Fill in current focus
   - Add initial pending items
   - Remove template placeholders

2. **Update wiki/hot.md**
   - Add today's date
   - Describe project status
   - Note initial setup as recent change

3. **Verify session start hook**
   ```bash
   # Test that memory loads
   claude
   # Should display handoff.md content
   ```

---

### Step 9: Test Everything

1. **Validate structure**
   ```bash
   python scripts/validate_structure.py
   ```
   Should show all green checkmarks

2. **Test index building**
   ```bash
   python scripts/build_index.py
   ```
   Check `wiki/index.md` looks correct

3. **Test with Claude**
   ```bash
   claude
   ```
   Try these commands:
   - "What is this project about?" (tests CLAUDE.md reading)
   - "Show me the wiki index" (tests wiki/index.md)
   - "What's in handoff?" (tests memory system)
   - "List available skills" (tests skills setup)

4. **Test immutability hook** (if configured)
   ```
   # In Claude session:
   Write to data/ground_truth/test.txt with content "test"
   ```
   Should be blocked with immutability error

---

## Advanced Customization

### Adding More Skills

1. Create new skill directory:
   ```bash
   mkdir .claude/skills/my-new-skill
   ```

2. Copy structure from `deep-read-template`

3. Fill in `skill.md` and `instructions.md`

4. Test by invoking in Claude

### Adding Pipeline Scripts

1. Create new Python script in `scripts/`
2. Follow conventions in `scripts/README.md`
3. Make executable: `chmod +x scripts/my-script.py`
4. Document in `scripts/README.md`
5. Reference in CLAUDE.md workflow if it's part of standard process

### Configuring Permissions

Edit `.claude/settings.json` to adjust what the agent can do:

```json
{
  "permissions": {
    "allow": [
      "read:*",
      "bash:ls",
      "bash:find",
      "write:wiki/**",
      "write:reports/**"
    ],
    "deny": [
      "write:data/ground_truth/**"
    ]
  }
}
```

---

## Troubleshooting

### "Hooks not firing"
- Check you're running claude from the agent directory
- Verify hooks are executable: `ls -l .claude/hooks/`
- Check `.claude/settings.json` syntax

### "Agent doesn't read memory files"
- Verify `load-memory.sh` hook is in settings.json
- Check files exist: `ls .claude/memory/`
- Test hook manually: `bash .claude/hooks/load-memory.sh`

### "Index build fails"
- Check Python version: `python --version` (need 3.11+)
- Verify wiki/ directory exists
- Check for syntax errors in markdown files

### "Validation fails"
- Run: `python scripts/validate_structure.py`
- Create missing files/directories as instructed
- Fill in required content

---

## Next Steps

Once your agent is set up:

1. **Add real knowledge**
   - Ingest your first source document using the deep-read skill
   - Add concept and entity pages
   - Build out the wiki

2. **Iterate on workflows**
   - Refine the source pipeline for your documents
   - Add domain-specific validation rules
   - Create additional skills as needed

3. **Establish practices**
   - Update handoff.md after each session
   - Refresh hot.md regularly
   - Run index rebuild when structure changes

4. **Expand as needed**
   - Add more hooks for automation
   - Create specialized skills
   - Build pipeline scripts for common tasks

---

## Template Files Reference

**Core (mandatory):**
- `CLAUDE.md` - Agent instructions (FILL THIS)
- `README.md` - Human docs (FILL THIS)
- `.gitignore` - Git config (USE AS-IS)
- `.claude/settings.json` - Hooks/config (CUSTOMIZE)

**Wiki (mandatory):**
- `wiki/index.md` - Catalog (AUTO-GENERATED)
- `wiki/hot.md` - Recent context (UPDATE EACH SESSION)
- `wiki/overview.md` - Structure guide (FILL THIS)

**Memory (recommended):**
- `.claude/memory/handoff.md` - Work state (UPDATE EACH SESSION)

**Skills (start with 1, grow as needed):**
- `.claude/skills/deep-read-template/` - Example skill (CUSTOMIZE)
- `.claude/skills/README.md` - Skills guide (USE AS-IS)

**Scripts (use provided, add more):**
- `scripts/build_index.py` - Rebuild wiki index (USE AS-IS)
- `scripts/validate_structure.py` - Check setup (USE AS-IS)

**Documentation:**
- `data/README.md` - Data guide (CUSTOMIZE)
- `reports/README.md` - Reports guide (CUSTOMIZE)

---

## Getting Help

If you need assistance:
1. Check CLAUDE.md for agent instructions
2. Read README files in each directory
3. Run validation script: `python scripts/validate_structure.py`
4. Review existing agent examples in parent directory

---

## Completion Checklist

- [ ] Filled all [PLACEHOLDERS] in CLAUDE.md
- [ ] Updated README.md with project details
- [ ] Configured hooks in .claude/settings.json
- [ ] Customized deep-read skill for domain
- [ ] Created wiki section directories
- [ ] Updated wiki/index.md and wiki/overview.md
- [ ] Initialized .claude/memory/handoff.md
- [ ] Updated wiki/hot.md with current state
- [ ] Organized data/ directory
- [ ] Tested with `python scripts/validate_structure.py`
- [ ] Tested with `python scripts/build_index.py`
- [ ] Launched Claude and verified everything works

**When all boxes are checked, your agent is ready to use!** 🎉
