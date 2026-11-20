# Wiki Index

**Last updated:** [DATE]  
**Total pages:** [NUMBER]

> 📖 **READ THIS FIRST** every session to understand what knowledge is available.

## Overview

This wiki contains compiled domain knowledge organized by topic. The agent reads this catalog to locate relevant information before answering questions.

---

## Sections

### [Section 1 Name]
*[Brief description of what this section covers]*

- [[Page Name 1]] — [one-line description]
- [[Page Name 2]] — [one-line description]
- [[Page Name 3]] — [one-line description]

### [Section 2 Name]
*[Brief description of what this section covers]*

- [[Page Name 4]] — [one-line description]
- [[Page Name 5]] — [one-line description]

### [Section 3 Name]
*[Brief description of what this section covers]*

- [[Page Name 6]] — [one-line description]
- [[Page Name 7]] — [one-line description]

---

## Special Pages

- [[hot]] — Recent context cache (~500 words, updated each session)
- [[overview]] — Project structure and organization
- [[glossary]] — Domain terminology (optional)

---

## Page Types

This wiki uses several page types:

- **Concept pages**: Explain domain concepts, methods, phenomena
- **Entity pages**: Facts about specific specimens, experiments, platforms
- **Source pages**: Per-document summaries combining extraction + validation
- **Question pages**: Open research questions and gaps
- **Comparison pages**: Cross-platform or cross-method comparisons

---

## Usage Notes

**For the agent:**
1. Read this index.md FIRST every session
2. Identify which pages are relevant to the user's query
3. Read ALL relevant pages (not just one)
4. Cite pages as [[Page Name]] in responses

**For domain scientists:**
- Add new pages to the appropriate section above
- Keep one-line descriptions concise and searchable
- Run `scripts/build_index.py` to regenerate this file automatically (optional)

---

## Statistics

- Total pages: [NUMBER]
- Sections: [NUMBER]
- Last major update: [DATE]
- Coverage areas: [list key topics]
