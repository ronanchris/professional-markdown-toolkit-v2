#!/usr/bin/env python3
"""
Complete Notion Import Fixer - All-in-one solution for Notion markdown import issues
Combines Unicode cleaning, horizontal rule removal, and WikiLink conversion.
"""

import os
import sys
import re
import argparse

# Unicode character mappings for safe replacements
UNICODE_REPLACEMENTS = {
    # Em and En dashes
    '\u2014': '--',  # Em dash
    '\u2013': '-',   # En dash
    
    # Smart quotes
    '\u2018': "'",   # Left single quotation mark
    '\u2019': "'",   # Right single quotation mark  
    '\u201C': '"',   # Left double quotation mark
    '\u201D': '"',   # Right double quotation mark
    
    # Mathematical symbols
    '\u00D7': 'x',   # Multiplication sign
    '\u2265': '>=',  # Greater than or equal to
    '\u2192': '->',  # Rightwards arrow
    '\u2190': '<-',  # Leftwards arrow
    
    # Special punctuation
    '\u2026': '...',  # Horizontal ellipsis
    '\u2020': '*',    # Dagger
    '\u2021': '**',   # Double dagger
    '\u2042': '***',  # Asterism
    
    # Status indicators - preserve visual meaning with safe alternatives
    '\u2705': '✓',    # White heavy check mark -> safe check
    '\u2713': '✓',    # Check mark -> safe check  
    '\u2714': '✓',    # Heavy check mark -> safe check
    '\u274C': '✗',    # Cross mark -> safe X
    '\u2716': '✗',    # Heavy multiplication X -> safe X
    '\u2717': '✗',    # Ballot X -> safe X
    '\u26A0': '⚠',    # Warning sign -> keep (works in most contexts)
    '\u26A1': '!',    # High voltage -> exclamation
    '\u2611': '[✓]',  # Ballot box with check -> bracketed check
    '\u2612': '[✗]',  # Ballot box with X -> bracketed X
    
    # Common emoji replacements for status/indicators
    '✅': '✓',        # White heavy check mark
    '❌': '✗',        # Cross mark
    '⚠️': '⚠',        # Warning sign
    '🟢': '[GREEN]',  # Green circle
    '🟡': '[YELLOW]', # Yellow circle  
    '🔴': '[RED]',    # Red circle
    '🔵': '[BLUE]',   # Blue circle
    '⭐': '[STAR]',   # Star
    '📊': '[BAR_CHART]', # Bar chart
    '📈': '[CHART_UP]',  # Chart with upwards trend
    '📉': '[CHART_DOWN]', # Chart with downwards trend
    '💰': '[MONEY]',     # Money bag
    '🎯': '[TARGET]',    # Direct hit
    '🏆': '[TROPHY]',    # Trophy
    '🚨': '[ALERT]',     # Police car light
    '🔧': '[TOOL]',      # Wrench
    '⚡': '[LIGHTNING]', # High voltage
    '🔥': '[FIRE]',      # Fire
    '💡': '[IDEA]',      # Electric light bulb
    '📱': '[MOBILE]',    # Mobile phone
    '💻': '[LAPTOP]',    # Laptop computer
    '🌐': '[WEB]',       # Globe with meridians
    '🔒': '[LOCK]',      # Lock
    '🔓': '[UNLOCK]',    # Open lock
    '✨': '[SPARKLES]',  # Sparkles
    '🎉': '[PARTY]',     # Party popper
    '👍': '[THUMBS_UP]', # Thumbs up sign
    '👎': '[THUMBS_DOWN]', # Thumbs down sign
    '❤️': '[HEART]',     # Heavy black heart
    '💙': '[BLUE_HEART]', # Blue heart
    '💚': '[GREEN_HEART]', # Green heart
}

# Emoji ranges to detect and remove entirely
EMOJI_RANGES = [
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
    (0x1F680, 0x1F6FF),  # Transport and Map Symbols
    (0x1F1E0, 0x1F1FF),  # Regional indicator symbols (flags)
    (0x2600, 0x26FF),    # Miscellaneous Symbols
    (0x2700, 0x27BF),    # Dingbats
    (0xFE00, 0xFE0F),    # Variation Selectors
    (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
]

def is_emoji(char):
    """Check if a character is an emoji."""
    code_point = ord(char)
    return any(start <= code_point <= end for start, end in EMOJI_RANGES)

def clean_unicode_text(text, strip_emojis=True, replace_chars=True):
    """Clean Unicode characters from text that commonly cause Notion import issues."""
    cleaned = text
    
    # Replace problematic characters with safe equivalents first
    if replace_chars:
        for unicode_char, replacement in UNICODE_REPLACEMENTS.items():
            cleaned = cleaned.replace(unicode_char, replacement)
    
    # Strip remaining emojis entirely (they're the biggest Notion import problem)
    if strip_emojis:
        cleaned = ''.join(char for char in cleaned if not is_emoji(char))
    
    return cleaned

def reduce_horizontal_rules(text):
    """Remove excessive horizontal rules that can break Notion import."""
    lines = text.split('\n')
    fixed_lines = []
    
    for line in lines:
        line_stripped = line.strip()
        
        # Check if this line is a horizontal rule
        if line_stripped in ['---', '***', '___']:
            # Replace with empty line for spacing
            fixed_lines.append('')
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def convert_wikilinks_to_bold(text):
    """Convert Obsidian WikiLinks to bold descriptive text."""
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

def fix_complex_tables(text):
    """Simplify complex tables that might break Notion import."""
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
    """Fix nested bold/italic formatting that can break Notion."""
    # First, fix bold headers that have inconsistent asterisks
    # Remove any stray asterisks from headers and clean them up
    
    # Pattern 1: # **Text** (keep as is - properly formatted)
    # Pattern 2: # Section Text** (remove trailing asterisks)
    text = re.sub(r'^(#{1,6}\s+)([^*\n]*[^*\s])\*\*\s*$', r'\1\2', text, flags=re.MULTILINE)
    
    # Pattern 3: # **Section Text (remove leading asterisks if no trailing)
    text = re.sub(r'^(#{1,6}\s+)\*\*([^*\n]*[^*\s])\s*$', r'\1\2', text, flags=re.MULTILINE)
    
    # Pattern 4: Clean up any remaining header formatting issues
    # Remove any lone asterisks at the end of headers
    text = re.sub(r'^(#{1,6}\s+[^*\n]*)\*+\s*$', r'\1', text, flags=re.MULTILINE)
    
    # Fix nested bold within bold (but avoid headers)
    # Split into lines and process each line to avoid headers
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if not line.strip().startswith('#'):  # Only process non-header lines
            lines[i] = re.sub(r'\*\*([^*]*)\*\*([^*]*)\*\*([^*]*)\*\*', r'**\1\2\3**', line)
    text = '\n'.join(lines)
    
    # Fix mixed formatting
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'***\1***', text)
    
    return text

def analyze_issues(text):
    """Analyze all potential Notion import issues in the text."""
    issues = {}
    
    # Count Unicode issues
    unicode_chars = [c for c in text if ord(c) > 127]
    replaceable_unicode = [c for c in unicode_chars if c in UNICODE_REPLACEMENTS]
    emoji_chars = [c for c in unicode_chars if is_emoji(c) and c not in UNICODE_REPLACEMENTS]
    other_unicode = [c for c in unicode_chars if not is_emoji(c) and c not in UNICODE_REPLACEMENTS]
    
    issues['unicode_total'] = len(unicode_chars)
    issues['unicode_replaceable'] = len(replaceable_unicode)
    issues['unicode_emojis'] = len(emoji_chars)
    issues['unicode_other'] = len(other_unicode)
    
    # Count WikiLinks
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', text)
    issues['wikilinks'] = len(wikilinks)
    
    # Count horizontal rules
    hr_count = text.count('\n---\n') + text.count('\n***\n') + text.count('\n___\n')
    issues['horizontal_rules'] = hr_count
    
    # Count lines
    lines = text.split('\n')
    issues['total_lines'] = len(lines)
    
    # Check for complex tables
    complex_tables = len([line for line in lines if re.match(r'^\|[-:\s|]+\|$', line.strip())])
    issues['complex_tables'] = complex_tables
    
    # Check for nested formatting
    nested_bold = len(re.findall(r'\*\*[^*]*\*\*[^*]*\*\*', text))
    issues['nested_formatting'] = nested_bold
    
    return issues

def complete_notion_fix(text, fix_unicode=True, fix_hrs=True, fix_wikilinks=True, 
                       fix_tables=True, fix_formatting=True):
    """Apply all Notion import fixes to the text."""
    fixed_text = text
    
    if fix_unicode:
        fixed_text = clean_unicode_text(fixed_text)
    
    if fix_hrs:
        fixed_text = reduce_horizontal_rules(fixed_text)
    
    if fix_wikilinks:
        fixed_text = convert_wikilinks_to_bold(fixed_text)
    
    if fix_tables:
        fixed_text = fix_complex_tables(fixed_text)
    
    if fix_formatting:
        fixed_text = fix_nested_formatting(fixed_text)
    
    return fixed_text

def process_file(input_path, output_path=None, **options):
    """Process a markdown file to fix all Notion import issues."""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Analyze before fixes
        before_analysis = analyze_issues(content)
        
        # Apply all fixes
        fixed_content = complete_notion_fix(content, **options)
        
        # Analyze after fixes
        after_analysis = analyze_issues(fixed_content)
        
        # Determine output path
        if output_path is None:
            base_path = input_path.replace('.md', '')
            output_path = f"{base_path}-notion-ready.md"
        
        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        return True, output_path, before_analysis, after_analysis
        
    except Exception as e:
        return False, None, None, str(e)

def main():
    parser = argparse.ArgumentParser(description='Complete Notion markdown import fixer')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('--no-unicode', action='store_false', dest='fix_unicode',
                       help='Skip Unicode character fixing')
    parser.add_argument('--no-hr-removal', action='store_false', dest='fix_hrs',
                       help='Skip horizontal rule removal')
    parser.add_argument('--no-wikilinks', action='store_false', dest='fix_wikilinks',
                       help='Skip WikiLink conversion')
    parser.add_argument('--no-table-fix', action='store_false', dest='fix_tables',
                       help='Skip table simplification')
    parser.add_argument('--no-format-fix', action='store_false', dest='fix_formatting',
                       help='Skip formatting fixes')
    parser.add_argument('--analyze', action='store_true',
                       help='Only analyze issues, don\'t fix')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    
    if args.analyze:
        print(f"Analyzing Notion import issues in: {args.input_file}")
        
        try:
            with open(args.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            issues = analyze_issues(content)
            
            print(f"\nComplete Notion Import Analysis:")
            print(f"  Total Unicode Characters: {issues['unicode_total']}")
            print(f"    - Replaceable: {issues['unicode_replaceable']}")
            print(f"    - Emojis: {issues['unicode_emojis']}")
            print(f"    - Other: {issues['unicode_other']}")
            print(f"  WikiLinks: {issues['wikilinks']}")
            print(f"  Horizontal Rules: {issues['horizontal_rules']}")
            print(f"  Total Lines: {issues['total_lines']}")
            print(f"  Complex Tables: {issues['complex_tables']}")
            print(f"  Nested Formatting: {issues['nested_formatting']}")
            
            # Recommendations
            print(f"\nRecommendations:")
            if issues['unicode_total'] > 0:
                print(f"  - Clean {issues['unicode_total']} Unicode characters")
            if issues['wikilinks'] > 0:
                print(f"  - Convert {issues['wikilinks']} WikiLinks")
            if issues['horizontal_rules'] > 0:
                print(f"  - Remove {issues['horizontal_rules']} horizontal rules")
            if issues['total_lines'] > 2000:
                print(f"  - Consider splitting {issues['total_lines']} lines into smaller documents")
            if issues['complex_tables'] > 0:
                print(f"  - Simplify {issues['complex_tables']} complex tables")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        
        return
    
    # Process the file
    print(f"Applying complete Notion import fixes to: {args.input_file}")
    
    success, output_path, before, after = process_file(
        args.input_file,
        args.output,
        fix_unicode=args.fix_unicode,
        fix_hrs=args.fix_hrs,
        fix_wikilinks=args.fix_wikilinks,
        fix_tables=args.fix_tables,
        fix_formatting=args.fix_formatting
    )
    
    if success:
        print(f"✅ Successfully processed file")
        print(f"📄 Output: {os.path.basename(output_path)}")
        
        print(f"\nProcessing Summary:")
        print(f"  Unicode Characters: {before['unicode_total']} → {after['unicode_total']}")
        print(f"  WikiLinks: {before['wikilinks']} → {after['wikilinks']}")
        print(f"  Horizontal Rules: {before['horizontal_rules']} → {after['horizontal_rules']}")
        print(f"  Complex Tables: {before['complex_tables']} → {after['complex_tables']}")
        print(f"  Total Lines: {before['total_lines']} → {after['total_lines']}")
        
        print(f"💡 Ready for Notion import!")
    else:
        print(f"❌ Error: {after}")
        sys.exit(1)

if __name__ == "__main__":
    main() 