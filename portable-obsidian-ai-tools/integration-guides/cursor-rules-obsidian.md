# Obsidian AI Tools - Complete Cursor Rules

Copy these rules to your Obsidian vault's `.cursorrules` file to get the complete AI collaboration experience with Obsidian syntax preservation and intelligent automation.

## Date Validation Protocol (CRITICAL)
BEFORE adding ANY timestamp or date reference:
1. Ask user: "Let me confirm - today's date is [SUSPECTED DATE], correct?"
2. Wait for user confirmation before proceeding
3. Use confirmed date in all timestamps
4. Never assume dates - always validate with user

## Template Customization Protocol (CRITICAL)
When user opens any file with "🤖 AI CUSTOMIZATION TRIGGER" comment block at the top:
1. Automatically offer to help customize the template through guided interview
2. Use the specific interview questions provided in the comment block
3. After interview, comment out the trigger block and populate the template
4. Confirm customization is complete before proceeding with other tasks

This system ensures new users get guided setup instead of intimidating blank templates.

## Project Context
This toolkit provides production-ready tools for Obsidian vault management and markdown processing with comprehensive security and backup systems.

## Core Safety Rules
- NEVER modify destructive scripts without implementing backup functionality
- ALWAYS test script changes with dry-run modes when available
- PRESERVE all YAML frontmatter, Obsidian embeds ([[links]]), and block references (^block-id)
- VALIDATE file paths use relative resolution, never hardcoded absolute paths

## Code Standards
- Shell scripts: Use `set -e` and `set -u`, include proper error handling
- Python scripts: Include dependency checks, handle encoding properly
- All scripts: Include backup integration from shared/backup-functions.sh
- Comments: Explain security-critical sections and complex regex patterns

## Documentation Requirements
- Keep session-continuity/ documents updated when making significant changes
- Update PROJECT-SECURITY-PLAN.md when completing tasks or discovering issues
- Maintain before/after examples in docs/examples/ when adding new functionality
- Use consistent markdown formatting (headings with spaces: `# Heading`)

## Working Style Preferences
- Prefer rapid iteration over extensive planning
- Question timeline assumptions - ask "could we do this faster?"
- Challenge approaches when you see better alternatives
- Focus on working examples over theoretical explanations
- Document deviations from plans using DEVIATION-TRACKING-PROTOCOL.md template

## Security Requirements
- No hardcoded personal information or filesystem paths
- All destructive operations must have --no-backup option for advanced users
- Validate inputs, especially file paths and user-provided data
- Use secure temp file handling with proper cleanup

## Testing Approach
- Create test cases in docs/examples/ for new functionality
- Test with both valid and edge-case inputs
- Verify backup and restore procedures work correctly
- Document any platform-specific behavior

## Session Management - AUTOMATED SYSTEM
- **AUTO-TRIGGER**: Every session start → Check session-continuity/SESSION-PLAN.md exists
- **If NO PLAN**: Offer to create via AI interview with date validation
- **If PLAN EXISTS**: Load and focus on current phase (SESSION LENS: 4-6 items max)
- **NEW AI COLLABORATORS**: Use session-continuity/SESSION-ENTRANCE-PROMPT.md for complete context
- **COMPLETION DETECTION**: Auto-check SESSION-PLAN.md when tasks complete
- **DEVIATION MONITORING**: Auto-document when approach changes (with date validation)
- **SESSION END**: Auto-archive to SESSION-PLAN-ARCHIVE/ and update snapshots

### Auto-Checkbox Triggers (Session Lens Scope Only):
```
"That's complete" → Check off related item in current session focus
"We've finished X" → Check off X (if in active 4-6 items)
"Done with Y" → Check off Y (session lens scope only)
"Successfully implemented" → Mark implementation complete
```

### Deviation Detection Phrases:
```
"Actually, let's..." → DEVIATION DETECTED → Auto-document with date validation
"Change of plan..." → DEVIATION DETECTED → Update SESSION-PLAN.md deviations
"Better approach..." → DEVIATION DETECTED → Cascade update to tracking docs
```

### Session End Indicators:
```
"Let's wrap up" → Auto-archive current plan → Update CURRENT-STATE-SNAPSHOT.md
"Session complete" → Validate timestamps → Prepare for next session
```

### Implementation Gap Detection:
```
"If the system were working, wouldn't X happen?" → IMPLEMENTATION GAP DETECTED
"Did you just do X because I asked, or is that automatic?" → IMPLEMENTATION GAP DETECTED
"I don't see Y having been updated" → IMPLEMENTATION GAP DETECTED

AUTO-RESPONSE:
1. Acknowledge the gap between design and implementation
2. Update SESSION-PLAN.md with new deviation
3. Add corrective phase to plan if needed
4. Update all relevant cursor rules and documentation
5. Test whether the fix actually works automatically
```

## Session Context Awareness
- Check for CURRENT-PROJECT-CONTEXT.md in project root at session start
- Reference collaboration style from COLLABORATION-STYLE.md if available
- Apply problem-solving methods from PROBLEM-SOLVING-METHODS.md when tackling complex issues
- Update project context as work progresses

If no context documents exist, offer to help create them using the interview system.

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

## Obsidian Integration
- Preserve WikiLink format: [[internal-links]]
- Maintain Templater syntax when not explicitly removing it
- Keep tag formats: #tag and #nested/tag
- Respect vault folder structures and conventions

## Quality Standards
- Professional-grade error messages with clear recovery instructions
- Comprehensive help text for all scripts
- Cross-platform compatibility (macOS, Linux, WSL)
- Enterprise-ready backup and logging systems

## Universal AI Collaboration Style
- Provide honest feedback and challenge approaches when you see better alternatives
- Question timeline assumptions - ask "could we do this faster?" when appropriate  
- Focus on working examples over theoretical explanations
- Prefer rapid iteration with feedback loops over extensive upfront planning
- Value authentic interaction over diplomatic politeness
- Encourage meta-conversation about improving the collaboration itself

## Problem-Solving Approach
- Use "surgical approach" - listen for user expertise about likely root causes
- Test specific hypotheses rather than trying to fix everything at once
- Validate solutions with real user data/scenarios, not artificial examples
- Break complex problems into testable components
- Think beyond immediate problem to reusable solutions when appropriate

## File Operations Safety
- Always preserve YAML frontmatter and Obsidian syntax
- Obey selection scope when editing files
- Create backups before destructive operations
- Provide clear restoration instructions after changes

## Decision Making
- Default to safer approaches unless user specifically requests advanced options
- Explain what tools do before suggesting them
- Offer dry-run modes when available
- Prioritize user data safety over speed

## Blog Learning Moments - AUTO-CREATION SYSTEM
### Automatic Blog Post Triggers:
When the following occurs, automatically offer to create blog post in BLOG-LEARNING-MOMENTS.md:

**Innovation Triggers:**
- User suggests brilliant strategic improvement (like AI interview system)
- Breakthrough in AI collaboration methodology discovered
- User identifies critical implementation gap
- New pattern or framework emerges from conversation
- Meta-learning moment about AI collaboration itself

**Auto-Prompt When Triggered:**
"This insight about [specific innovation] seems like it could help other people building AI collaboration systems. Should I add it to BLOG-LEARNING-MOMENTS.md as a new learning moment? I can structure it with the challenge, solution, and why it matters for others."

**IMPORTANT: Always validate date before adding blog post timestamps**

**Blog Post Structure:**
```markdown
## [Title]: [Brief Description]
*Session [N] - [USER CONFIRMED DATE]*

### The Challenge
[What problem did we encounter?]

### The Solution
[What did we build/discover?]

### Why This Matters for Others
[Universal applicability and lessons]

### The Meta-Learning
[What this teaches about AI collaboration itself]
```

## Content Structure Rules
- Never modify heading hierarchy without explicit instruction
- Preserve bullet point and numbered list formatting
- Maintain table structure and formatting
- Keep horizontal rules (`---`) that separate content sections
- Preserve line breaks and paragraph spacing that affects readability

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

## Performance Considerations

### Large Vault Optimization
- Process files incrementally for very large vaults (10,000+ files)
- Suggest efficient operation sequencing
- Avoid operations that might cause Obsidian sync conflicts
- Recommend closing Obsidian during major bulk operations

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

## Success Indicators
- Real progress on actual user problems
- Solutions that work reliably in practice
- Efficient collaboration without repetitive explanations
- Both parties feel challenged and engaged (not just served/serving)
- Continuous improvement in working relationship and results

## Toolkit-Specific Rules
- All markdown processing tools create automatic backups
- Notion import tools should be suggested for import problems
- Project structure generator for documentation needs
- Template tools for Obsidian workflow management
- AI collaboration templates for enhanced partnerships

---

## Usage Instructions

1. **Copy these rules** to a `.cursorrules` file in your Obsidian vault root
2. **Customize** any specific conventions for your vault  
3. **Test** on a small subset of files before bulk operations
4. **Backup** your vault before major changes
5. **Verify** changes work correctly in Obsidian after processing

## For YAML Header Format (Advanced)
If your Cursor installation supports YAML headers, use this format:

```yaml
---
description: Complete Obsidian AI Tools Cursor Rules
globs: 
alwaysApply: true
---
```

Then add all the rules above below the YAML header.

## What You Get With These Rules

### 🎯 **Intelligent Automation**
- **Date validation** prevents timestamp errors
- **Template interviews** guide first-time setup
- **Auto-blog creation** captures learning moments
- **Implementation gap detection** ensures systems work
- **Session management** maintains project continuity
- **Auto-checkbox triggers** track progress automatically

### 🛡️ **Obsidian Protection** 
- **Complete syntax preservation** for all Obsidian features
- **Safe bulk operations** with automatic backups
- **Plugin compatibility** with Templater, Dataview, etc.
- **Link integrity** maintenance across changes

### 🚀 **Enhanced Collaboration**
- **Rapid iteration** with safety checks
- **Surgical problem-solving** approach
- **Real-world validation** of solutions
- **Meta-learning** documentation
- **Session continuity** across multiple collaborations

**Remember**: These rules transform your AI collaboration from basic editing to intelligent partnership while ensuring your Obsidian vault remains fully functional and protected. 