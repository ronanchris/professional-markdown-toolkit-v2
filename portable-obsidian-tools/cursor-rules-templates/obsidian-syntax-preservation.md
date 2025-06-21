# Obsidian Syntax Preservation

**Rule Type**: ALWAYS  
**Purpose**: Prevent corruption of Obsidian-specific syntax elements

## WikiLink Formats (CRITICAL - Never Break These)
- Internal links: `[[page-name]]`
- Aliased links: `[[page-name|display text]]`
- Header links: `[[page-name#heading]]`
- Block references: `[[page-name#^block-id]]`
- NEVER convert these to standard markdown links unless explicitly requested

## Obsidian Embeds (Preserve Always)
- Page embeds: `![[page-name]]`
- Image embeds: `![[image.png]]`
- Block embeds: `![[page-name#^block-id]]`
- Partial embeds: `![[page-name#heading]]`

## Templater Syntax (Handle Carefully)
- Template expressions: `` `= this.file.name` ``, `` `= date.now()` ``
- Template code blocks: `<%* ... %>`
- Template inline: `<% ... %>`
- Only remove when user explicitly requests Templater cleanup

## Obsidian-Specific Formatting
- Tags: `#tag`, `#nested/tag` (preserve spacing and format)
- Block references: `^unique-block-id` (never modify these)
- Callouts: `> [!note]`, `> [!warning]`, `> [!info]` etc.
- Dataview queries: ` ```dataview ` (preserve code block syntax)
- Math expressions: `$$math blocks$$` and `$inline math$`

## YAML Frontmatter Rules
- Preserve unless user specifically requests removal
- Common Obsidian fields: aliases, tags, cssclass, publish
- Never modify without explicit user permission
- Use portable-obsidian-tools for safe YAML operations

## Enforcement
- Apply to ALL text editing operations
- Apply to ALL file processing operations
- Apply to ALL search and replace operations
- Override only with explicit user confirmation 