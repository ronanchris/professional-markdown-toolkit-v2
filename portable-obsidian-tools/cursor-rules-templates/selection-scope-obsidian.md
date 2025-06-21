# Selection Scope Rules for Obsidian

**Rule Type**: ALWAYS  
**Purpose**: Respect user selections and prevent unintended changes

## When User Selects Text/Lines
- ONLY modify the selected content
- NEVER auto-expand selection to "fix" adjacent formatting
- NEVER modify content outside the selection boundaries
- Preserve all Obsidian syntax outside selection boundaries

## WikiLink Boundary Handling
- If selection starts/ends within a WikiLink `[[]]`, ask user how to handle
- Options: Modify entire WikiLink, skip WikiLink, or expand selection
- NEVER partially modify WikiLink syntax (would break the link)
- Default to asking rather than making assumptions

## YAML Frontmatter Boundaries
- If selection includes part of YAML frontmatter, ask user to confirm scope
- Options: Include entire frontmatter, exclude frontmatter, or modify selection
- NEVER partially modify YAML (would break the frontmatter)
- Preserve frontmatter delimiter lines (`---`) unless explicitly included

## Block Reference Boundaries
- If selection includes block reference `^block-id`, ask user to confirm
- NEVER partially modify block references (would break the reference)
- Consider the entire line when block references are involved

## Multi-File Selections
- When user selects across multiple files, confirm scope for each file
- Apply same selection rules to each file independently
- Preserve file-specific Obsidian syntax in each file

## Selection Expansion Rules
- ONLY expand selection if user explicitly requests it
- When expanding, respect Obsidian syntax boundaries
- Always show what the new selection would be before applying changes
- Allow user to cancel expansion if it includes unintended content

## Formatting Preservation
- Preserve indentation and spacing outside selection
- Maintain bullet point and numbered list formatting
- Keep table formatting intact when modifying partial tables
- Preserve code block boundaries when editing partial blocks

## Enforcement
- Apply to ALL text editing operations
- Apply to ALL formatting operations
- Apply to ALL search and replace within selections
- Cannot be overridden - selection scope is sacred 