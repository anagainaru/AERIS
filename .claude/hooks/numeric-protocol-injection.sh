#!/usr/bin/env bash
# Numeric Value Protocol Injection (UserPromptSubmit Hook)
# Injects mandatory protocol for handling numeric values
# Ensures agent always cites sources, specifies units, and validates values

set -euo pipefail

# Inject protocol into context (printed to stdout becomes part of context)
cat <<'PROTOCOL'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NUMERIC VALUE REPORTING PROTOCOL (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

When reporting ANY numeric value, you MUST:

1. **Explicit Units**
   - ALWAYS specify units: "10.5 g/cm³" not "10.5"
   - Use standard notation (SI preferred)
   - Clarify ambiguous units (e.g., "at%" vs "wt%")

2. **Source Citation**
   - Cite original source: [n] (numeric citation)
   - Include secondary source: ([[Wiki-Page]])
   - Format: [VALUE] [UNIT] [n] ([[Page]])
   - Example: "Density is 10.5 g/cm³ [1] ([[PyC-Properties]])"

3. **Source Location**
   - Table: "Table 3, row 5"
   - Figure: "Figure 7(b)"
   - Page: "p. 42, paragraph 3"
   - Line range: "L145-147"

4. **Cross-Validation**
   - Check against ground truth/known values
   - Flag mismatches: "GT: X, Source: Y, Diff: Z%"
   - Investigate discrepancies before reporting
   - NEVER silently overwrite ground truth

5. **Unit Conversions** (CUSTOMIZE for your domain)
   - Document conversion formula
   - Show both values: "X [unit1] = Y [unit2]"
   - Example conversions for your domain:
     * [UNIT_A] → [UNIT_B]: multiply by [CONVERSION_FACTOR]
     * [UNIT_C] → [UNIT_D]: [CONVERSION_FORMULA]

6. **Uncertainty/Ranges**
   - Report if available: "10.5 ± 0.2 g/cm³"
   - Use ranges when appropriate: "10-12 GPa"
   - Note measurement method if relevant

7. **Context Requirements**
   - State conditions: "at 1200°C", "after 5% burnup"
   - Note methodology: "measured by EPMA", "calculated by BISON"
   - Specify which specimen/sample if multiple exist

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DOMAIN-SPECIFIC CONVERSION RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CUSTOMIZE THESE for your domain:

Temperature:
  • Celsius to Kelvin: T(K) = T(°C) + 273.15
  • [ADD YOUR CONVERSIONS]

Composition:
  • [UNIT_TYPE_1] to [UNIT_TYPE_2]: [FORMULA]
  • [ADD YOUR CONVERSIONS]

Energy:
  • [UNIT_A] to [UNIT_B]: [FORMULA]
  • [ADD YOUR CONVERSIONS]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOL

exit 0
