# Cursor + Obsidian Workflow Guide

This guide explains how to use **Cursor as a powerful companion editor** for Obsidian vault management. This workflow combines the best of both tools: Obsidian's excellent note-taking and linking capabilities with Cursor's advanced editing, AI assistance, and bulk operation features.

**🎯 New to Python or command-line tools?** Don't worry! Cursor will teach you everything step by step. You don't need any programming experience - just follow the prompts in `cursor-prompts-guide.md`.

## 🎯 The Power User Workflow

### **Cursor as a Writing Environment**
**Beyond Obsidian**: Cursor transforms writing across many platforms by providing:
- **Collaborative AI assistance** - Work with AI as a writing partner, not through separate chat
- **Context-aware help** - AI understands your entire document structure and writing goals
- **Professional workflows** - Git integration, formatting automation, and publishing pipelines
- **Distraction-free writing** - Stay in your document without switching between tools

*This approach works with Notion, Roam Research, LogSeq, Zettlr, standard markdown, and any text-based writing system.*

### **Obsidian: Your Primary Interface**
- Daily note-taking and journaling
- Link creation and graph exploration  
- Plugin ecosystem (templates, calendar, etc.)
- Mobile synchronization
- Reading and reviewing content

### **Cursor: Your Vault Operations Center**
- Bulk metadata management
- Multi-file search and replace operations
- Automated formatting and cleanup
- YAML frontmatter standardization
- Large-scale reorganization
- Professional document generation
- Git version control management

## 🚀 Getting Started

### **1. Setup Your Vault in Cursor**
```bash
# Open your Obsidian vault as a project in Cursor
cd /path/to/your/obsidian/vault
cursor .

# Or use File > Open Folder in Cursor
```

### **2. Install Recommended Cursor Extensions**
- **Markdown All in One** - Enhanced markdown editing
- **YAML** - Better YAML frontmatter support
- **GitLens** - Advanced Git integration
- **Regex Preview** - Visual regex testing

### **3. Configure Cursor Rules**
Copy the rules from `cursor-rules-obsidian.md` to your vault's `.cursorrules` file (see below for details).

## 📋 Essential Cursor Rules for Obsidian

Create a `.cursorrules` file in your vault root with these rules:

### **YAML Frontmatter Rules**
- Always preserve existing YAML frontmatter
- Use consistent date formats (YYYY-MM-DD)
- Maintain standard field names (title, tags, created, modified)
- Never remove metadata without explicit instruction

### **Obsidian Syntax Rules**
- Preserve WikiLinks format `[[note-name]]`
- Maintain block references `^block-id`
- Keep embed syntax `![[image.png]]`
- Preserve tag formats `#tag` and `#nested/tag`

### **Content Safety Rules**
- Never modify content meaning, only formatting
- Preserve all links and references
- Maintain heading structure and hierarchy
- Keep code blocks and callouts intact

## 🛠️ Common Operations

### **Bulk Metadata Updates**
```bash
# Add missing 'modified' dates to all notes
python scripts/metadata-tools/update_date_created_to_templater.py vault/

# Standardize tag formats across vault
# Use Cursor's find/replace with regex
```

### **Format Cleanup**
```bash
# Clean up markdown formatting issues
python scripts/markdown-processing/cleanup_markdown_batch.py vault/ --recursive

# Apply templates to inbox notes
python scripts/obsidian-tools/apply_inbox_template_to_folder.py vault/inbox/
```

### **Quality Assurance**
```bash
# Check for broken links (use Cursor's search)
# Search for: \[\[.*\|\]\]  (empty link text)

# Find notes without frontmatter
# Search for files that don't start with ---
```

## 🎯 Advanced Techniques

### **Multi-Vault Management**
```bash
# Process multiple vaults efficiently
for vault in ~/vaults/*/; do
    echo "Processing $vault"
    python scripts/markdown-processing/clean_all_markdown.sh "$vault"
done
```

### **Content Migration**
```bash
# Convert Roam Research blocks to Obsidian format
# Use Cursor's regex find/replace:
# Find: {{.*?}}
# Replace with appropriate Obsidian syntax
```

### **Professional Document Generation**
```bash
# Generate executive reports from vault content
cd scripts/company-executive
./build-consolidated-doc.sh
```

## 📊 Workflow Examples

### **Daily Vault Maintenance**
1. **Open vault in Cursor** for bulk operations
2. **Run cleanup scripts** to fix formatting issues
3. **Update metadata** using batch operations
4. **Commit changes** with descriptive Git messages
5. **Return to Obsidian** for content work

### **Monthly Vault Audit**
1. **Search for orphaned notes** (no backlinks)
2. **Standardize tag hierarchies** using find/replace
3. **Update templates** and apply to relevant notes
4. **Generate analytics** on vault growth and structure
5. **Backup and version control** cleanup

### **Project Documentation**
1. **Collect related notes** using Cursor's search
2. **Apply consistent formatting** with scripts
3. **Generate consolidated documents** for sharing
4. **Export to professional formats** (PDF, etc.)

## ⚠️ Best Practices

### **Safety First**
- **Always commit** to Git before bulk operations
- **Test on small subsets** before processing entire vault
- **Use dry-run modes** when available
- **Keep Obsidian closed** during bulk operations to avoid conflicts

### **Metadata Consistency**
- **Standardize date formats** across all notes
- **Use consistent tag hierarchies** (#project/work vs #work/project)
- **Maintain template compliance** for similar note types
- **Regular cleanup** of unused metadata fields

### **Performance Optimization**
- **Process during off-hours** for large vaults
- **Use incremental operations** rather than full-vault processing
- **Monitor file system** for conflicts between Cursor and Obsidian
- **Optimize search indices** after major reorganizations

## 🔧 Troubleshooting

### **Common Issues**

**Obsidian Can't Find Files:**
- Ensure consistent file naming (no special characters)
- Check for case sensitivity issues
- Verify WikiLink format compliance

**Git Conflicts:**
- Always close Obsidian before major Git operations
- Use `.gitignore` for cache and config files
- Commit frequently with descriptive messages

**Performance Issues:**
- Exclude large binary files from processing
- Use `--dry-run` for testing operations
- Process subfolders individually for very large vaults

### **Emergency Recovery**
```bash
# If something goes wrong, restore from Git
git status                    # Check what changed
git checkout -- filename.md  # Restore specific file
git reset --hard HEAD~1      # Restore to previous commit (careful!)
```

## 📚 Additional Resources

- `cursor-rules-obsidian.md` - Complete Cursor rules template
- `vault-analytics.py` - Scripts for vault analysis
- `migration-tools/` - Format conversion utilities
- `templates/` - Standard note templates

## 🎉 Benefits of This Workflow

### **For Individual Users**
- **Massive time savings** on repetitive tasks
- **Professional quality** output
- **Consistent formatting** across entire vault
- **Advanced search** and analysis capabilities

### **For Teams**
- **Standardized workflows** across team members
- **Version control** for collaborative knowledge bases
- **Quality assurance** for shared documentation
- **Professional deliverables** from team knowledge

---

**Remember**: This workflow is about leveraging the strengths of both tools. Use Obsidian for what it does best (note-taking, linking, exploration) and Cursor for what it excels at (bulk operations, advanced editing, automation). 