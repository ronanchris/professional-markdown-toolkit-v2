# Obsidian + Cursor Troubleshooting Guide

This guide helps resolve common issues when using Cursor as a companion editor for Obsidian vault management.

## 🚨 Critical Safety Issues

### **Data Corruption Prevention**
**Issue:** Files getting corrupted when both Obsidian and Cursor are open
**Symptoms:** 
- Notes showing garbled text
- YAML frontmatter getting mangled
- Links becoming broken
- Sync conflicts

**Solutions:**
1. **Close Obsidian before major Cursor operations**
   ```bash
   # Before running bulk scripts
   # 1. Close Obsidian completely
   # 2. Run your Cursor operations
   # 3. Commit changes to Git
   # 4. Reopen Obsidian
   ```

2. **Use file watchers to detect conflicts**
   ```bash
   # Monitor for file changes while both apps are open
   fswatch -o /path/to/vault | xargs -n1 -I{} echo "File changed: {}"
   ```

3. **Enable auto-save delay in Cursor**
   ```json
   // In Cursor settings.json
   {
       "files.autoSave": "afterDelay",
       "files.autoSaveDelay": 2000  // 2 second delay
   }
   ```

### **Backup Strategy**
**Always implement before bulk operations:**
```bash
# 1. Commit current state
git add -A
git commit -m "Before bulk operation: $(date)"

# 2. Create backup branch
git checkout -b backup-$(date +%Y%m%d-%H%M%S)
git checkout main

# 3. Run operations

# 4. If problems occur, restore
git checkout backup-branch-name
git checkout -b main-restored
```

## 📁 File System Issues

### **Permission Problems**
**Issue:** Cannot read/write files in vault
**Error messages:**
- "Permission denied"
- "Cannot access file"
- "Read-only file system"

**Solutions:**
```bash
# Check file permissions
ls -la /path/to/vault

# Fix permissions for entire vault
chmod -R 755 /path/to/vault

# For macOS, grant Full Disk Access to Cursor
# System Preferences > Security & Privacy > Privacy > Full Disk Access
```

### **Path Issues**
**Issue:** Scripts can't find files or vault
**Common causes:**
- Spaces in path names
- Special characters in folder names
- Relative vs absolute paths

**Solutions:**
```bash
# Use quotes for paths with spaces
python script.py "/path/to/My Vault/note.md"

# Convert to absolute path
realpath "/path/to/vault"

# Check current working directory
pwd
```

### **File Encoding Problems**
**Issue:** Special characters display incorrectly
**Symptoms:**
- Emojis showing as squares
- Accented characters corrupted
- Unicode errors in scripts

**Solutions:**
```python
# Always specify UTF-8 encoding in scripts
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# For Cursor settings
{
    "files.encoding": "utf8",
    "files.autoGuessEncoding": true
}
```

## 🔗 Link and Reference Issues

### **Broken WikiLinks After Editing**
**Issue:** Links not working in Obsidian after Cursor edits
**Symptoms:**
- `[[Link]]` shows as unresolved
- Block references `^block-id` not working
- Embed syntax `![[file]]` broken

**Prevention:**
```markdown
# .cursorrules should include:
- Never convert WikiLinks to markdown links
- Preserve [[note-name]] format exactly
- Keep block references intact: ^block-id
- Maintain embed syntax: ![[file.png]]
```

**Diagnosis:**
```bash
# Find potentially broken links
grep -r "\[\[.*\]\]" vault/ | grep -v "\.md:"

# Check for converted markdown links
grep -r "\[.*\](.*\.md)" vault/

# Verify block references
grep -r "\^[a-zA-Z0-9-]*" vault/
```

**Solutions:**
```bash
# Use Obsidian's built-in link updater
# Settings > Files & Links > Automatically update internal links

# Or manually fix with regex in Cursor
# Find: \[([^\]]+)\]\(([^)]+\.md)\)
# Replace: [[$2|$1]]
```

### **Missing Files and Attachments**
**Issue:** References to files that don't exist
**Common causes:**
- Files moved outside of Obsidian
- Case sensitivity mismatches
- Renamed files without updating references

**Solutions:**
```bash
# Find broken file references
python obsidian-cursor-workflow/vault-analytics.py /path/to/vault

# Search for missing images
find vault/ -name "*.md" -exec grep -l "!\[\[.*\.\(png\|jpg\|pdf\)\]\]" {} \; | \
xargs grep -o "!\[\[.*\.\(png\|jpg\|pdf\)\]\]" | \
sort | uniq

# Use Obsidian's "Detect all file types" plugin
```

## 🏷️ Metadata and Frontmatter Issues

### **YAML Parsing Errors**
**Issue:** Frontmatter not parsing correctly
**Error symptoms:**
- Notes not appearing in Dataview queries
- Template variables not working
- Metadata fields showing as text

**Common problems:**
```yaml
# WRONG - Missing quotes around titles with colons
title: Note: Important Information

# RIGHT - Quoted titles
title: "Note: Important Information"

# WRONG - Inconsistent date formats
created: 12/25/2023
modified: 2023-12-26

# RIGHT - Consistent ISO format
created: 2023-12-25
modified: 2023-12-26

# WRONG - Mixed list formats
tags: [tag1, tag2, tag3]
categories: 
  - cat1
  - cat2

# RIGHT - Consistent format
tags: [tag1, tag2, tag3]
categories: [cat1, cat2]
```

**Validation script:**
```python
import yaml
import glob

def validate_frontmatter(vault_path):
    errors = []
    for file_path in glob.glob(f"{vault_path}/**/*.md", recursive=True):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    yaml.safe_load(parts[1])
                except yaml.YAMLError as e:
                    errors.append(f"{file_path}: {e}")
    
    return errors

# Run validation
errors = validate_frontmatter("/path/to/vault")
for error in errors:
    print(error)
```

### **Date Format Inconsistencies**
**Issue:** Mixed date formats causing template/query problems
**Common patterns:**
- `12/25/2023` (US format)
- `25/12/2023` (European format) 
- `2023-12-25` (ISO format)
- `Dec 25, 2023` (Text format)

**Standardization script:**
```python
import re
from datetime import datetime

def standardize_dates(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert MM/DD/YYYY to YYYY-MM-DD
    content = re.sub(
        r'(\d{1,2})/(\d{1,2})/(\d{4})',
        lambda m: f"{m.group(3)}-{m.group(1).zfill(2)}-{m.group(2).zfill(2)}",
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
```

## 🔍 Search and Performance Issues

### **Slow Search in Large Vaults**
**Issue:** Cursor becomes slow with large vaults (10,000+ files)
**Symptoms:**
- Search taking minutes
- High CPU usage
- Cursor becoming unresponsive

**Solutions:**
```json
// Cursor settings.json optimizations
{
    "search.exclude": {
        "**/.obsidian": true,
        "**/node_modules": true,
        "**/.git": true,
        "**/attachments": true,
        "**/*.pdf": true
    },
    "files.watcherExclude": {
        "**/.obsidian/**": true,
        "**/attachments/**": true
    },
    "editor.largeFileOptimizations": true,
    "search.maxResults": 5000
}
```

### **Git Performance Issues**
**Issue:** Git operations slow in large vaults
**Solutions:**
```bash
# Optimize Git for large repositories
git config core.preloadindex true
git config core.fscache true
git config gc.auto 256

# Use sparse checkout for huge vaults
git config core.sparseCheckout true
echo "!/attachments/*" >> .git/info/sparse-checkout
git read-tree -m -u HEAD
```

## 🏃‍♂️ Script Execution Problems

### **Python Script Errors**
**Issue:** Automation scripts failing
**Common errors:**

**Missing dependencies:**
```bash
# Error: ModuleNotFoundError: No module named 'yaml'
pip install pyyaml

# Error: No module named 'frontmatter'
pip install python-frontmatter
```

**Path encoding issues:**
```python
# Always use Path objects for cross-platform compatibility
from pathlib import Path

vault_path = Path("/path/to/vault")
for md_file in vault_path.glob("**/*.md"):
    print(md_file)
```

**Permission errors:**
```bash
# Make scripts executable
chmod +x script.py

# Run with explicit Python
python3 script.py instead of ./script.py
```

### **Shell Script Issues**
**Issue:** Bash scripts not working correctly

**Common problems:**
```bash
# WRONG - No shebang
echo "Hello World"

# RIGHT - Proper shebang
#!/bin/bash
echo "Hello World"

# WRONG - Not handling spaces in filenames
for file in $(find . -name "*.md"); do
    echo $file
done

# RIGHT - Proper handling
find . -name "*.md" -print0 | while read -d $'\0' file; do
    echo "$file"
done
```

## 🌐 Obsidian Publish and Sync Issues

### **Scripts Appearing on Published Sites**
**Issue:** Automation scripts visible on public Obsidian Publish sites
**Symptoms:**
- Python/shell scripts showing up on published website
- `.cursorrules` file visible to public
- Script folders appearing in site navigation
- Technical files contaminating professional content

**CRITICAL Solution:**
```
Settings > Core plugins > Publish > Site options:
⚠️  MUST ADD to "Excluded files":
- scripts/                    # Entire automation toolkit
- .cursorrules               # AI editing rules  
- .gitignore                 # Git configuration
- requirements.txt           # Python dependencies
- *.py                       # All Python files
- *.sh                       # All shell scripts
- *.log                      # Log files

Optional exclusions:
- consolidated-document/     # If you don't want generated docs public
- LICENSE                    # License information
- CONTRIBUTING.md           # Contribution guidelines
```

### **Sync Conflicts with Script Outputs**
**Issue:** Generated files causing sync conflicts across devices
**Symptoms:**
- Merge conflicts in `consolidated-document/`
- Large generated files slowing sync
- Log files accumulating across devices
- Script outputs overwriting each other

**Solutions:**
```
Settings > Core plugins > Sync > Settings > Selective sync:

Recommended approach:
✅ Sync scripts/ folder (keep automation consistent)
❌ Exclude outputs:
- scripts/consolidated-document/
- scripts/**/output/
- scripts/**/*.log
- scripts/**/temp/

Alternative approach (device-specific scripts):
❌ Exclude entire scripts/ folder
Note: Requires manual script installation per device
```

### **Vault Interface Cluttered with Scripts**
**Issue:** Script files appearing in daily Obsidian workflow
**Symptoms:**
- Python files in search results
- Scripts showing in graph view
- File explorer cluttered with technical files
- Autocomplete suggesting script names

**Solutions:**
```
Settings > Core plugins > Search:
Add to "Excluded files": path:scripts/

Settings > Core plugins > Graph view:
Add to "Files": path:-scripts/

Settings > Files & Links:
Add to "Excluded files": scripts/

Settings > Core plugins > Quick switcher:
Consider excluding scripts/ if it supports folder exclusions
```

## 🔧 Extension and Plugin Conflicts

### **Cursor Extensions Not Working**
**Issue:** Markdown or YAML extensions malfunctioning
**Troubleshooting:**
```bash
# 1. Check extension logs
# View > Output > Select extension from dropdown

# 2. Disable conflicting extensions temporarily
# Extensions > Disable > Test > Re-enable one by one

# 3. Reset extension settings
# Remove from settings.json and restart Cursor
```

### **Obsidian Plugin Conflicts**
**Issue:** Plugins interfering with external editing
**Common conflicts:**
- Auto-formatters changing content
- Sync plugins creating conflicts
- Backup plugins interfering with Git

**Solutions:**
```
# Temporarily disable problematic plugins:
1. Auto-format plugins during bulk operations
2. Cloud sync during Git operations  
3. File watchers during script execution

# Configure plugin exceptions:
- Exclude .cursorrules from formatters
- Set sync delays for external changes
- Configure backup exclusions
```

### **Scripts in Vault Issues**
**Issue:** Scripts appearing in Obsidian interface or published sites
**Symptoms:**
- Script files showing in graph view
- Python/shell files appearing in search results
- Scripts published on Obsidian Publish sites
- Sync conflicts with script outputs

**Solutions:**
```
# Exclude scripts from core plugins
Settings > Search: Add "path:scripts/" to excluded files
Settings > Graph view: Add "path:-scripts/" to files filter
Settings > Publish: Add "scripts/" to excluded files

# Exclude from community plugins
Dataview: Add scripts/ to excluded folders
Tag Wrangler: Add scripts/ to ignored folders

# Git considerations
Add script outputs to .gitignore:
scripts/consolidated-document/
scripts/*/output/
scripts/*/*.log
```

## 📊 Debugging and Diagnostics

### **Diagnostic Commands**
```bash
# Check vault structure
find /path/to/vault -type f -name "*.md" | wc -l

# Find problematic files
find /path/to/vault -name "*.md" -size +1M

# Check Git status
git status --porcelain | head -20

# Verify encoding
file -bi /path/to/vault/**/*.md | grep -v "utf-8"

# Check for BOM (Byte Order Mark) issues
grep -l $'\xEF\xBB\xBF' /path/to/vault/**/*.md
```

### **Health Check Script**
```python
#!/usr/bin/env python3
"""Quick health check for Obsidian vault"""

import os
import yaml
import re
from pathlib import Path

def health_check(vault_path):
    vault = Path(vault_path)
    issues = []
    
    # Check for .obsidian folder
    if not (vault / ".obsidian").exists():
        issues.append("Missing .obsidian folder - not an Obsidian vault?")
    
    # Find markdown files
    md_files = list(vault.glob("**/*.md"))
    print(f"Found {len(md_files)} markdown files")
    
    # Check for frontmatter issues
    yaml_errors = 0
    for md_file in md_files[:100]:  # Sample first 100
        try:
            content = md_file.read_text(encoding='utf-8')
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    yaml.safe_load(parts[1])
        except Exception as e:
            yaml_errors += 1
            issues.append(f"YAML error in {md_file.name}: {e}")
    
    if yaml_errors:
        print(f"⚠️  {yaml_errors} files with YAML issues")
    
    # Check for Git
    if (vault / ".git").exists():
        print("✅ Git repository detected")
    else:
        issues.append("No Git repository - consider initializing")
    
    return issues

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python health_check.py /path/to/vault")
        sys.exit(1)
    
    issues = health_check(sys.argv[1])
    if issues:
        print("\n🔍 Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ Vault appears healthy!")
```

## 🆘 Emergency Recovery

### **If Everything Goes Wrong**
**Complete vault restoration:**
```bash
# 1. Don't panic - check Git status first
git status

# 2. See what changed
git diff --name-only

# 3. Restore specific files
git checkout HEAD -- problematic-file.md

# 4. Restore entire vault to last commit
git reset --hard HEAD

# 5. If you need to go back further
git log --oneline
git reset --hard COMMIT_HASH

# 6. Nuclear option - restore from backup
cp -r /path/to/backup/vault/* /path/to/current/vault/
```

### **Prevention Checklist**
Before any major operation:
- [ ] Close Obsidian completely
- [ ] Commit current state to Git
- [ ] Test operation on small subset first
- [ ] Have .cursorrules properly configured
- [ ] Verify backup strategy is working
- [ ] Know how to restore from backup

### **When to Ask for Help**
1. **Data loss** - Stop immediately, don't make more changes
2. **Corrupted vault** - Restore from backup before troubleshooting
3. **Repeated failures** - Check system requirements and permissions
4. **Performance issues** - May need vault reorganization

---

**Remember**: Most issues are preventable with proper setup, backups, and gradual testing. When in doubt, start small and verify results before scaling up operations. 