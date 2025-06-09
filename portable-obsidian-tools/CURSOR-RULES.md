# Cursor Rules for Portable Obsidian Tools

**Copy the following rules to your project's .cursorrules file or Cursor settings:**

```markdown
## Obsidian Tools Integration

- This project has portable Obsidian tools in `portable-obsidian-tools/` folder
- Use these tools for all Obsidian markdown cleanup and template operations
- All scripts have built-in backup systems - explain safety to user before running
- Reference `portable-obsidian-tools/AI-INTEGRATION-GUIDE.md` for detailed AI instructions

### Tool Selection Matrix:
- YAML/frontmatter cleanup → `portable-obsidian-tools/metadata-tools/remove_metadata.sh`
- Template application → `portable-obsidian-tools/obsidian-tools/apply_template.sh` 
- MOC file processing → `python portable-obsidian-tools/obsidian-tools/apply_moc_template_preserve_metadata.py`
- Testing changes → Add `--dry-run` flag to Python scripts
- Advanced users → Add `--no-backup` flag to skip backups

### Safety Protocol:
1. Always mention automatic backup system to user
2. Offer dry-run mode for testing when available  
3. Provide restore instructions after destructive operations
4. Confirm vault structure exists before running tools

### Common Commands:
```bash
# Most common operations
portable-obsidian-tools/metadata-tools/remove_metadata.sh
portable-obsidian-tools/obsidian-tools/apply_template.sh
python portable-obsidian-tools/obsidian-tools/apply_inbox_template.py --dry-run
```

### Dependencies:
- Python 3.7+ with PyYAML (install: `cd portable-obsidian-tools && pip install -r requirements.txt`)
- Bash shell for .sh scripts
- Obsidian vault structure with folders like `0-inbox/`, `00-MOCs/`
```

---

## Quick Integration Steps:

1. **Copy this entire rule block** to your project's Cursor configuration
2. **Reference the AI Integration Guide** when helping users with Obsidian tasks  
3. **Use the exact commands** provided in the tool selection matrix
4. **Always explain the backup system** to make users feel safe 