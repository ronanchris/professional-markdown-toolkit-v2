#!/bin/bash

# Script to clean all markdown files in the entire vault
# Usage: ./clean_all_markdown.sh [--dry-run]

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Get the parent directory (vault root)
VAULT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

# Default flags
DRY_RUN=false
VERBOSE=false

# Parse arguments
for arg in "$@"; do
  case $arg in
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --verbose)
      VERBOSE=true
      shift
      ;;
  esac
done

# Build command arguments array
CMD_ARGS=("$SCRIPT_DIR/cleanup_markdown_batch.py" "$VAULT_ROOT" "--recursive")

if [ "$DRY_RUN" = true ]; then
  CMD_ARGS+=("--dry-run")
fi

if [ "$VERBOSE" = true ]; then
  CMD_ARGS+=("--verbose")
fi

# Print header
echo "============================================="
echo "  Markdown Cleanup for Obsidian Vault"
echo "============================================="
echo "Vault location: $VAULT_ROOT"
echo "Mode: $([ "$DRY_RUN" = true ] && echo "Dry run (no changes)" || echo "Live cleanup")"
echo "Verbose: $([ "$VERBOSE" = true ] && echo "Yes" || echo "No")"
echo "============================================="
echo "Starting cleanup process..."
echo

# Execute command safely (no eval)
python "${CMD_ARGS[@]}"

echo
echo "============================================="
echo "          Cleanup process complete!"
echo "=============================================" 