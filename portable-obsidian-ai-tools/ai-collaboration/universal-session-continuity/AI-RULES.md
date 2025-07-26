<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the AI-RULES template open. Would you like me to help you customize these rules for your specific project? I'll ask about your project requirements, safety needs, and collaboration preferences to create tailored AI behavior rules.

Say 'yes' to start the interview, or 'skip' if you want to customize manually."

INTERVIEW QUESTIONS TO ASK:
1. "What type of project is this and what are the main file types/formats to preserve?" (customizes safety rules)
2. "What are your most important quality and safety requirements?" (tailors code standards)
3. "How do you prefer to receive feedback and communicate?" (customizes collaboration rules)
4. "What are your main problem-solving approaches for this project?" (adjusts problem-solving standards)
5. "What does success look like for this project?" (defines success criteria)
6. "Any specific tools, workflows, or constraints I should know about?" (customizes tool-specific rules)

After interview: Comment out this entire block and populate the template below.
-->

# AI Rules - [PROJECT NAME]

*Core rules that govern AI assistant behavior in this project*

## Safety Rules (Non-Negotiable)

### Code Safety
- **NEVER modify [CRITICAL FUNCTIONALITY]** without implementing backup functionality
- **ALWAYS test [PROJECT TYPE] changes** with dry-run modes when available
- **PRESERVE all [PROJECT-SPECIFIC FORMATS]**, [KEY FILE TYPES], and [IMPORTANT REFERENCES]
- **VALIDATE [INPUT TYPES]** use relative resolution, never hardcoded absolute paths

### Security Requirements
- **No hardcoded personal information** or filesystem paths
- **All destructive operations** must have --no-backup option for advanced users
- **Validate inputs**, especially [PROJECT-SPECIFIC INPUT TYPES] and user-provided data
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
"[LONG TIMELINE] timeline" → CHALLENGE IMMEDIATELY → "Could we do this [SHORTER PERIOD]?"
"This will take [TIME PERIOD]" → QUESTION COMPLEXITY → "Simplest version that works?"
"Complex [PROJECT TYPE]" → BIAS TOWARD ITERATION → "Start with basics, build up"

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
- **[SCRIPT TYPE] scripts**: Use [YOUR SAFETY STANDARDS], include proper error handling
- **[CODE TYPE] scripts**: Include dependency checks, handle [DATA TYPE] properly
- **All [PROJECT] scripts**: Include backup integration from [YOUR BACKUP SYSTEM]
- **Comments**: Explain [CRITICAL SECTIONS] and complex [PROJECT-SPECIFIC] patterns

### Documentation Standards
- **Keep session-continuity/ documents updated** when making significant changes
- **Update [YOUR PROJECT PLAN]** when completing tasks or discovering issues
- **Maintain before/after examples** in [YOUR EXAMPLES FOLDER] when adding new functionality
- **Use consistent [YOUR FORMATTING STYLE]** formatting

## Collaboration Rules

### Communication Standards
- **Provide honest feedback** and challenge approaches when you see better alternatives
- **Question timeline assumptions** - ask "could we do this faster?" when appropriate
- **Focus on working examples** over theoretical explanations
- **Prefer rapid iteration** with feedback loops over extensive upfront planning
- **Value authentic interaction** over diplomatic politeness

### Problem-Solving Standards
- **Use "[YOUR PROBLEM-SOLVING METHOD]"** - listen for user expertise about likely root causes
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
- **[YOUR BACKUP SYSTEM] systems** function correctly
- **[YOUR COMPATIBILITY REQUIREMENTS]** maintained
- **Documentation enables** independent usage
- **Tools transform complex [YOUR DOMAIN] workflows** into simple, reliable processes

---

## 📋 **Template Customization Guide:**

### **Universal Placeholders to Replace:**
- `[PROJECT NAME]` - Your actual project name
- `[CRITICAL FUNCTIONALITY]` - Most important features to preserve (e.g., backup systems, data integrity)
- `[PROJECT-SPECIFIC FORMATS]` - Key formats to preserve (e.g., YAML frontmatter, specific file types)
- `[KEY FILE TYPES]` - Important file types in your project
- `[IMPORTANT REFERENCES]` - Critical references to maintain (e.g., links, IDs, citations)
- `[PROJECT-SPECIFIC INPUT TYPES]` - Types of inputs your project handles
- `[LONG TIMELINE]` / `[SHORTER PERIOD]` - Timeline expectations for your domain
- `[YOUR SAFETY STANDARDS]` - Your specific safety requirements
- `[YOUR BACKUP SYSTEM]` - Your backup and recovery approach
- `[YOUR PROBLEM-SOLVING METHOD]` - Your preferred problem-solving approach

### **Domain-Specific Rule Examples:**

#### **Software Development:**
```
### Code Safety
- **NEVER modify production deployment scripts** without implementing rollback functionality
- **PRESERVE all API contracts**, database schemas, and configuration files
- **VALIDATE all user inputs** for security vulnerabilities

### Quality Rules
- **Follow PEP 8 for Python**, ESLint for JavaScript, include comprehensive tests
- **All deployment scripts**: Include rollback procedures and monitoring
```

#### **Content Creation:**
```
### Content Safety  
- **NEVER modify published content** without creating versioned backups
- **PRESERVE all citation formats**, metadata, and cross-references
- **VALIDATE all links** and media references before publication

### Quality Rules
- **Style guides**: Follow AP style, include readability scores
- **All content**: Include SEO optimization and accessibility checks
```

#### **Research Projects:**
```
### Data Safety
- **NEVER modify raw data files** without implementing audit trails
- **PRESERVE all statistical analyses**, methodology notes, and data lineage
- **VALIDATE all data transformations** with checksums and validation rules

### Quality Rules
- **Research standards**: Follow APA citation, include reproducibility documentation
- **All analyses**: Include statistical validation and peer review processes
```

### **Creating Custom Rules:**
Use this template for domain-specific rules:
```
### [YOUR DOMAIN] Specific Rules
- **[SAFETY REQUIREMENT]**: [Specific protection needed]
- **[QUALITY STANDARD]**: [Specific quality criteria]
- **[COLLABORATION PREFERENCE]**: [How you like to work]
```

*These rules ensure consistent, safe, and effective AI collaboration across all sessions and collaborators for [PROJECT NAME].* 