#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Get script directory and work relative to it
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(dirname "$SCRIPT_DIR")"
INBOX_DIR="$VAULT_ROOT/0-inbox"

# Source backup functions
source "$SCRIPT_DIR/../shared/backup-functions.sh"

# Parse command line arguments
BACKUP_ENABLED=true
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

echo "🚀 Starting metadata removal process in 0-inbox..."
echo "📁 Working directory: $INBOX_DIR"

# Create backup of all markdown files before processing
if [ "$BACKUP_ENABLED" = true ]; then
    echo "💾 Creating backup of all markdown files..."
    create_directory_backup "$INBOX_DIR" "*.md" "metadata_removal"
fi

for file in *.md; do
  if [ -f "$file" ]; then
    echo "Processing $file..."
    
    # Create a temporary file
    temp_file=$(mktemp)
    
    # Read the file content
    content=$(cat "$file")
    
    # Check if the file begins with YAML frontmatter
    if [[ "$content" =~ ^---.*---$ ]]; then
      # Extract everything after the second '---' marker (end of YAML frontmatter)
      content=$(echo "$content" | awk 'BEGIN{flag=0; count=0} /^---$/{count++; if(count==2){flag=1; next}} flag{print}')
    fi
    
    # Remove templater code blocks
    content=$(echo "$content" | sed -E '/<%\*/,/-%>/d')
    
    # Remove the "`= this.file.name`" line if present
    content=$(echo "$content" | sed -E '/`= this\.file\.name`/d')
    
    # Trim leading and trailing whitespace
    content=$(echo "$content" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    
    # Write the cleaned content to temporary file
    echo "$content" > "$temp_file"
    
    # Copy temporary file back to original
    cp "$temp_file" "$file"
    
    # Remove temporary file
    rm "$temp_file"
  fi
done

echo ""
echo "🎉 Processing complete! All metadata removed from files in 0-inbox."
echo ""
get_backup_info
echo ""
echo "💡 To restore files if needed:"
echo "   $SCRIPT_DIR/../shared/backup-functions.sh restore_from_backup '$SCRIPT_DIR'" 