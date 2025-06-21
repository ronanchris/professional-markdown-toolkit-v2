# Dead Simple Guide

**When your brain is fried and you just need to know which script to run.**

## 🔥 **Most Common: Fix Notion Import Issues**

### **Document won't import to Notion** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py your-document.md
```
**What it does**: Fixes Unicode, emojis, WikiLinks, horizontal rules - everything that breaks Notion imports.  
**Success rate**: 95%+ for import failures

### **Want to see what's wrong first** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py your-document.md --analyze
```
**What it does**: Shows you exactly what's causing the import problems without fixing anything.

## 📊 **Generate Project Documentation**

### **Need project sitemap or documentation** → Use this:
```bash
python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```
**What it does**: Creates comprehensive PROJECT-STRUCTURE.md with file counts, directory tree, and AI-friendly project context.

## 🧹 **Clean Up Obsidian Files**

### **Remove YAML frontmatter and Templater code** → Use this:
```bash
portable-obsidian-tools/metadata-tools/remove_metadata.sh
```
**What it does**: Strips `<%* code %>`, `` `= this.file.name` ``, and YAML frontmatter from markdown files.

### **Apply templates to inbox files** → Use this:
```bash
portable-obsidian-tools/obsidian-tools/apply_template.sh
```
**What it does**: Applies your inbox template to new markdown files.

### **Clean up extra spaces and formatting** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py
```
**What it does**: Removes extra whitespace, fixes bullet points, normalizes markdown formatting.

## 🎯 **Specific Notion Problems**

### **Emojis and special characters breaking import** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/unicode_cleaner.py your-document.md
```

### **WikiLinks not working in Notion** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/wikilink_converter.py your-document.md
```

### **Too many horizontal rules (---) causing issues** → Use this:
```bash
python portable-obsidian-tools/markdown-processing/notion_import_fixer.py your-document.md
```

## ⚡ **Quick Decision Tree**

**Problem**: Document won't import to Notion  
**Solution**: `notion_complete_fixer.py` ← **Start here, fixes 95% of cases**

**Problem**: Need to clean Obsidian vault files  
**Solution**: `remove_metadata.sh` ← **Removes YAML and Templater code**

**Problem**: Messy markdown formatting  
**Solution**: `cleanup_markdown_batch.py` ← **Fixes spacing and formatting**

**Problem**: Want to apply templates  
**Solution**: `apply_template.sh` ← **For inbox files**

**Problem**: Need project documentation or sitemap  
**Solution**: `generate_project_structure.py` ← **Creates comprehensive documentation**

## 🚨 **Safety Notes**

- **All scripts create automatic backups** in `portable-obsidian-tools/backups/`
- **Add `--dry-run` to Python scripts** to test without changing files
- **Add `--analyze` to see what would change** without doing it

## 💡 **Pro Tips**

### **For Notion imports:**
1. **Always start with**: `notion_complete_fixer.py` (fixes everything at once)
2. **If still failing**: Check file size (>10MB can be problematic)
3. **Large documents**: Consider splitting into smaller sections

### **For Obsidian cleanup:**
1. **Remove metadata first**: `remove_metadata.sh`
2. **Then clean formatting**: `cleanup_markdown_batch.py`
3. **Apply templates last**: `apply_template.sh`

### **When in doubt:**
- Use `--analyze` flag to see what will change
- Check the backups folder if something goes wrong
- All scripts have `--help` for more options

---

**Bottom line**: 90% of the time you want `notion_complete_fixer.py` for Notion issues or `remove_metadata.sh` for Obsidian cleanup. Start there. 