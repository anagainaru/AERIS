#!/usr/bin/env bash
# Immutability Guard Hook
# Prevents accidental writes to protected read-only directories
#
# CUSTOMIZE THIS: Add your read-only directories to the PROTECTED_DIRS array

set -euo pipefail

# Configuration: Add directories that should be read-only
# Example: PROTECTED_DIRS=("raw" "data/ground_truth" "papers")
PROTECTED_DIRS=("[PROTECTED_DIR_1]" "[PROTECTED_DIR_2]")

# Get the file path from stdin (Claude Code hook protocol)
read -r file_path

# Check if file_path is inside any protected directory
for protected in "${PROTECTED_DIRS[@]}"; do
    # Resolve to absolute path if relative
    if [[ "$file_path" == "$protected"/* ]] || [[ "$file_path" == "./$protected"/* ]]; then
        echo "❌ IMMUTABILITY VIOLATION"
        echo ""
        echo "Cannot write to protected directory: $protected/"
        echo "File: $file_path"
        echo ""
        echo "This directory is READ-ONLY to preserve source integrity."
        echo ""
        echo "If you need to modify this file:"
        echo "1. Check if it should really be in a read-only directory"
        echo "2. Update .claude/hooks/immutability-guard.sh if the policy changed"
        echo "3. Consider copying to a writable location instead"
        exit 2  # Exit code 2 blocks the tool use
    fi
done

# If we get here, the write is allowed
exit 0
