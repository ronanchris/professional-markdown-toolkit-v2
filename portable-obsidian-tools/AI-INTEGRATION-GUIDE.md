# AI Integration Guide for Portable Obsidian Tools

**Instructions for AI Assistants (Cursor AI, Claude, etc.) when working with Obsidian markdown files**

## 🎯 **Core AI Instructions**

### **Always Check First:**
1. Verify `portable-obsidian-tools/` folder exists in project root
2. Confirm user has Obsidian vault structure (folders like `0-inbox/`, `00-MOCs/`)
3. Ask about backup preferences (enabled by default, can disable with `--no-backup`)
4. For large vaults (1000+ pages), suggest using cursor-rules-templates/ for enhanced safety

### **Decision Matrix for Common Requests:**

| **User Says** | **Action** | **Tool** | **Safety Level** |
|---------------|------------|----------|------------------|
| "Clean my markdown" | Remove YAML frontmatter | `remove_metadata.sh` | 🟢 Auto-backup |
| "Remove extra spaces" | Clean whitespace/formatting | `cleanup_markdown_batch.py` | 🟢 Auto-backup |
| "Format my markdown" | Comprehensive formatting | `cleanup_markdown_batch.py` | 🟢 Auto-backup |
| "Fix my templates" | Apply/repair templates | `apply_template.sh` or `fix_template.sh` | 🟢 Auto-backup |
| "Remove Templater code" | Clean Templater syntax | `remove_metadata.sh` | 🟢 Auto-backup |
| "Process MOC files" | MOC template with preservation | `apply_moc_template_preserve_metadata.py` | 🟢 Auto-backup |
| "Generate sitemap" / "project docs" | Generate project structure | `generate_project_structure.py` | 🟢 Documentation only |
| "Test first" | Dry-run mode | Add `--dry-run` to Python scripts | 🟡 Read-only |
| "I'm advanced user" | Skip backups | Add `--no-backup` flag | 🔴 No backup |

## 🛠️ **Exact Commands to Use**

### **Most Common Operations:**
```bash
# Clean YAML frontmatter and Templater code
portable-obsidian-tools/metadata-tools/remove_metadata.sh

# Clean whitespace, formatting, extra spaces
python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py

# Apply templates to inbox files  
portable-obsidian-tools/obsidian-tools/apply_template.sh

# Test template application first (dry-run)
python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run

# Process MOC files with metadata preservation
python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py

# Advanced metadata cleaning
portable-obsidian-tools/metadata-tools/fix_metadata.sh

# Generate comprehensive project documentation (NEW!)
python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### **With Options:**
```bash
# Skip backups (advanced users)
portable-obsidian-tools/metadata-tools/remove_metadata.sh --no-backup

# Get help for any script
portable-obsidian-tools/obsidian-tools/apply_template.sh --help

# Apply templates then clean
portable-obsidian-tools/obsidian-tools/apply_template.sh
portable-obsidian-tools/metadata-tools/remove_metadata.sh
```

## 💬 **AI Response Templates**

### **When User Asks About Markdown Cleanup:**
```
I can help you clean up your Obsidian markdown files using the portable tools.

**Available actions:**
- Clean YAML frontmatter: `portable-obsidian-tools/metadata-tools/remove_metadata.sh`
- Apply templates: `portable-obsidian-tools/obsidian-tools/apply_template.sh`
- Advanced cleaning: `portable-obsidian-tools/metadata-tools/fix_metadata.sh`

**Safety:** All operations create automatic backups in `portable-obsidian-tools/backups/`

Would you like me to proceed with automatic backups enabled?
```

### **When User Mentions Testing/Safety:**
```
Great approach! These tools offer safe testing options:

**For testing:**
- Dry-run mode: `python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run`
- View what would change without making changes

**For safety:**
- Automatic backups (default): Creates timestamped backups before changes
- Manual restore: Instructions provided after each operation
- Skip backups: Add `--no-backup` for advanced users

Which approach would you prefer?
```

### **When User Has Template Problems:**
```
I can help fix your template issues using these specialized tools:

**Template problems:**
- Apply new templates: `portable-obsidian-tools/obsidian-tools/apply_template.sh`
- Fix broken templates: `portable-obsidian-tools/obsidian-tools/fix_template.sh`
- MOC template preservation: `python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py`

**Templater integration:** These tools handle Templater syntax (`<%* ... -%>`, `` `= this.file.name` ``)

What type of template issue are you experiencing?
```

### **When User Needs Project Documentation:**
```
I can generate comprehensive project documentation using the PROJECT-STRUCTURE tool:

**Project Documentation:**
- Complete sitemap: `python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py`
- Creates PROJECT-STRUCTURE.md with file counts, directory hierarchy, and AI context
- Customizable via project_template.json for project-specific descriptions

**Benefits:**
- Provides complete project context for AI assistants
- Automatically detects project structure and generates statistics
- Works from any directory within the project

Would you like me to generate current project documentation?
```

### **When User Has Large Vault (1000+ pages):**
```
For large Obsidian vaults, I recommend using the specialized Cursor rules templates:

**Cursor Rules Setup:**
- Ready-to-use rules in `portable-obsidian-tools/cursor-rules-templates/`
- 4 specialized rules: syntax preservation, vault safety, selection scope, tool integration
- Optimized for large vault operations with enhanced safety protocols

**Benefits:**
- Prevents accidental WikiLink corruption across hundreds of files
- Enforces dry-run testing before bulk operations
- Respects user selections precisely
- Provides intelligent tool suggestions

Would you like me to help you set up these specialized Cursor rules?
```

## 🔍 **Troubleshooting AI Responses**

### **Common Issues & AI Solutions:**

**"Script not found":**
```
The script path needs to be run from your project root. Let me run:
`portable-obsidian-tools/metadata-tools/remove_metadata.sh`

If this fails, let's verify the portable tools are properly installed.
```

**"No vault structure found":**
```
The tools expect Obsidian vault structure. Let me check if you have:
- `0-inbox/` folder for inbox files
- `00-MOCs/` folder for MOC files

Should I help you create the expected folder structure?
```

**"PyYAML missing":**
```
The Python tools need PyYAML. Let me install it:
`cd portable-obsidian-tools && pip install -r requirements.txt`
```

**"Permission denied":**
```
Let me fix the script permissions:
`chmod +x portable-obsidian-tools/obsidian-tools/*.sh`
`chmod +x portable-obsidian-tools/metadata-tools/*.sh`
```

## 🎯 **Best Practices for AI Assistants**

### **Always:**
1. **Confirm tool exists** before suggesting commands
2. **Explain what the tool does** before running it
3. **Mention backup system** so user feels safe
4. **Offer dry-run first** for testing when available
5. **Provide restore instructions** after destructive operations

### **Never:**
1. **Skip explaining backups** - users need to know their files are safe
2. **Use tools on non-Obsidian files** - these are specialized for Obsidian
3. **Assume advanced user** - always offer backup options first
4. **Run multiple destructive operations** without user confirmation

### **Decision Flow:**
```
User request → Check if tools exist → Explain what tool does → 
Mention safety features → Ask for confirmation → Run command → 
Provide backup/restore info
```

## 📋 **Quick Reference for AI**

**Problem Recognition:**
- "YAML frontmatter" / "metadata" → `remove_metadata.sh`
- "Templater" / "`<%*`" / "`` `= this.file.name` ``" → `remove_metadata.sh`
- "templates" / "inbox files" → `apply_template.sh`
- "MOC" / "preserve metadata" → `apply_moc_template_preserve_metadata.py`
- "sitemap" / "project structure" / "documentation" → `generate_project_structure.py`
- "test" / "dry-run" → Add `--dry-run` flag to Python scripts

**Safety Levels:**
- 🟢 **Safe**: Default with auto-backups
- 🟡 **Testing**: Dry-run mode  
- 🔴 **Advanced**: `--no-backup` flag

**File Types:**
- `.sh` scripts: Batch processing, auto-backup, faster
- `.py` scripts: More control, dry-run mode, metadata preservation 