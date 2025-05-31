#!/usr/bin/env python3

import re
import sys

def clean_markdown_file(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Keep track of original length
    original_length = len(content)
    print(f"Processing file: {file_path}")
    
    # First, let's look at what kinds of whitespace are present
    triple_newlines = content.count('\n\n\n')
    double_newlines = content.count('\n\n')
    spaces_after_newline = len(re.findall(r'\n[ \t]+\n', content))
    
    print(f"Found {triple_newlines} triple newlines")
    print(f"Found {double_newlines} double newlines")
    print(f"Found {spaces_after_newline} newlines with spaces between them")
    
    # Preserve YAML frontmatter (if present)
    if content.startswith('---'):
        # Find the end of frontmatter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = f"---{parts[1]}---"
            main_content = parts[2]
        else:
            frontmatter = ""
            main_content = content
    else:
        frontmatter = ""
        main_content = content

    # MOST IMPORTANT: Target the specific pattern in this document "  " (two spaces on their own line)
    main_content = re.sub(r'\n[ \t]+\n', '\n\n', main_content)
    
    # Remove the common pattern of 3+ newlines
    main_content = re.sub(r'\n{3,}', '\n\n', main_content)
    
    # Process main content - catch various whitespace patterns
    main_content = re.sub(r'(\n\s*){3,}', '\n\n', main_content)
    
    # Special handling for sections with "  " (two spaces alone)
    main_content = re.sub(r'\n[ ]{2,}\n', '\n\n', main_content)
    
    # Ensure proper spacing around headers
    main_content = re.sub(r'\n{2,}(#{1,6}\s)', '\n\n\\1', main_content)
    main_content = re.sub(r'(#{1,6}[^\n]+)\n{2,}', '\\1\n\n', main_content)
    
    # Clean up table formatting
    main_content = re.sub(r'\n{2,}(\|)', '\n\n|', main_content)
    
    # Combine the processed content
    if frontmatter:
        processed_content = frontmatter + main_content
    else:
        processed_content = main_content
    
    # Write back to the file
    with open(file_path, 'w') as file:
        file.write(processed_content)
    
    # Report statistics
    new_length = len(processed_content)
    chars_removed = original_length - new_length
    
    print(f"File cleaned: {file_path}")
    print(f"Removed {chars_removed} characters of whitespace")
    print(f"Original size: {original_length} characters")
    print(f"New size: {new_length} characters")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cleanup_markdown.py <markdown_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    clean_markdown_file(file_path) 