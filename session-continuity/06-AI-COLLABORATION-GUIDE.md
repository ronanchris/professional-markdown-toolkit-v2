# AI Collaboration Guide - Professional Markdown Toolkit

*Comprehensive instructions and rules for AI assistant behavior in this project*

## 🚨 Safety Rules (Non-Negotiable)

### Code Safety Requirements
- **NEVER modify destructive scripts** without implementing backup functionality
- **ALWAYS test script changes** with dry-run modes when available
- **PRESERVE all YAML frontmatter**, Obsidian embeds ([[links]]), and block references (^block-id)
- **VALIDATE file paths** use relative resolution, never hardcoded absolute paths

### Security Requirements
- **No hardcoded personal information** or filesystem paths
- **All destructive operations** must have --no-backup option for advanced users
- **Validate inputs**, especially file paths and user-provided data
- **Use secure temp file handling** with proper cleanup

## 🔄 Session Management Protocol

### Session Start Instructions
1. **Always check 02-SESSION-PLAN.md first** for current goals
2. **Load 01-PROJECT-REQUIREMENTS.md** for overall context
3. **Reference 03-CURRENT-STATE-SNAPSHOT.md** for current status
4. **Review 04-README-FOR-FUTURE-AI.md** for project context
5. **Apply session lens approach** - focus on 4-6 items maximum

### Automated Session Rules
- **AUTO-TRIGGER**: Every session start → Check session-continuity/SESSION-PLAN.md exists
- **If NO PLAN**: Offer to create via AI interview with date validation
- **If PLAN EXISTS**: Load and focus on current phase (SESSION LENS: 4-6 items max)
- **NEW AI COLLABORATORS**: Use 05-SESSION-ENTRANCE-PROMPT.md for complete context

### Trigger Monitoring
- **Monitor for completion phrases** automatically: "That's complete", "We've finished X"
- **Monitor for deviation phrases**: "Actually, let's...", "Change of plan..."
- **Update documentation** when making significant changes
- **Validate dates** to prevent timestamp errors

## 💻 Code Modification Instructions

### Development Standards
1. **Never remove backup functionality** without explicit user request
2. **Preserve YAML frontmatter** and Obsidian embeds ([[links]])
3. **Test changes with dry-run modes** when available
4. **Include comprehensive error handling** in all scripts
5. **Maintain cross-platform compatibility** (macOS, Linux, WSL)

### Code Quality Requirements
- **Shell scripts**: Use `set -e` and `set -u`, include proper error handling
- **Python scripts**: Include dependency checks, handle encoding properly
- **All scripts**: Include backup integration from shared/backup-functions.sh
- **Comments**: Explain security-critical sections and complex regex patterns

## 📝 Documentation Instructions

### Update Requirements
1. **Keep session continuity documents updated** when making significant changes
2. **Update 03-CURRENT-STATE-SNAPSHOT.md** when completing tasks or discovering issues
3. **Maintain before/after examples** in docs/examples/ when adding new functionality
4. **Use consistent markdown formatting** (headings with spaces: `# Heading`)

### Documentation Standards
- **Professional-grade error messages** with recovery instructions
- **Comprehensive help text** for all scripts
- **Cross-platform compatibility** maintained
- **Enterprise-ready backup and logging systems

## 🤝 Collaboration Instructions

### Communication Standards
- **Provide honest feedback** and challenge approaches when you see better alternatives
- **Question timeline assumptions** - ask "could we do this faster?" when appropriate
- **Focus on working examples** over theoretical explanations
- **Prefer rapid iteration** with feedback loops over extensive upfront planning
- **Value authentic interaction** over diplomatic politeness

### Problem-Solving Standards
- **Use "surgical approach"** - listen for user expertise about likely root causes
- **Test specific hypotheses** rather than trying to fix everything at once
- **Validate solutions** with real user data/scenarios, not artificial examples
- **Break complex problems** into testable components
- **Think beyond immediate problem** to reusable solutions when appropriate

## 🎯 Success Criteria

### Technical Success
- **Real progress** on actual user problems
- **Solutions work reliably** in practice
- **Efficient collaboration** without repetitive explanations
- **Both parties feel challenged** and engaged (not just served/serving)
- **Continuous improvement** in working relationship and results

### System Success
- **Backup and restore systems** function correctly
- **Cross-platform compatibility** maintained
- **Documentation enables** independent usage
- **Tools transform complex workflows** into simple, reliable processes

---

*This guide ensures consistent, safe, and effective AI collaboration across all sessions and collaborators.* 