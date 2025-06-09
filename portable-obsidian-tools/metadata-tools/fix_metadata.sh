#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Get script directory and work relative to it
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
INBOX_DIR="$VAULT_ROOT/0-inbox"

# Source backup functions
source "$SCRIPT_DIR/../shared/backup-functions.sh"

# Parse command line arguments
for arg in "$@"; do
    case $arg in
        --no-backup)
            disable_backups
            shift
            ;;
        --help)
            echo "Usage: $0 [--no-backup] [--help]"
            echo "  --no-backup  Skip backup creation (advanced users only)"
            echo "  --help       Show this help message"
            exit 0
            ;;
    esac
done

# Check if inbox directory exists
if [ ! -d "$INBOX_DIR" ]; then
    echo "Error: Inbox directory not found at $INBOX_DIR"
    echo "Please ensure this script is run from within an Obsidian vault structure"
    echo "Expected structure: vault-root/scripts/metadata-tools/"
    echo "Looking for: vault-root/0-inbox/"
    exit 1
fi

# Initialize backup system
init_backup_system "$SCRIPT_DIR"

# Navigate to the 0-inbox directory
cd "$INBOX_DIR" || exit 1

echo "🚀 Starting metadata fix process in 0-inbox..."
echo "📁 Working directory: $INBOX_DIR"

# Create backup of all markdown files before processing
if [ "$BACKUP_ENABLED" = true ]; then
    echo "💾 Creating backup of all markdown files..."
    create_directory_backup "$INBOX_DIR" "*.md" "metadata_fix"
fi

for file in *.md; do
  if [ -f "$file" ]; then
    echo "Processing $file..."
    
    # Create a temporary file
    temp_file=$(mktemp)
    
    # Check if file starts with YAML frontmatter and remove it
    if grep -q "^---" "$file"; then
      # Find line number of second "---" marker
      second_marker=$(grep -n "^---" "$file" | sed -n '2p' | cut -d: -f1)
      
      if [ -n "$second_marker" ]; then
        # Extract everything after the second marker
        tail -n +$((second_marker + 1)) "$file" > "$temp_file"
      else
        # No second marker found, just copy the file
        cp "$file" "$temp_file"
      fi
    else
      # No frontmatter, just copy the file
      cp "$file" "$temp_file"
    fi
    
    # Remove templater code blocks
    sed -i.bak -e '/<%\*/,/-%>/d' "$temp_file"
    
    # Remove the "`= this.file.name`" line
    sed -i.bak -e '/`= this\.file\.name`/d' "$temp_file"
    
    # Clean up empty lines at the beginning and end
    sed -i.bak -e '/./,$!d' -e ':a;/^\n*$/{$d;N;ba;}' "$temp_file"
    
    # Copy cleaned file back to original
    cp "$temp_file" "$file"
    
    # Remove temporary files
    rm "$temp_file"
    rm -f "$temp_file.bak"
  fi
done

echo ""
echo "🎉 Processing complete! All metadata fixed in files in 0-inbox."
echo ""
get_backup_info
echo ""
echo "💡 To restore files if needed:"
echo "   $SCRIPT_DIR/../shared/backup-functions.sh restore_from_backup '$SCRIPT_DIR'" 