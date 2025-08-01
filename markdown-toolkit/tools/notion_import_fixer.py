#!/usr/bin/env python3
"""
Notion Import Fixer - Addresses specific Notion markdown import issues
Fixes WikiLinks, excessive horizontal rules, and other Notion-specific problems.
"""

import os
import sys
import re
import argparse

def fix_wikilinks(text):
    """
    Convert Obsidian WikiLinks to regular markdown links or plain text.
    [[link-name]] -> link-name or [link-name](#)
    """
    def replace_wikilink(match):
        link_content = match.group(1)
        # Convert to plain text with emphasis
        return f"**{link_content.replace('-', ' ').title()}**"
    
    # Pattern to match [[wikilink]] format
    wikilink_pattern = r'\[\[([^\]]+)\]\]'
    
    fixed_text = re.sub(wikilink_pattern, replace_wikilink, text)
    
    return fixed_text

def reduce_horizontal_rules(text):
    """
    Reduce excessive horizontal rules that can break Notion import.
    Keep important section breaks but remove excessive ones.
    """
    lines = text.split('\n')
    fixed_lines = []
    previous_was_hr = False
    hr_count = 0
    
    for line in lines:
        line_stripped = line.strip()
        
        # Check if this line is a horizontal rule
        if line_stripped == '---' or line_stripped == '***' or line_stripped == '___':
            hr_count += 1
            
            # Only keep horizontal rules if:
            # 1. Previous line wasn't already a horizontal rule
            # 2. We haven't exceeded a reasonable limit in this section
            if not previous_was_hr and hr_count <= 30:  # Limit to 30 total
                fixed_lines.append('')  # Replace with empty line for spacing
                previous_was_hr = True
            # Otherwise skip this horizontal rule
        else:
            fixed_lines.append(line)
            previous_was_hr = False
    
    return '\n'.join(fixed_lines)

def fix_complex_tables(text):
    """
    Simplify complex tables that might break Notion import.
    """
    lines = text.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Check for complex table alignment syntax
        if re.match(r'^\|[-:\s|]+\|$', line.strip()):
            # Simplify table alignment to basic format
            cell_count = line.count('|') - 1
            simplified_line = '|' + '---|' * cell_count
            fixed_lines.append(simplified_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_nested_formatting(text):
    """
    Fix nested bold/italic formatting that can break Notion.
    """
    # Fix nested bold within bold
    text = re.sub(r'\*\*([^*]*)\*\*([^*]*)\*\*([^*]*)\*\*', r'**\1\2\3**', text)
    
    # Fix mixed formatting
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'***\1***', text)
    
    return text

def split_large_document(text, max_lines=1500):
    """
    Split very large documents into smaller chunks for Notion.
    """
    lines = text.split('\n')
    
    if len(lines) <= max_lines:
        return [text]  # No splitting needed
    
    chunks = []
    current_chunk = []
    current_lines = 0
    
    for line in lines:
        # Check if we should start a new chunk
        if (current_lines >= max_lines and 
            (line.startswith('#') or line.strip() == '' or line.startswith('---'))):
            
            # Save current chunk
            if current_chunk:
                chunks.append('\n'.join(current_chunk))
                current_chunk = []
                current_lines = 0
        
        current_chunk.append(line)
        current_lines += 1
    
    # Add the last chunk
    if current_chunk:
        chunks.append('\n'.join(current_chunk))
    
    return chunks

def fix_notion_import_issues(text, fix_wikilinks_enabled=True, reduce_hrs=True, 
                           fix_tables=True, fix_formatting=True, split_docs=False):
    """
    Apply all Notion import fixes to the text.
    """
    fixed_text = text
    
    if fix_wikilinks_enabled:
        fixed_text = fix_wikilinks(fixed_text)
    
    if reduce_hrs:
        fixed_text = reduce_horizontal_rules(fixed_text)
    
    if fix_tables:
        fixed_text = fix_complex_tables(fixed_text)
    
    if fix_formatting:
        fixed_text = fix_nested_formatting(fixed_text)
    
    if split_docs:
        return split_large_document(fixed_text)
    
    return [fixed_text]

def process_file(input_path, output_path=None, **options):
    """
    Process a markdown file to fix Notion import issues.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply fixes
        fixed_chunks = fix_notion_import_issues(content, **options)
        
        # Determine output path(s)
        if output_path is None:
            base_path = input_path.replace('.md', '')
            if len(fixed_chunks) == 1:
                output_path = f"{base_path}-notion-ready.md"
            else:
                output_paths = [f"{base_path}-part{i+1}-notion-ready.md" 
                              for i in range(len(fixed_chunks))]
        else:
            if len(fixed_chunks) == 1:
                output_paths = [output_path]
            else:
                base_path = output_path.replace('.md', '')
                output_paths = [f"{base_path}-part{i+1}.md" 
                              for i in range(len(fixed_chunks))]
        
        # Write output files
        created_files = []
        for i, chunk in enumerate(fixed_chunks):
            current_output = output_paths[i] if len(fixed_chunks) > 1 else output_paths[0]
            
            with open(current_output, 'w', encoding='utf-8') as f:
                f.write(chunk)
            
            created_files.append(current_output)
        
        return True, created_files, len(fixed_chunks)
        
    except Exception as e:
        return False, [], str(e)

def analyze_notion_issues(file_path):
    """
    Analyze a file for Notion import issues.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = {}
        
        # Count WikiLinks
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        issues['wikilinks'] = len(wikilinks)
        
        # Count horizontal rules
        hr_count = content.count('\n---\n') + content.count('\n***\n') + content.count('\n___\n')
        issues['horizontal_rules'] = hr_count
        
        # Count lines
        lines = content.split('\n')
        issues['total_lines'] = len(lines)
        
        # Check for complex tables
        complex_tables = len([line for line in lines if re.match(r'^\|[-:\s|]+\|$', line.strip())])
        issues['complex_tables'] = complex_tables
        
        # Check for nested formatting
        nested_bold = len(re.findall(r'\*\*[^*]*\*\*[^*]*\*\*', content))
        issues['nested_formatting'] = nested_bold
        
        return issues
        
    except Exception as e:
        return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description='Fix Notion markdown import issues')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('--no-wikilinks', action='store_false', dest='fix_wikilinks',
                       help='Skip WikiLink fixing')
    parser.add_argument('--no-hr-reduction', action='store_false', dest='reduce_hrs',
                       help='Skip horizontal rule reduction')
    parser.add_argument('--no-table-fix', action='store_false', dest='fix_tables',
                       help='Skip table simplification')
    parser.add_argument('--no-format-fix', action='store_false', dest='fix_formatting',
                       help='Skip formatting fixes')
    parser.add_argument('--split', action='store_true', dest='split_docs',
                       help='Split large documents into chunks')
    parser.add_argument('--analyze', action='store_true',
                       help='Only analyze issues, don\'t fix')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    
    if args.analyze:
        print(f"Analyzing Notion import issues in: {args.input_file}")
        issues = analyze_notion_issues(args.input_file)
        
        if 'error' in issues:
            print(f"Error: {issues['error']}")
            sys.exit(1)
        
        print(f"\nNotion Import Analysis:")
        print(f"  WikiLinks: {issues['wikilinks']}")
        print(f"  Horizontal Rules: {issues['horizontal_rules']}")
        print(f"  Total Lines: {issues['total_lines']}")
        print(f"  Complex Tables: {issues['complex_tables']}")
        print(f"  Nested Formatting: {issues['nested_formatting']}")
        
        # Recommendations
        print(f"\nRecommendations:")
        if issues['wikilinks'] > 0:
            print(f"  - Fix {issues['wikilinks']} WikiLinks")
        if issues['horizontal_rules'] > 20:
            print(f"  - Reduce {issues['horizontal_rules']} horizontal rules")
        if issues['total_lines'] > 2000:
            print(f"  - Consider splitting {issues['total_lines']} lines into smaller documents")
        if issues['complex_tables'] > 0:
            print(f"  - Simplify {issues['complex_tables']} complex tables")
        
        return
    
    # Process the file
    print(f"Fixing Notion import issues in: {args.input_file}")
    
    success, output_files, chunk_count = process_file(
        args.input_file,
        args.output,
        fix_wikilinks_enabled=args.fix_wikilinks,
        reduce_hrs=args.reduce_hrs,
        fix_tables=args.fix_tables,
        fix_formatting=args.fix_formatting,
        split_docs=args.split_docs
    )
    
    if success:
        print(f"✅ Successfully processed file")
        if chunk_count > 1:
            print(f"📄 Split into {chunk_count} files:")
            for file_path in output_files:
                print(f"   - {os.path.basename(file_path)}")
        else:
            print(f"📄 Output: {os.path.basename(output_files[0])}")
        print(f"💡 Ready for Notion import!")
    else:
        print(f"❌ Error: {output_files}")
        sys.exit(1)

if __name__ == "__main__":
    main() 