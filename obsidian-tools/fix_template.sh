#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Get script directory and work relative to it
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(dirname "$SCRIPT_DIR")"

# Check if vault structure exists
if [ ! -d "$VAULT_ROOT/0-inbox" ]; then
    echo "Error: Expected Obsidian vault structure not found"
    echo "Script location: $SCRIPT_DIR"
    echo "Expected vault root: $VAULT_ROOT"
    echo "Looking for: $VAULT_ROOT/0-inbox/"
    echo ""
    echo "Please ensure this script is run from within an Obsidian vault structure:"
    echo "  vault-root/scripts/obsidian-tools/fix_template.sh"
    echo "  vault-root/0-inbox/"
    exit 1
fi

# Navigate to the workspace directory (vault root)
cd "$VAULT_ROOT" || exit 1

# Correct template content (exactly matching the original inbox-template.md)
TEMPLATE=$(cat <<'EOF'
---
date-created: <% tp.file.creation_date("YYYY-MM-DD") %>
date-updated: <% tp.date.now("YYYY-MM-DD") %>
status: []
category:
tags:
author:
linked-notes:
source: ""
priority:
---
<%*
try {
    const folder = tp.file.folder(true);
    const dateTime = tp.file.creation_date("YYYY-MM-DD-HHmm");
    const currentName = tp.file.title;
    const nameWithoutDate = currentName.replace(/^\d{4}-\d{2}-\d{2}-\d{4}-?/, "");
    const newName = `${dateTime}-${nameWithoutDate}`;
    await tp.file.rename(newName);
} catch (error) {
    console.error("Templater: File rename failed!", error);
    tR += "\\n\\n**Templater Error:** File rename failed. Check console (Ctrl+Shift+I)\\n\\n";
}
-%>
`= this.file.name`

EOF
)

# Process each markdown file in the 0-inbox directory
echo "Starting to fix template in files in 0-inbox..."
for file in 0-inbox/*.md; do
  # Skip hidden files and system files
  if [[ "$(basename "$file")" == ".*" || "$(basename "$file")" == ".DS_Store" ]]; then
    continue
  fi
  
  echo "Processing $file..."
  
  # Create a temporary file
  temp_file=$(mktemp)
  
  # Get the file content after the YAML front matter and template code
  content=$(sed -n '/`= this.file.name`/,$ p' "$file" | tail -n +2)
  
  # Add template to the beginning of the file
  echo "$TEMPLATE" > "$temp_file"
  
  # Append the existing content if there is any (without leading empty lines)
  if [ -n "$content" ]; then
    echo "$content" >> "$temp_file"
  fi
  
  # Replace the original file with the new content
  cp "$temp_file" "$file"
  
  # Clean up
  rm "$temp_file"
done

echo "Template has been fixed in all files in 0-inbox." 