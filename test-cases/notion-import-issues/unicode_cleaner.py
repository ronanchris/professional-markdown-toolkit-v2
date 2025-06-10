#!/usr/bin/env python3
"""
Unicode Character Cleaner for Notion Import Issues
Strips problematic Unicode characters that commonly cause Notion markdown import failures.
"""

import os
import sys
import re
import argparse
from pathlib import Path

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
    
    # Color/status circle alternatives (common in tables)
    '\u1F534': '[RED]',     # Red circle
    '\u1F7E0': '[ORANGE]',  # Orange circle  
    '\u1F7E1': '[YELLOW]',  # Yellow circle
    '\u1F7E2': '[GREEN]',   # Green circle
    '\u1F535': '[BLUE]',    # Blue circle
    '\u26AB': '[BLACK]',    # Black circle
    '\u26AA': '[WHITE]',    # White circle
    '\u1F7E3': '[PURPLE]',  # Purple circle
    '\u1F7E4': '[BROWN]',   # Brown circle
    
    # Business/table indicators
    '\u1F4C8': '[CHART_UP]',    # Chart increasing
    '\u1F4C9': '[CHART_DOWN]',  # Chart decreasing  
    '\u1F4CA': '[BAR_CHART]',   # Bar chart
    '\u1F4CB': '[CLIPBOARD]',   # Clipboard
    '\u1F4DD': '[MEMO]',        # Memo
    '\u1F4E4': '[OUTBOX]',      # Outbox tray
    '\u1F4E5': '[INBOX]',       # Inbox tray
    '\u1F50D': '[SEARCH]',      # Magnifying glass
    '\u1F527': '[WRENCH]',      # Wrench
    '\u1F680': '[ROCKET]',      # Rocket
    '\u1F3AF': '[TARGET]',      # Direct hit
    '\u1F3C6': '[TROPHY]',      # Trophy
    '\u1F948': '[SILVER]',      # Silver medal
    '\u1F949': '[BRONZE]',      # Bronze medal
    '\u1F4B0': '[MONEY]',       # Money bag
    '\u1F4F1': '[MOBILE]',      # Mobile phone
    '\u1F4E4': '[SENT]',        # Outbox
    '\u1F6A8': '[ALERT]',       # Police car light
    '\u1F6E1': '[SHIELD]',      # Shield
    '\u1F504': '[REFRESH]',     # Refresh/reload
    '\u1F465': '[USERS]',       # Busts in silhouette
    '\u1F3E2': '[BUILDING]',    # Office building
    
    # Keep these functional characters that usually work
    '\uFE0F': '',              # Variation selector (invisible)
}

# Emoji ranges to strip entirely (they cause the most Notion issues)
EMOJI_RANGES = [
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
    (0x1F680, 0x1F6FF),  # Transport and Map Symbols
    (0x1F1E0, 0x1F1FF),  # Regional Indicator Symbols
    (0x2600, 0x26FF),    # Miscellaneous Symbols
    (0x2700, 0x27BF),    # Dingbats
    (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
    (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
]

def is_emoji(char):
    """Check if character is an emoji by Unicode code point."""
    code_point = ord(char)
    return any(start <= code_point <= end for start, end in EMOJI_RANGES)

def clean_unicode_text(text, strip_emojis=True, replace_chars=True):
    """
    Clean Unicode characters from text that commonly cause Notion import issues.
    
    Args:
        text (str): Input text to clean
        strip_emojis (bool): Remove emoji characters entirely
        replace_chars (bool): Replace problematic chars with safe equivalents
    
    Returns:
        str: Cleaned text safe for Notion import
    """
    cleaned = text
    
    # First, replace characters with safe equivalents (this includes some emojis)
    if replace_chars:
        for unicode_char, replacement in UNICODE_REPLACEMENTS.items():
            cleaned = cleaned.replace(unicode_char, replacement)
    
    # Then strip remaining emojis that don't have specific replacements
    if strip_emojis:
        cleaned = ''.join(char for char in cleaned if not is_emoji(char) or char in UNICODE_REPLACEMENTS)
    
    return cleaned

def clean_markdown_file(file_path, output_path=None, strip_emojis=True, replace_chars=True, backup=True):
    """
    Clean Unicode characters from a markdown file.
    
    Args:
        file_path (str): Path to input markdown file
        output_path (str): Path for cleaned output (default: same as input)
        strip_emojis (bool): Remove emoji characters
        replace_chars (bool): Replace problematic characters
        backup (bool): Create backup of original file
    
    Returns:
        tuple: (success, message, changes_made)
    """
    try:
        # Read original file
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Clean the content
        cleaned_content = clean_unicode_text(original_content, strip_emojis, replace_chars)
        
        # Check if changes were made
        changes_made = original_content != cleaned_content
        
        if not changes_made:
            return True, "No Unicode issues found - file is already clean", False
        
        # Determine output path
        if output_path is None:
            output_path = file_path
        
        # Create backup if requested and we're overwriting
        if backup and output_path == file_path:
            backup_path = f"{file_path}.unicode-backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
        
        # Write cleaned content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        # Count changes
        original_chars = len([c for c in original_content if ord(c) > 127])
        cleaned_chars = len([c for c in cleaned_content if ord(c) > 127])
        chars_removed = original_chars - cleaned_chars
        
        message = f"Cleaned {chars_removed} problematic Unicode characters"
        if backup and output_path == file_path:
            message += f" (backup saved as {os.path.basename(backup_path)})"
        
        return True, message, True
        
    except Exception as e:
        return False, f"Error processing file: {str(e)}", False

def analyze_unicode_issues(file_path):
    """
    Analyze Unicode characters in a file and report potential issues.
    
    Args:
        file_path (str): Path to markdown file
    
    Returns:
        dict: Analysis results
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all non-ASCII characters
        non_ascii_chars = [c for c in content if ord(c) > 127]
        unique_chars = list(set(non_ascii_chars))
        
        # Categorize problems - prioritize replaceable over emoji category
        replaceable = [c for c in unique_chars if c in UNICODE_REPLACEMENTS]
        emojis = [c for c in unique_chars if is_emoji(c) and c not in UNICODE_REPLACEMENTS]
        other_unicode = [c for c in unique_chars if not is_emoji(c) and c not in UNICODE_REPLACEMENTS]
        
        return {
            'total_non_ascii': len(non_ascii_chars),
            'unique_chars': len(unique_chars),
            'emojis': len(emojis),
            'replaceable': len(replaceable),
            'other_unicode': len(other_unicode),
            'emoji_list': emojis,
            'replaceable_list': replaceable,
            'other_list': other_unicode
        }
        
    except Exception as e:
        return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description='Clean Unicode characters causing Notion import issues')
    parser.add_argument('input_file', help='Input markdown file to clean')
    parser.add_argument('-o', '--output', help='Output file path (default: overwrite input)')
    parser.add_argument('--no-emojis', action='store_false', dest='strip_emojis', 
                       help='Keep emoji characters (not recommended for Notion)')
    parser.add_argument('--no-replace', action='store_false', dest='replace_chars',
                       help='Don\'t replace problematic characters with safe equivalents')
    parser.add_argument('--no-backup', action='store_false', dest='backup',
                       help='Don\'t create backup file')
    parser.add_argument('--analyze', action='store_true',
                       help='Only analyze Unicode issues, don\'t clean')
    parser.add_argument('--verbose', action='store_true',
                       help='Show detailed analysis')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found")
        sys.exit(1)
    
    if args.analyze or args.verbose:
        print(f"Analyzing Unicode issues in: {args.input_file}")
        analysis = analyze_unicode_issues(args.input_file)
        
        if 'error' in analysis:
            print(f"Error: {analysis['error']}")
            sys.exit(1)
        
        print(f"\nUnicode Analysis Results:")
        print(f"  Total non-ASCII characters: {analysis['total_non_ascii']}")
        print(f"  Unique Unicode characters: {analysis['unique_chars']}")
        print(f"  Emojis (will be removed): {analysis['emojis']}")
        print(f"  Replaceable characters: {analysis['replaceable']}")
        print(f"  Other Unicode: {analysis['other_unicode']}")
        
        if args.verbose and analysis['unique_chars'] > 0:
            print(f"\nDetailed Character List:")
            all_chars = analysis['emoji_list'] + analysis['replaceable_list'] + analysis['other_list']
            for char in sorted(all_chars, key=ord):
                category = "EMOJI" if is_emoji(char) else "REPLACEABLE" if char in UNICODE_REPLACEMENTS else "OTHER"
                replacement = UNICODE_REPLACEMENTS.get(char, "[REMOVE]" if is_emoji(char) else "[KEEP]")
                print(f"  U+{ord(char):04X}: '{char}' ({category}) -> {replacement}")
        
        if args.analyze:
            return
    
    # Clean the file
    print(f"Cleaning Unicode characters in: {args.input_file}")
    success, message, changes_made = clean_markdown_file(
        args.input_file, 
        args.output, 
        args.strip_emojis, 
        args.replace_chars, 
        args.backup
    )
    
    if success:
        print(f"✅ {message}")
        if changes_made:
            output_file = args.output or args.input_file
            print(f"📄 Cleaned file: {output_file}")
            print(f"💡 Ready for Notion import!")
        sys.exit(0)
    else:
        print(f"❌ {message}")
        sys.exit(1)

if __name__ == "__main__":
    main() 