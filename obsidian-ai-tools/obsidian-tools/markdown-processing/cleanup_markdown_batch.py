#!/usr/bin/env python3

import re
import sys
import os
import argparse
from datetime import datetime

def clean_markdown_file(file_path, dry_run=False, verbose=False):
    """Clean a single markdown file by removing excessive whitespace and normalizing formatting."""
    try:
        # Skip non-markdown files
        if not file_path.lower().endswith(('.md', '.markdown')):
            if verbose:
                print(f"Skipping non-markdown file: {file_path}")
            return None
        
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Keep track of original length
        original_length = len(content)
        
        if verbose:
            print(f"Processing file: {file_path}")
            # Diagnostic information
            triple_newlines = content.count('\n\n\n')
            double_newlines = content.count('\n\n')
            spaces_after_newline = len(re.findall(r'\n[ \t]+\n', content))
            print(f"  Found {triple_newlines} triple newlines")
            print(f"  Found {double_newlines} double newlines")
            print(f"  Found {spaces_after_newline} newlines with spaces between them")
        
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

        # COMPREHENSIVE BULLET POINT HANDLING:
        
        # 1. Convert the document to lines for easier processing
        lines = main_content.split('\n')
        processed_lines = []
        
        # 2. Define regex patterns for bullet points/list items
        bullet_pattern = re.compile(r'^\s*- .+')
        numbered_list_pattern = re.compile(r'^\s*\d+\.\s+.+')
        
        # 3. Process the lines, removing blank lines between list items
        i = 0
        while i < len(lines):
            current_line = lines[i]
            processed_lines.append(current_line)
            
            # If current line is a bullet point/list item
            if bullet_pattern.match(current_line) or numbered_list_pattern.match(current_line):
                # Look ahead to the next non-empty line
                j = i + 1
                while j < len(lines) and (not lines[j].strip()):
                    j += 1
                    
                # If the next non-empty line is also a bullet point/list item, skip any blank lines
                if j < len(lines) and (bullet_pattern.match(lines[j]) or numbered_list_pattern.match(lines[j])):
                    i = j - 1  # Will be incremented to j in the next loop iteration
                
            i += 1
        
        # Reassemble the document
        main_content = '\n'.join(processed_lines)
        
        # FALLBACK: Use regex substitution for any patterns we might have missed
        # Handle individual bullet points with blank lines between them
        main_content = re.sub(r'(^|\n)- ([^\n]+)(\n\s*)+\n- ', r'\1- \2\n- ', main_content)
        
        # Also handle numbered lists the same way
        main_content = re.sub(r'(^|\n)(\d+)\.\s+([^\n]+)(\n\s*)+\n(\d+)\.\s+', r'\1\2. \3\n\5. ', main_content)
        
        # Handle indented bullets (nested lists)
        main_content = re.sub(r'(^|\n)(\s+)- ([^\n]+)(\n\s*)+\n\2- ', r'\1\2- \3\n\2- ', main_content)
        
        # GENERAL WHITESPACE CLEANUP:
        
        # Target lines with only whitespace 
        main_content = re.sub(r'\n[ \t]+\n', '\n\n', main_content)
        
        # Remove 3+ consecutive newlines
        main_content = re.sub(r'\n{3,}', '\n\n', main_content)
        
        # Catch other whitespace patterns
        main_content = re.sub(r'(\n\s*){3,}', '\n\n', main_content)
        
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
        
        # Calculate changes
        new_length = len(processed_content)
        chars_removed = original_length - new_length
        
        # Only write to the file if changes were made and this is not a dry run
        if chars_removed > 0 and not dry_run:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(processed_content)
        
        # Return stats for reporting
        return {
            'file_path': file_path,
            'chars_removed': chars_removed,
            'original_size': original_length,
            'new_size': new_length,
            'processed': not dry_run and chars_removed > 0
        }
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None

def process_directory(directory_path, recursive=False, dry_run=False, verbose=False):
    """Process all markdown files in a directory, optionally including subdirectories."""
    start_time = datetime.now()
    total_files = 0
    processed_files = 0
    total_chars_removed = 0
    file_stats = []
    
    for root, dirs, files in os.walk(directory_path):
        if not recursive and root != directory_path:
            continue
            
        for file in files:
            if file.lower().endswith(('.md', '.markdown')):
                total_files += 1
                file_path = os.path.join(root, file)
                
                result = clean_markdown_file(file_path, dry_run, verbose)
                if result:
                    file_stats.append(result)
                    if result['chars_removed'] > 0:
                        processed_files += 1
                        total_chars_removed += result['chars_removed']
                        if not verbose:  # If not in verbose mode, print simple progress
                            action = "Would clean" if dry_run else "Cleaned"
                            print(f"{action}: {file_path} ({result['chars_removed']} chars removed)")
    
    # Print summary
    elapsed_time = (datetime.now() - start_time).total_seconds()
    print("\nSummary:")
    print(f"Processed {total_files} markdown files in {elapsed_time:.2f} seconds")
    print(f"Modified {processed_files} files" + (" (dry run)" if dry_run else ""))
    print(f"Removed {total_chars_removed} characters of whitespace" + (" (would remove)" if dry_run else ""))
    
    return {
        'total_files': total_files,
        'processed_files': processed_files,
        'total_chars_removed': total_chars_removed,
        'elapsed_time': elapsed_time,
        'file_stats': file_stats
    }

def main():
    parser = argparse.ArgumentParser(description='Clean up markdown files by removing excessive whitespace and normalizing formatting.')
    parser.add_argument('path', help='File or directory to process')
    parser.add_argument('-r', '--recursive', action='store_true', help='Process subdirectories recursively')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed information about processing')
    
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        result = clean_markdown_file(args.path, args.dry_run, args.verbose)
        if result:
            action = "Would clean" if args.dry_run else "Cleaned"
            print(f"{action}: {result['file_path']}")
            print(f"Removed {result['chars_removed']} characters of whitespace" + (" (would remove)" if args.dry_run else ""))
            print(f"Original size: {result['original_size']} characters")
            print(f"New size: {result['new_size']} characters")
    elif os.path.isdir(args.path):
        process_directory(args.path, args.recursive, args.dry_run, args.verbose)
    else:
        print(f"Error: {args.path} is not a valid file or directory")
        sys.exit(1)

if __name__ == "__main__":
    main() 