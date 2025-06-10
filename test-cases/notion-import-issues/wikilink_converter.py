#!/usr/bin/env python3
"""
WikiLink Converter - Convert Obsidian WikiLinks to Notion-friendly format
Transforms [[wiki-link]] to **Wiki Link** for better readability in Notion.
"""

import os
import sys
import re
import argparse

def convert_wikilinks_to_bold(text):
    """
    Convert Obsidian WikiLinks to bold descriptive text.
    [[link-name]] -> **Link Name**
    [[complex-file-name-here]] -> **Complex File Name Here**
    """
    def replace_wikilink(match):
        link_content = match.group(1)
        
        # Clean up the link content:
        # 1. Replace hyphens and underscores with spaces
        cleaned = link_content.replace('-', ' ').replace('_', ' ')
        
        # 2. Title case each word
        words = cleaned.split()
        title_cased = ' '.join(word.capitalize() for word in words)
        
        # 3. Return as bold text
        return f"**{title_cased}**"
    
    # Pattern to match [[wikilink]] format
    wikilink_pattern = r'\[\[([^\]]+)\]\]'
    
    # Replace all WikiLinks
    converted_text = re.sub(wikilink_pattern, replace_wikilink, text)
    
    return converted_text

def analyze_wikilinks(text):
    """
    Analyze WikiLinks in the text and return statistics.
    """
    wikilink_pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(wikilink_pattern, text)
    
    analysis = {
        'total_wikilinks': len(matches),
        'unique_wikilinks': len(set(matches)),
        'wikilinks': matches
    }
    
    return analysis

def process_file(input_path, output_path=None, dry_run=False):
    """
    Process a markdown file to convert WikiLinks.
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Analyze before conversion
        before_analysis = analyze_wikilinks(content)
        
        # Convert WikiLinks
        converted_content = convert_wikilinks_to_bold(content)
        
        # Analyze after conversion
        after_analysis = analyze_wikilinks(converted_content)
        
        # Determine output path
        if output_path is None:
            base_path = input_path.replace('.md', '')
            output_path = f"{base_path}-wikilinks-converted.md"
        
        # Write output (unless dry run)
        if not dry_run:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(converted_content)
        
        return True, output_path, before_analysis, after_analysis
        
    except Exception as e:
        return False, None, None, str(e)

def preview_conversions(file_path, limit=10):
    """
    Preview how WikiLinks will be converted without making changes.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        wikilink_pattern = r'\[\[([^\]]+)\]\]'
        matches = re.findall(wikilink_pattern, content)
        
        if not matches:
            return []
        
        # Show unique conversions
        unique_matches = list(set(matches))[:limit]
        previews = []
        
        for match in unique_matches:
            # Apply the same conversion logic
            cleaned = match.replace('-', ' ').replace('_', ' ')
            words = cleaned.split()
            title_cased = ' '.join(word.capitalize() for word in words)
            
            before = f"[[{match}]]"
            after = f"**{title_cased}**"
            
            previews.append({
                'before': before,
                'after': after,
                'original': match
            })
        
        return previews
        
    except Exception as e:
        return [{'error': str(e)}]

def main():
    parser = argparse.ArgumentParser(description='Convert Obsidian WikiLinks to Notion-friendly bold text')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview changes without making them')
    parser.add_argument('--preview', action='store_true',
                       help='Show conversion preview for WikiLinks')
    parser.add_argument('--analyze', action='store_true',
                       help='Only analyze WikiLinks, don\'t convert')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    
    if args.preview:
        print(f"WikiLink Conversion Preview for: {args.input_file}")
        print("=" * 60)
        
        previews = preview_conversions(args.input_file)
        
        if not previews:
            print("No WikiLinks found in file.")
            return
        
        if 'error' in previews[0]:
            print(f"Error: {previews[0]['error']}")
            sys.exit(1)
        
        for preview in previews:
            print(f"BEFORE: {preview['before']}")
            print(f"AFTER:  {preview['after']}")
            print("-" * 40)
        
        return
    
    if args.analyze:
        print(f"Analyzing WikiLinks in: {args.input_file}")
        
        try:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            analysis = analyze_wikilinks(content)
            
            print(f"\nWikiLink Analysis:")
            print(f"  Total WikiLinks: {analysis['total_wikilinks']}")
            print(f"  Unique WikiLinks: {analysis['unique_wikilinks']}")
            
            if analysis['wikilinks']:
                print(f"\nFound WikiLinks:")
                for link in set(analysis['wikilinks']):
                    print(f"  - [[{link}]]")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        
        return
    
    # Process the file
    print(f"Converting WikiLinks in: {args.input_file}")
    
    success, output_path, before, after = process_file(
        args.input_file,
        args.output,
        dry_run=args.dry_run
    )
    
    if success:
        if args.dry_run:
            print(f"✅ DRY RUN - No files changed")
        else:
            print(f"✅ Successfully converted WikiLinks")
            print(f"📄 Output: {os.path.basename(output_path)}")
        
        print(f"\nConversion Summary:")
        print(f"  WikiLinks before: {before['total_wikilinks']}")
        print(f"  WikiLinks after: {after['total_wikilinks']}")
        print(f"  Converted: {before['total_wikilinks'] - after['total_wikilinks']}")
        
        if not args.dry_run:
            print(f"💡 Ready for Notion import!")
    else:
        print(f"❌ Error: {after}")
        sys.exit(1)

if __name__ == "__main__":
    main() 