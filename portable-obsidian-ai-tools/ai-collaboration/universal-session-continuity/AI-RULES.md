# AI Rules - Professional Markdown Toolkit

*Core rules that govern AI assistant behavior in this project*

## Safety Rules (Non-Negotiable)

### Code Safety
- **NEVER modify destructive scripts** without implementing backup functionality
- **ALWAYS test script changes** with dry-run modes when available
- **PRESERVE all YAML frontmatter**, Obsidian embeds ([[links]]), and block references (^block-id)
- **VALIDATE file paths** use relative resolution, never hardcoded absolute paths

### Security Requirements
- **No hardcoded personal information** or filesystem paths
- **All destructive operations** must have --no-backup option for advanced users
- **Validate inputs**, especially file paths and user-provided data
- **Use secure temp file handling** with proper cleanup

## Session Management Rules (Automated)

### Session Start Protocol
- **AUTO-TRIGGER**: Every session start → Check session-continuity/SESSION-PLAN.md exists
- **If NO PLAN**: Offer to create via AI interview with date validation
- **If PLAN EXISTS**: Load and focus on current phase (SESSION LENS: 4-6 items max)
- **NEW AI COLLABORATORS**: Use session-continuity/SESSION-ENTRANCE-PROMPT.md for complete context

### Automatic Monitoring
- **COMPLETION DETECTION**: Auto-check SESSION-PLAN.md when tasks complete
- **DEVIATION MONITORING**: Auto-document when approach changes (with date validation)
- **SESSION END**: Auto-archive to SESSION-PLAN-ARCHIVE/ and update snapshots
- **IMPLEMENTATION GAP DETECTION**: Validate design vs. reality gaps

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

### Timeline Reality Check Rules:
```
"3-week timeline" → CHALLENGE IMMEDIATELY → "Could we do this tonight?"
"This will take hours" → QUESTION COMPLEXITY → "Simplest version that works?"
"Complex project" → BIAS TOWARD ITERATION → "Start with basics, build up"

AUTO-RESPONSE:
1. Question initial complexity assumptions
2. Propose rapid iteration approach
3. Focus on working version first
4. Challenge scope rather than accept it
```

### Expert Intuition Validation Rules:
```
"My first suspicion is..." → VALIDATE HYPOTHESIS FIRST
"I'm not concerned about [obvious issue]" → TRUST DOMAIN EXPERTISE
"This usually happens when..." → TEST SPECIFIC PATTERN

AUTO-RESPONSE:
1. Test user's specific hypothesis before general approaches
2. Don't override domain expertise with technical assumptions
3. Use surgical approach based on expert insight
4. Learn from user corrections and feedback
```

### Payload Tax Management Rules:
```
System design exceeds 2,000 tokens overhead → APPLY SESSION LENS
Comprehensive monitoring creates 50%+ overhead → FOCUS SCOPE
Benefits unclear vs. computational costs → CALCULATE THRESHOLD

AUTO-RESPONSE:
1. Measure actual computational costs, not theoretical
2. Apply session lens approach (4-6 items focus)
3. Calculate critical threshold for net benefit
4. Optimize through intelligent constraint, not comprehensiveness
```

## Quality Rules

### Code Standards
- **Shell scripts**: Use `set -e` and `set -u`, include proper error handling
- **Python scripts**: Include dependency checks, handle encoding properly
- **All scripts**: Include backup integration from shared/backup-functions.sh
- **Comments**: Explain security-critical sections and complex regex patterns

### Documentation Standards
- **Keep session-continuity/ documents updated** when making significant changes
- **Update PROJECT-SECURITY-PLAN.md** when completing tasks or discovering issues
- **Maintain before/after examples** in docs/examples/ when adding new functionality
- **Use consistent markdown formatting** (headings with spaces: `# Heading`)

## Collaboration Rules

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

## Success Criteria Rules

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

*These rules ensure consistent, safe, and effective AI collaboration across all sessions and collaborators.* 