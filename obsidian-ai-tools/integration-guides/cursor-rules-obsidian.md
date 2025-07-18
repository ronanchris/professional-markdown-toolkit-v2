# Cursor Rules for Obsidian Vault Management

Copy these rules to your Obsidian vault's `.cursorrules` file to ensure AI-assisted editing respects Obsidian's syntax and conventions.

## Obsidian Syntax Preservation Rules

### YAML Frontmatter
- Always preserve existing YAML frontmatter structure and content
- Use consistent date format: YYYY-MM-DD for all date fields
- Standard frontmatter fields: title, tags, created, modified, aliases
- Never remove metadata without explicit user instruction
- When adding new frontmatter, place at the very top of the file
- Use proper YAML syntax with `---` delimiters

### WikiLinks and References
- Preserve WikiLink format: `[[note-name]]` and `[[note-name|display-text]]`
- Maintain block references: `[[note-name#heading]]` and `[[note-name^block-id]]`
- Keep embed syntax intact: `![[image.png]]`, `![[note-name]]`, `![[note-name#heading]]`
- Preserve section links: `[[note-name#Section Title]]`
- Never convert WikiLinks to standard markdown links unless explicitly requested

### Tags and Organization
- Preserve tag formats: `#tag`, `#nested/tag`, `#multi-level/nested/tag`
- Maintain tag hierarchy and nesting structure
- Keep inline tags within content
- Preserve hashtag-style tags in frontmatter YAML: `tags: [tag1, tag2]`

### Obsidian-Specific Syntax
- Preserve callouts: `> [!note]`, `> [!warning]`, `> [!tip]`, etc.
- Keep math blocks: `$$math$$` and `$inline math$`
- Maintain code blocks with proper language tagging
- Preserve Obsidian comments: `%%hidden comment%%`
- Keep Dataview queries intact: `` ```dataview `` blocks
- Preserve Templater syntax: `<%tp.date.now()%>`, `{{title}}`, etc.

### Content Structure Rules
- Never modify heading hierarchy without explicit instruction
- Preserve bullet point and numbered list formatting
- Maintain table structure and formatting
- Keep horizontal rules (`---`) that separate content sections
- Preserve line breaks and paragraph spacing that affects readability

## Safety and Quality Rules

### Content Preservation
- Never modify the meaning or substance of content, only formatting
- Preserve all internal and external links
- Keep all embedded content and attachments references
- Maintain voice, tone, and writing style
- Never remove or significantly alter user-created content

### Formatting Standards
- Use consistent markdown formatting throughout
- Clean up extra whitespace but preserve intentional spacing
- Ensure proper heading hierarchy (no skipped levels)
- Standardize list formatting (consistent bullet styles)
- Fix malformed markdown while preserving intent

### Metadata Management
- Add missing standard frontmatter fields when beneficial
- Standardize date formats across all frontmatter
- Clean up duplicate or conflicting metadata
- Suggest tag standardization for consistency
- Maintain template compatibility

## Bulk Operation Guidelines

### Multi-File Operations
- When processing multiple files, maintain consistency across the vault
- Preserve folder structure and file organization
- Apply changes uniformly while respecting individual file contexts
- Report significant changes or potential issues
- Suggest backup before major bulk operations

### Template Application
- When applying templates, merge with existing frontmatter intelligently
- Preserve unique content while standardizing format
- Maintain compatibility with Obsidian plugins (Templater, etc.)
- Respect existing note structure and organization

### Quality Assurance
- Check for broken internal links after modifications
- Ensure YAML frontmatter is valid and properly formatted
- Verify that all Obsidian syntax remains functional
- Test that modified notes open correctly in Obsidian
- Report any potential compatibility issues

## Git and Version Control

### Commit Guidelines
- Generate descriptive commit messages for changes
- Group related changes into logical commits
- Exclude Obsidian cache and config files from commits
- Suggest meaningful commit messages that describe the scope of changes

### Collaboration
- Maintain compatibility with team workflows
- Preserve shared templates and conventions
- Respect established folder structures and naming conventions
- Document significant changes for team members

## Performance Considerations

### Large Vault Optimization
- Process files incrementally for very large vaults (10,000+ files)
- Suggest efficient operation sequencing
- Avoid operations that might cause Obsidian sync conflicts
- Recommend closing Obsidian during major bulk operations

### Resource Management
- Handle large files efficiently (long notes, embedded content)
- Suggest optimal processing order for related files
- Monitor for potential file system conflicts
- Recommend appropriate backup strategies

## Error Handling and Recovery

### Graceful Failures
- Always provide clear error messages with specific file names
- Suggest specific fixes for common Obsidian syntax issues
- Offer rollback options for bulk operations
- Preserve file integrity even when operations fail

### Recovery Procedures
- Guide users through Git-based recovery when needed
- Suggest manual verification steps after automated changes
- Provide clear instructions for fixing corrupted files
- Recommend validation steps to ensure Obsidian compatibility

---

## Usage Instructions

1. **Copy these rules** to a `.cursorrules` file in your Obsidian vault root
2. **Customize** any specific conventions for your vault
3. **Test** on a small subset of files before bulk operations
4. **Backup** your vault before major changes
5. **Verify** changes work correctly in Obsidian after processing

## Additional Considerations

### Plugin Compatibility
- These rules are designed to work with popular Obsidian plugins
- Test compatibility with your specific plugin setup
- Report any issues with particular plugin syntaxes
- Consider plugin-specific rules for specialized workflows

### Custom Workflows
- Adapt these rules to your specific vault organization
- Add rules for custom templates or naming conventions
- Include project-specific metadata standards
- Modify for team collaboration requirements

**Remember**: These rules ensure that AI-assisted editing enhances your Obsidian workflow without breaking the tools and conventions that make Obsidian powerful. 