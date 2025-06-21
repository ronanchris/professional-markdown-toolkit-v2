# Obsidian Toolkit Cursor Rules

**Copy the following rules to your project's .cursorrules file or Cursor settings:**

```markdown
## Professional Markdown Toolkit Integration

- This project has portable markdown processing tools in `portable-obsidian-tools/` folder
- Use these tools for Obsidian vault management, Notion import fixes, and universal markdown processing
- All scripts have built-in backup systems - explain safety to user before running
- **Essential Reading**: `portable-obsidian-tools/session-continuity/PROJECT-CONTEXT.md` for project understanding
- **Collaboration Guide**: `portable-obsidian-tools/session-continuity/COLLABORATION-GUIDE.md` for working relationship patterns
- **Technical Reference**: `portable-obsidian-tools/AI-INTEGRATION-GUIDE.md` for detailed commands and responses

### Expanded Tool Selection Matrix:

#### **Obsidian Workflows:**
- YAML/frontmatter cleanup → `portable-obsidian-tools/metadata-tools/remove_metadata.sh`
- Template application → `portable-obsidian-tools/obsidian-tools/apply_template.sh` 
- MOC file processing → `python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py`
- Templater code removal → `portable-obsidian-tools/metadata-tools/remove_metadata.sh`

#### **Notion Import Issues:** ⭐ **NEW**
- Complete Notion import fixing → `python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py`
- Unicode character problems → `python portable-obsidian-tools/markdown-processing/unicode_cleaner.py`
- WikiLink conversion → `python portable-obsidian-tools/markdown-processing/wikilink_converter.py`
- Notion-specific formatting → `python portable-obsidian-tools/markdown-processing/notion_import_fixer.py`

#### **Universal Markdown Processing:**
- Comprehensive formatting cleanup → `python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py`
- Batch whitespace normalization → `portable-obsidian-tools/markdown-processing/clean_all_markdown.sh`
- Cross-platform markdown fixes → Any tool from `markdown-processing/` directory

#### **Testing & Safety:**
- Test before applying → Add `--dry-run` flag to Python scripts
- Analyze Unicode issues → Add `--analyze` flag to `unicode_cleaner.py`
- Advanced users → Add `--no-backup` flag to skip backups

### Problem Recognition Patterns:

#### **When User Says:**
- "Notion won't import" / "Notion import failed" → Use `notion_complete_fixer.py`
- "Unicode errors" / "special characters" / "emojis" → Use `unicode_cleaner.py`
- "WikiLinks won't work" / "[[links]]" → Use `wikilink_converter.py`
- "Clean my markdown" / "format files" → Use `cleanup_markdown_batch.py`
- "Remove YAML" / "frontmatter" → Use `remove_metadata.sh`
- "Apply templates" / "inbox files" → Use `apply_template.sh`

### Safety Protocol:
1. Always mention automatic backup system to user
2. Offer dry-run mode for testing when available  
3. Provide restore instructions after destructive operations
4. Confirm file/folder structure exists before running tools
5. For Notion issues, suggest analysis mode first (`--analyze`)

### Common Command Patterns:

#### **Most Frequent Operations:**
```bash
# Obsidian vault management
portable-obsidian-tools/metadata-tools/remove_metadata.sh
portable-obsidian-tools/obsidian-tools/apply_template.sh

# Notion import fixes (NEW!)
python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py document.md
python portable-obsidian-tools/markdown-processing/unicode_cleaner.py document.md --analyze

# Universal markdown processing
python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py
```

#### **Safe Testing Approach:**
```bash
# Always offer testing first
python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run
python portable-obsidian-tools/markdown-processing/unicode_cleaner.py document.md --analyze
```

### Context Recognition:
- **Obsidian vault** → Use obsidian-tools/ and metadata-tools/
- **Notion import problems** → Use markdown-processing/ Notion tools
- **General markdown cleanup** → Use markdown-processing/ universal tools
- **Mixed workflows** → Can combine tools from different categories

### Dependencies:
- Python 3.7+ with PyYAML (install: `cd portable-obsidian-tools && pip install -r requirements.txt`)
- Bash shell for .sh scripts
- Target files can be anywhere in project (tools work on any file path)

### Success Metrics:
- **Notion import tools**: 95%+ success rate for previously failing documents
- **Unicode cleaning**: Complete emoji and special character normalization
- **Obsidian workflows**: Preserve WikiLinks, YAML frontmatter, and Templater syntax as needed
```

---

## Quick Integration Steps:

1. **Copy this entire rule block** to your project's Cursor configuration
2. **Reference the AI Integration Guide** when helping users with markdown tasks  
3. **Use the exact commands** provided in the expanded tool selection matrix
4. **Always explain the backup system** to make users feel safe
5. **Recognize Notion import issues** and suggest appropriate tools immediately 