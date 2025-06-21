# Portable Obsidian Tools

**Self-contained toolkit for Obsidian vault management - copy anywhere and use immediately!**

## 🤖 **AI Assistant Quick Reference**

**For Cursor AI / Claude / Other AI Assistants working with Obsidian markdown:**

### **Problem → Solution Mapping**

| **User Problem** | **Exact Tool to Use** | **Command** |
|------------------|----------------------|-------------|
| "Clean up YAML frontmatter" | `remove_metadata.sh` | `portable-obsidian-tools/metadata-tools/remove_metadata.sh` |
| "Remove Templater code" | `remove_metadata.sh` | `portable-obsidian-tools/metadata-tools/remove_metadata.sh` |
| "Apply templates to inbox files" | `apply_template.sh` | `portable-obsidian-tools/obsidian-tools/apply_template.sh` |
| "Fix broken templates" | `fix_template.sh` | `portable-obsidian-tools/obsidian-tools/fix_template.sh` |
| "Process MOC files safely" | `apply_moc_template_preserve_metadata.py` | `python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py` |
| "Test changes first" | Any Python script with `--dry-run` | `python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run` |
| "Clean metadata but keep some fields" | `apply_moc_template_preserve_metadata.py` | `python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py` |
| "Advanced metadata cleaning" | `fix_metadata.sh` | `portable-obsidian-tools/metadata-tools/fix_metadata.sh` |
| "Won't import into Notion" | `notion_complete_fixer.py` | `python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py` |
| "Unicode/emoji import issues" | `unicode_cleaner.py` | `python portable-obsidian-tools/markdown-processing/unicode_cleaner.py` |
| "WikiLinks in Notion export" | `wikilink_converter.py` | `python portable-obsidian-tools/markdown-processing/wikilink_converter.py` |

### **AI Communication Templates**

**When user asks about markdown cleanup:**
```
I'll help you clean up your markdown files using the portable Obsidian tools. 

For YAML frontmatter removal: `portable-obsidian-tools/metadata-tools/remove_metadata.sh`
For template application: `portable-obsidian-tools/obsidian-tools/apply_template.sh`

Both tools have automatic backup systems. Would you like me to run with backups enabled (safer) or disabled (faster)?
```

**When user asks about templates:**
```
I can help you with template management using these tools:

- Apply templates: `portable-obsidian-tools/obsidian-tools/apply_template.sh`
- Fix broken templates: `portable-obsidian-tools/obsidian-tools/fix_template.sh`  
- Test first (dry-run): `python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run`

Which operation would you like to perform?
```

**When user mentions backup concerns:**
```
All tools have built-in backup systems that create timestamped backups in `portable-obsidian-tools/backups/`.

Safe mode (default): Automatic backups
Advanced mode: Add `--no-backup` flag

Restoration instructions are provided after each operation.
```

**When user has Notion import issues:**
```
I can help you fix Notion import issues with these specialized tools:

All-in-one solution: `python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py your-document.md`

Specific fixes available:
- Unicode/emoji issues: `unicode_cleaner.py`
- WikiLink conversion: `wikilink_converter.py`  
- Horizontal rules/formatting: `notion_import_fixer.py`

Would you like me to analyze your document first to see what issues exist?
```

**When user needs project documentation:**
```
I can generate comprehensive project documentation with the PROJECT-STRUCTURE tool:

`python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py`

This creates PROJECT-STRUCTURE.md with:
- Complete file inventory and statistics
- Hierarchical directory structure
- Project context for AI assistants
- Customizable templates for different project types

Would you like me to run this to create current project documentation?
```

### **Decision Tree for AI Assistants**

```
User mentions markdown problems:
├── YAML/frontmatter issues → remove_metadata.sh
├── Template problems → apply_template.sh or fix_template.sh  
├── MOC files → apply_moc_template_preserve_metadata.py
├── Want to test first → Use --dry-run flag
├── Batch processing → Use shell scripts (.sh files)
└── Need metadata preservation → Use Python scripts with preservation
```

## 🚀 **Quick Setup (30 seconds)**

1. **Copy this entire folder** to your project:
   ```bash
   cp -r portable-obsidian-tools /path/to/your/project/
   ```

2. **Install Python dependencies** (one-time setup):
   ```bash
   cd /path/to/your/project/portable-obsidian-tools
   pip install -r requirements.txt
   ```

3. **You're ready!** Run scripts from your project root:
   ```bash
   # Apply templates to inbox files
   portable-obsidian-tools/obsidian-tools/apply_template.sh
   
   # Clean metadata from files  
   portable-obsidian-tools/metadata-tools/remove_metadata.sh
   ```

## 📁 **What's Included**

```
portable-obsidian-tools/
├── obsidian-tools/          # Obsidian-specific template and structure tools
├── metadata-tools/          # YAML frontmatter and metadata management
├── markdown-processing/     # Whitespace cleanup and markdown formatting
├── PROJECT-STRUCTURE/       # Automated project documentation generator
├── cursor-rules-templates/  # Ready-to-use Cursor rules for large Obsidian vaults
├── shared/                  # Backup system (used by all scripts)
├── requirements.txt         # Python dependencies
└── README.md               # This guide
```

## 🛠️ **Core Tools**

### **Template Management** (`obsidian-tools/`)
- **`apply_template.sh`** - Apply inbox templates with Templater code
- **`fix_template.sh`** - Repair and standardize template formatting
- **`apply_inbox_template.py`** - Python-based template application (dry-run mode)
- **`apply_moc_template_preserve_metadata.py`** - MOC templates with metadata preservation

### **Metadata Management** (`metadata-tools/`)
- **`remove_metadata.sh`** - Clean YAML frontmatter and Templater code
- **`fix_metadata.sh`** - Advanced metadata cleaning and standardization
- **`clean_files.sh`** - Comprehensive file cleaning

### **Project Documentation** (`PROJECT-STRUCTURE/`)
- **`generate_project_structure.py`** - Auto-generate comprehensive PROJECT-STRUCTURE.md documentation
- **Template system** - Customizable project context and descriptions
- **Universal detection** - Works from any directory, finds project root automatically
- **AI integration** - Creates context-rich documentation for AI assistants

### **Cursor Rules Templates** (`cursor-rules-templates/`)
- **Ready-to-use Cursor rules** for large Obsidian vaults (1000+ pages)
- **4 specialized rules** - syntax preservation, vault safety, selection scope, tool integration
- **Copy-paste ready** - just copy content into your project's Cursor rules
- **Safety optimized** - prevents disasters in large vault operations

### **Markdown Processing** (`markdown-processing/`)

#### **Notion Import Tools** ⭐ **NEW**
- **`notion_complete_fixer.py`** - All-in-one Notion import issue resolver (95%+ success rate)
- **`unicode_cleaner.py`** - Smart Unicode character replacements  
- **`wikilink_converter.py`** - Convert `[[WikiLinks]]` to `**Bold Text**`
- **`notion_import_fixer.py`** - Notion-specific formatting fixes
- **`README-NOTION-TOOLS.md`** - Quick reference guide
- **Header formatting fix** - Resolves stray asterisks in headers (e.g., "Section 18: Title**")

#### **General Markdown Tools**
- **`cleanup_markdown_batch.py`** - Remove extra spaces, format whitespace, clean markdown
- **`clean_all_markdown.sh`** - Vault-wide markdown formatting
- **`cleanup_markdown.py`** - Single-file markdown cleanup

## 💡 **Usage Examples**

### **Basic Operations**
```bash
# Clean up inbox files (with automatic backup)
portable-obsidian-tools/metadata-tools/remove_metadata.sh

# Apply templates to new files
portable-obsidian-tools/obsidian-tools/apply_template.sh

# Test operations first (dry-run)
python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run

# Clean extra spaces and format markdown
python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py

# Fix Notion import issues (NEW!)
python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py document.md

# Generate project documentation (NEW!)
python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py

# Set up Cursor rules for large Obsidian vaults (NEW!)
# Copy rules from portable-obsidian-tools/cursor-rules-templates/ to your Cursor settings
```

### **Advanced Usage**
```bash
# Skip backups (advanced users only)
portable-obsidian-tools/metadata-tools/remove_metadata.sh --no-backup

# Get help for any script
portable-obsidian-tools/obsidian-tools/apply_template.sh --help
```

## 🔧 **Requirements**

- **Python 3.7+** with PyYAML (install: `pip install -r requirements.txt`)
- **Bash shell** (macOS/Linux/WSL)
- **Obsidian vault** with standard folder structure (e.g., `0-inbox/`, `00-MOCs/`)

## 🛡️ **Safety Features**

### **Automatic Backups**
All scripts create timestamped backups before making changes:
- **Location**: `portable-obsidian-tools/backups/YYYYMMDD_HHMMSS/`
- **Restoration**: Instructions provided after each operation
- **Disable**: Use `--no-backup` flag if needed

### **Vault Structure Detection**
Scripts automatically detect your vault structure and work relative to your project root.

## 🎯 **Cursor AI Integration**

### **Add to your Cursor Rules:**
```markdown
# Obsidian Tools Integration
- Use portable-obsidian-tools/ scripts for Obsidian vault management
- All scripts have built-in backup systems and --help flags
- Scripts work from project root, automatically detect vault structure
```

### **Common Cursor Prompts:**
```
"Help me clean up metadata in my Obsidian files using the portable tools"
"I want to apply templates to my inbox files safely"
"Show me how to use the backup system in the Obsidian tools"
```

## 🔍 **Troubleshooting**

### **"Script not found" error:**
- Run scripts from your project root (where you copied the portable-obsidian-tools folder)
- Use full path: `portable-obsidian-tools/obsidian-tools/script-name.sh`

### **"PyYAML not found" error:**
```bash
cd portable-obsidian-tools
pip install -r requirements.txt
```

### **"Vault structure not found" error:**
- Ensure you have Obsidian folders like `0-inbox/` in your project root
- Scripts expect standard Obsidian vault structure

### **Permission denied:**
```bash
chmod +x portable-obsidian-tools/obsidian-tools/*.sh
chmod +x portable-obsidian-tools/metadata-tools/*.sh
```

## 📋 **Quick Reference**

### **Most Common Operations:**
```bash
# 1. Clean metadata from inbox
portable-obsidian-tools/metadata-tools/remove_metadata.sh

# 2. Apply templates to files  
portable-obsidian-tools/obsidian-tools/apply_template.sh

# 3. Process MOC files
python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py

# 4. Get help for any script
portable-obsidian-tools/[tool-folder]/[script-name] --help
```

## 🎉 **That's It!**

You now have a complete, self-contained Obsidian toolkit that you can copy to any project and use immediately. All safety features, backup systems, and professional functionality included!

---

**💡 Pro Tip**: Keep one copy of this folder as your "master" and just copy it to new projects as needed. No setup required - just copy and run! 