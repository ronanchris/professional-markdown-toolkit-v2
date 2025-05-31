#!/usr/bin/env python3
import os
import re
import shutil
import sys
from pathlib import Path

def remove_metadata(file_path, dry_run=True, force=False):
    """
    Safely remove YAML frontmatter and Templater code blocks from a markdown file.
    
    Args:
        file_path: Path to the markdown file
        dry_run: If True, don't modify the file, just print what would be done
        force: If True, remove metadata even if the file is mostly metadata
        
    Returns:
        tuple: (success, message)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Make a backup before modifying
        if not dry_run:
            backup_path = f"{file_path}.bak"
            shutil.copy2(file_path, backup_path)
            
        # Check if file has YAML frontmatter (starts with ---)
        if content.startswith('---'):
            # Find the end of the frontmatter (second ---)
            parts = content.split('---', 2)
            if len(parts) >= 3:
                # The content is after the second ---
                content_without_frontmatter = parts[2].lstrip()
            else:
                # Only one --- found, no proper frontmatter
                content_without_frontmatter = content
        else:
            # No frontmatter
            content_without_frontmatter = content
            
        # Remove Templater code blocks <%* ... -%>
        content_without_templater = re.sub(r'<%\*[\s\S]*?-%>', '', content_without_frontmatter)
        
        # Remove the line with `= this.file.name`
        content_without_filename = re.sub(r'`= this\.file\.name`\s*\n?', '', content_without_templater)
        
        # Check if there's any content after removing metadata
        content_without_metadata = content_without_filename.strip()
        
        # If the file is mostly metadata and we're not forcing removal
        if not force and len(content) > 0 and len(content_without_metadata) < len(content) * 0.2:
            # Check if there's any actual content at all
            if len(content_without_metadata) == 0:
                return True, f"File {file_path} has no content beyond metadata - skipping"
            else:
                return False, f"Warning: File {file_path} would lose most of its content (only {len(content_without_metadata)} bytes would remain)"
            
        if dry_run:
            print(f"Would modify {file_path}")
            print(f"Original size: {len(content)} bytes")
            print(f"New size: {len(content_without_metadata)} bytes")
            if len(content_without_metadata) == 0:
                print(f"Note: File would be empty after removing metadata")
            return True, "Dry run completed successfully"
        else:
            # Only write if there's content to preserve
            if len(content_without_metadata) > 0:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content_without_metadata)
                return True, f"Successfully removed metadata from {file_path}"
            else:
                # For empty files, create with a placeholder
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("")
                return True, f"File {file_path} is now empty (had no content beyond metadata)"
            
    except Exception as e:
        return False, f"Error processing {file_path}: {str(e)}"

def process_directory(directory, dry_run=True, force=False):
    """Process all markdown files in the given directory"""
    path = Path(directory)
    md_files = list(path.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {directory}")
        return
        
    print(f"Found {len(md_files)} markdown files in {directory}")
    
    success_count = 0
    error_count = 0
    
    for md_file in md_files:
        success, message = remove_metadata(md_file, dry_run, force)
        
        if success:
            success_count += 1
            print(f"Success: {message}")
        else:
            error_count += 1
            print(f"Error: {message}")
    
    print(f"Processed {len(md_files)} files: {success_count} successful, {error_count} with errors")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python safe_metadata_removal.py <directory|file> [--apply] [--force]")
        print("       --apply: Actually modify files (without this flag, runs in dry-run mode)")
        print("       --force: Force metadata removal even for files that are mostly metadata")
        sys.exit(1)
        
    path = sys.argv[1]
    dry_run = True
    force = False
    
    if "--apply" in sys.argv:
        dry_run = False
        
    if "--force" in sys.argv:
        force = True
    
    if dry_run:
        print("Running in DRY RUN mode - no files will be modified")
    else:
        print("Running in APPLY mode - files will be modified")
        
    if force:
        print("Force mode enabled - will remove metadata even if file is mostly metadata")
    
    # Check if the path is a file or directory
    if os.path.isfile(path):
        print(f"Processing single file: {path}")
        success, message = remove_metadata(path, dry_run, force)
        if success:
            print(f"Success: {message}")
        else:
            print(f"Error: {message}")
    elif os.path.isdir(path):
        process_directory(path, dry_run, force)
    else:
        print(f"Error: {path} is not a valid file or directory")
        sys.exit(1) 