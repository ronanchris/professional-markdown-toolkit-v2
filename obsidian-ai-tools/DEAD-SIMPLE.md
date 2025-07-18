# Dead Simple Guide

**When your brain is fried and you just need to know which script to run.**

## 🔥 **Most Common: Fix Notion Import Issues**

### **Document won't import to Notion** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/notion_complete_fixer.py your-document.md
```
**What it does**: Fixes Unicode, emojis, WikiLinks, horizontal rules - everything that breaks Notion imports.  
**Success rate**: 95%+ for import failures

### **Want to see what's wrong first** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/notion_complete_fixer.py your-document.md --analyze
```
**What it does**: Shows you exactly what's causing the import problems without fixing anything.

## 📊 **Generate Project Documentation**

### **Need project sitemap or documentation** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/project-structure/generate_project_structure.py
```
**What it does**: Creates comprehensive PROJECT-STRUCTURE.md with file counts, directory tree, and AI-friendly project context.

## 🧹 **Clean Up Obsidian Files**

### **Remove YAML frontmatter and Templater code** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/metadata-tools/remove_metadata.sh
```
**What it does**: Strips `<%* code %>`, `` `= this.file.name` ``, and YAML frontmatter from markdown files.

### **Safe metadata removal (Python version)** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/metadata-tools/safe_metadata_removal.py
```
**What it does**: More granular control over metadata removal with detailed reporting.

### **Fix broken metadata and standardize** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/metadata-tools/fix_metadata.sh
```
**What it does**: Repairs malformed YAML frontmatter and standardizes metadata formatting.

### **Clean up old/corrupted files** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/metadata-tools/clean_files.sh
```
**What it does**: Advanced file cleanup for corrupted or problematic markdown files.

### **Update old date fields to Templater format** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/metadata-tools/update_date_created_to_templater.py
```
**What it does**: Converts old date_created fields to Templater `<%* tp.file.creation_date() %>` format.

## 📝 **Template Management**

### **Apply templates to inbox files** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/template-management/apply_template.sh
```
**What it does**: Applies your inbox template to new markdown files.

### **Fix broken templates** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/template-management/fix_template.sh
```
**What it does**: Repairs and standardizes template formatting.

### **Apply templates (Python version with dry-run)** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/template-management/apply_inbox_template.py --dry-run
```
**What it does**: More control over template application with preview mode.

### **Apply templates to entire folders** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/template-management/apply_inbox_template_to_folder.py
```
**What it does**: Batch apply templates to all files in a directory.

### **Apply MOC templates safely** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/template-management/apply_moc_template_preserve_metadata.py
```
**What it does**: Applies MOC (Map of Content) templates while preserving existing metadata.

### **Update inbox files with new template** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/template-management/update_inbox_with_template.py
```
**What it does**: Updates existing inbox files with new template format.

## 🎯 **Markdown Formatting & Cleanup**

### **Clean up extra spaces and formatting** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/cleanup_markdown_batch.py
```
**What it does**: Removes extra whitespace, fixes bullet points, normalizes markdown formatting.

### **Clean single file formatting** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/cleanup_markdown.py your-file.md
```
**What it does**: Same as batch version but for individual files.

### **Clean all markdown files in directory** → Use this:
```bash
obsidian-ai-tools/obsidian-tools/markdown-processing/clean_all_markdown.sh
```
**What it does**: Runs cleanup on all .md files in current directory and subdirectories.

## 🎯 **Specific Notion Problems**

### **Emojis and special characters breaking import** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/unicode_cleaner.py your-document.md
```

### **WikiLinks not working in Notion** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/wikilink_converter.py your-document.md
```

### **Too many horizontal rules (---) causing issues** → Use this:
```bash
python obsidian-ai-tools/obsidian-tools/markdown-processing/notion_import_fixer.py your-document.md
```

## 🧠 **AI Collaboration Enhancement**

### **Want better AI collaboration patterns** → Use this:
```bash
# Copy the session continuity templates to your project root
cp -r obsidian-ai-tools/ai-collaboration/universal-session-continuity ./
```
**What it does**: Deploys proven AI collaboration patterns for better human-AI partnerships.

### **Need Cursor integration help** → Check this:
```bash
# Read the integration guides
open obsidian-ai-tools/integration-guides/README.md
```
**What it does**: Provides complete Cursor + Obsidian workflow setup and troubleshooting.

## ⚡ **Quick Decision Tree**

**Problem**: Document won't import to Notion  
**Solution**: `notion_complete_fixer.py` ← **Start here, fixes 95% of cases**

**Problem**: Need to clean Obsidian vault files  
**Solution**: `remove_metadata.sh` ← **Removes YAML and Templater code**

**Problem**: Broken or malformed metadata  
**Solution**: `fix_metadata.sh` ← **Repairs and standardizes metadata**

**Problem**: Messy markdown formatting  
**Solution**: `cleanup_markdown_batch.py` ← **Fixes spacing and formatting**

**Problem**: Want to apply templates  
**Solution**: `apply_template.sh` ← **For inbox files**

**Problem**: Need to apply templates to many files  
**Solution**: `apply_inbox_template_to_folder.py` ← **Batch template application**

**Problem**: MOC files need templates  
**Solution**: `apply_moc_template_preserve_metadata.py` ← **Safe MOC template application**

**Problem**: Need project documentation or sitemap  
**Solution**: `generate_project_structure.py` ← **Creates comprehensive documentation**

**Problem**: Old date fields need updating  
**Solution**: `update_date_created_to_templater.py` ← **Converts to Templater format**

**Problem**: Want better AI collaboration  
**Solution**: Copy `ai-collaboration/universal-session-continuity/` to project root

## 🚨 **Safety Notes**

- **All scripts create automatic backups** in `obsidian-ai-tools/shared/backups/`
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

### **For template management:**
1. **Test first**: Use `--dry-run` with Python scripts
2. **Individual files**: Use shell scripts (`.sh`)
3. **Batch operations**: Use Python scripts
4. **MOC files**: Use `apply_moc_template_preserve_metadata.py`

### **For AI collaboration:**
1. **Copy session continuity templates** to your project root
2. **Read integration guides** for Cursor setup
3. **Use proven patterns** rather than starting from scratch

### **When in doubt:**
- Use `--analyze` flag to see what will change
- Check the backups folder if something goes wrong
- All scripts have `--help` for more options
- Read the `TOOLKIT-GUIDE.md` for comprehensive documentation

---

**Bottom line**: 90% of the time you want `notion_complete_fixer.py` for Notion issues or `remove_metadata.sh` for Obsidian cleanup. For AI collaboration, copy the `ai-collaboration/` templates. Start there. 