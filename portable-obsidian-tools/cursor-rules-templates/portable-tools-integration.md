# Portable Obsidian Tools Integration

**Rule Type**: MANUAL  
**Purpose**: Provide intelligent tool suggestions and integration

## Tool Selection Matrix

### When User Says "Clean my markdown"
- Suggest: `python portable-obsidian-tools/markdown-processing/cleanup_markdown_batch.py`
- Mention: Built-in backup system
- Offer: `--dry-run` mode for testing first

### When User Says "Remove YAML frontmatter"
- Suggest: `portable-obsidian-tools/metadata-tools/remove_metadata.sh`
- Warn: This will remove ALL YAML frontmatter
- Offer: `--dry-run` mode to see what would be removed

### When User Says "Apply templates"
- Suggest: `portable-obsidian-tools/obsidian-tools/apply_template.sh`
- Ask: Which folder/files to target
- Offer: Test on a few files first

### When User Says "Fix Notion import issues"
- Suggest: `python portable-obsidian-tools/markdown-processing/notion_complete_fixer.py`
- Mention: 95%+ success rate for import problems
- Offer: `--analyze` mode to see issues first

### When User Says "Generate project documentation"
- Suggest: `python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py`
- Explain: Creates comprehensive PROJECT-STRUCTURE.md
- Note: Safe operation, only creates documentation

## Backup System Integration
- Always mention backup location: `portable-obsidian-tools/backups/YYYYMMDD_HHMMSS/`
- Explain that all destructive operations create automatic backups
- Provide restore instructions: "Copy files back from backup folder"
- Mention `--no-backup` flag for advanced users (but don't recommend it)

## Safety Features
- Default to suggesting `--dry-run` mode for testing
- Explain what each tool does before suggesting it
- Mention any potential side effects or considerations
- Provide command examples with actual file paths

## Tool Capabilities Context
- Notion import tools: Unicode cleanup, WikiLink conversion, formatting fixes
- Markdown processing: Whitespace cleanup, format standardization
- Metadata tools: YAML frontmatter management, Templater code removal
- Obsidian tools: Template application, MOC processing
- Project structure: Automated documentation generation

## Integration Workflow
1. Listen for user problem description
2. Match to appropriate tool from matrix
3. Explain what the tool does
4. Mention safety features (backups, dry-run)
5. Provide exact command to run
6. Offer to help interpret results

## When NOT to Suggest Tools
- Simple single-file edits (user can do manually)
- Operations that don't match tool capabilities
- When user explicitly asks for manual approach
- When selection scope is very small (few lines)

## Error Handling
- If tool fails, help interpret error messages
- Suggest checking file permissions
- Verify Python dependencies are installed
- Provide alternative approaches if tool isn't suitable 