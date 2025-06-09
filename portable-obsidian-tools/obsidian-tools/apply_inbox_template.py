#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

def read_template(template_path):
    """Read the template file and extract its content"""
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    return template_content

def apply_template(file_path, template_content, dry_run=True):
    """Apply the template to a file while preserving its content"""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read().strip()
            
        # Make a backup
        if not dry_run:
            backup_path = f"{file_path}.bak"
            shutil.copy2(file_path, backup_path)
        
        # Create new content by combining template and existing content
        new_content = template_content
        if file_content:
            # If the file already has content, add it after the template
            new_content += "\n\n" + file_content
            
        if dry_run:
            print(f"Would modify {file_path}")
            print(f"Original size: {len(file_content)} bytes")
            print(f"New size: {len(new_content)} bytes")
            return True, "Dry run completed successfully"
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"Successfully applied template to {file_path}"
            
    except Exception as e:
        return False, f"Error processing {file_path}: {str(e)}"

def process_directory(directory, template_content, dry_run=True):
    """Apply template to all markdown files in the directory"""
    path = Path(directory)
    md_files = list(path.glob("*.md"))
    
    if not md_files:
        print(f"No markdown files found in {directory}")
        return
        
    print(f"Found {len(md_files)} markdown files in {directory}")
    
    success_count = 0
    error_count = 0
    
    for md_file in md_files:
        success, message = apply_template(md_file, template_content, dry_run)
        
        if success:
            success_count += 1
            print(f"Success: {message}")
        else:
            error_count += 1
            print(f"Error: {message}")
    
    print(f"Processed {len(md_files)} files: {success_count} successful, {error_count} with errors")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python apply_inbox_template.py <template_file> <directory|file> [--apply]")
        print("       --apply: Actually modify files (without this flag, runs in dry-run mode)")
        sys.exit(1)
        
    template_path = sys.argv[1]
    target_path = sys.argv[2]
    dry_run = True
    
    if len(sys.argv) > 3 and sys.argv[3] == "--apply":
        dry_run = False
        
    if not os.path.isfile(template_path):
        print(f"Error: Template file {template_path} not found")
        sys.exit(1)
        
    if dry_run:
        print("Running in DRY RUN mode - no files will be modified")
    else:
        print("Running in APPLY mode - files will be modified")
        
    # Read the template
    template_content = read_template(template_path)
    print(f"Read template file ({len(template_content)} bytes)")
    
    # Process path
    if os.path.isfile(target_path):
        print(f"Processing single file: {target_path}")
        success, message = apply_template(target_path, template_content, dry_run)
        if success:
            print(f"Success: {message}")
        else:
            print(f"Error: {message}")
    elif os.path.isdir(target_path):
        process_directory(target_path, template_content, dry_run)
    else:
        print(f"Error: {target_path} is not a valid file or directory")
        sys.exit(1) 