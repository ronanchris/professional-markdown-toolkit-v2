<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the AI-COLLABORATION template open. Would you like me to help you set up AI collaboration guidelines for your project through a quick interview? I'll ask you about your communication preferences, how you like to work with AI assistants, and which tools you'll be using most.

Say 'yes' to start the interview, or 'skip' if you want to customize it manually."

INTERVIEW QUESTIONS TO ASK:
1. How do you prefer to communicate with AI assistants? (Direct/diplomatic, rapid iteration/careful planning)
2. Which Obsidian tools will you be using most? (This helps set up tool-specific guidance)
3. Do you want session continuity features? (Auto-completion tracking, progress monitoring)
4. What's your experience level with these tools? (Helps set explanation depth)
5. Any specific collaboration preferences or things that frustrate you about AI?

After interview: Comment out this entire block and populate the template below.
-->

# AI Collaboration Guidelines
*Instructions for AI assistants working with this project and toolkit*

## 🎯 **Project Context**
**Project Name**: [PROJECT NAME]
**Primary Tools**: [List main Obsidian tools being used]
**User Experience Level**: [Beginner/Intermediate/Advanced with these tools]
**Session Continuity**: [Enabled/Basic/Disabled - affects AI behavior]

## 🤝 **Communication Preferences**

### **User Communication Style**
- **Feedback Style**: [Direct and honest / Diplomatic / Encouraging]
- **Pace Preference**: [Rapid iteration / Careful planning / Mixed approach]
- **Detail Level**: [High detail explanations / Brief and focused / Contextual]
- **Challenge Level**: [Challenge assumptions / Supportive guidance / Follow lead]

### **AI Response Guidelines**
- **Tool Recommendations**: [Always suggest specific tools / Ask what to use / User will specify]
- **Error Handling**: [Explain errors fully / Provide quick fixes / Ask user preference]
- **Progress Tracking**: [Automatic updates / Manual prompts / User-driven only]
- **Documentation**: [Update templates automatically / Ask before updating / User maintains]

## 🛠️ **Tool Usage Guidelines**

### **Notion Import Tools**
**When to Recommend:**
- User mentions import problems, Unicode issues, or WikiLink errors
- Files won't import into Notion or other platforms
- Complex formatting causing issues

**AI Behavior:**
- **Always start with**: `notion_complete_fixer.py` for comprehensive fixes
- **For specific issues**: Recommend targeted tools (unicode_cleaner.py, wikilink_converter.py)
- **Testing approach**: [Always use --dry-run first / User preference / Skip dry-run for experienced users]
- **Backup reminder**: [Always remind about backups / Assume user knows / Check if backup system working]

### **Metadata Management Tools**
**When to Recommend:**
- YAML frontmatter issues or inconsistencies
- Template integration problems
- Batch metadata operations needed

**AI Behavior:**
- **Safety first**: Always recommend `safe_metadata_removal.py --dry-run` before batch operations
- **Scope checking**: Ask about target files/folders before running batch operations
- **Integration awareness**: Consider impact on templates and existing workflows
- **Progress tracking**: [Update session plan automatically / Ask user / Track manually]

### **Template Management Tools**
**When to Recommend:**
- Template application or fixes needed
- Standardizing document structure
- Obsidian template integration

**AI Behavior:**
- **Template preservation**: Always check if user wants to preserve existing content
- **Batch vs individual**: Ask about scope for multiple files
- **Testing strategy**: [Test on single file first / User experienced with tools / Full batch okay]

### **Markdown Processing Tools**
**When to Recommend:**
- Formatting inconsistencies
- Batch cleanup needed  
- Professional formatting required

**AI Behavior:**
- **Scope awareness**: Ask about recursive processing for directories
- **Quality standards**: [Always use --verbose for feedback / User prefers quiet / Ask preference]
- **Verification**: [Always check results / User will verify / Trust tool output]

## 📋 **Session Continuity Behavior**

### **Session Start Protocol**
```
IF session-continuity enabled:
1. Check for existing 02-SESSION-PLAN.md
2. If no plan: Offer to create via interview
3. If plan exists: Load current focus (4-6 items max)
4. Summarize current status and ask how to proceed

IF session-continuity disabled:
1. Simple greeting and readiness check
2. Ask about current goals
3. Proceed with tool usage as needed
```

### **Progress Tracking**
- **Auto-completion detection**: [Enabled - monitor for "That's complete" / Disabled / Ask user preference]
- **Plan updates**: [Automatic when major progress / Manual prompts / User-driven only]
- **Deviation tracking**: [Auto-detect approach changes / Simple logging / User decides]

### **Session End Protocol**  
- **Progress summary**: [Automatic session wrap-up / Ask if user wants summary / Skip unless requested]
- **Next session preparation**: [Update current state automatically / Brief notes only / User handles]

## 🔧 **Tool Integration Patterns**

### **Typical Workflow Patterns**
**Notion Import Project:**
```
1. Start with session plan (if enabled)
2. Identify problematic files
3. Run notion_complete_fixer.py with --dry-run
4. Process files and verify results
5. Update progress (manual or automatic)
```

**Metadata Standardization:**
```
1. Plan scope and backup strategy
2. Use safe_metadata_removal.py --dry-run to understand scope
3. Apply fix_metadata.sh for standard fixes
4. Verify results and document patterns
5. Track completion
```

**Template Application:**
```
1. Identify target files and template needs
2. Test apply_template.sh on single file first
3. Batch process if successful
4. Verify template integration
5. Document results
```

## 🚨 **Safety & Error Handling**

### **Critical Safety Rules**
- **NEVER skip backups** unless user explicitly requests --no-backup
- **ALWAYS use --dry-run** for first-time tool usage (unless user experienced)
- **VERIFY file paths** are relative and correct before batch operations
- **CHECK dependencies** if tools fail (requirements.txt current?)

### **Error Response Protocol**
1. **Immediate safety check**: Is user data at risk?
2. **Error explanation**: Clear description of what went wrong  
3. **Recovery options**: How to fix or restore from backup
4. **Prevention**: How to avoid this error in future

### **User Experience Standards**
- **Tool recommendations**: Include brief explanation of what tool does
- **Command examples**: Always show actual command with options
- **Success verification**: Explain how user can confirm tool worked correctly
- **Next steps**: Clear guidance on what to do after tool completes

## 📊 **Quality Standards**

### **Tool Usage Quality**
- **Appropriate tool selection**: Right tool for the specific problem
- **Proper command options**: Use correct flags and parameters
- **Safety measures**: Backups and dry-runs when appropriate
- **Result verification**: Help user confirm tools worked correctly

### **Communication Quality**
- **Clear explanations**: User understands what tools do and why
- **Honest feedback**: Acknowledge when approaches don't work
- **Progress awareness**: User knows current status and next steps
- **Learning capture**: [Document insights for future sessions / Basic notes / User preference]

## 🎯 **Success Criteria**

### **Technical Success**
- Tools work reliably for user's specific needs
- No data loss or corruption incidents
- Efficient tool usage with minimal repetition
- User feels confident using tools independently

### **Collaboration Success**
- User gets helpful guidance without micromanagement
- Communication style matches user preferences
- Progress tracking works smoothly (when enabled)
- Both parties contribute effectively to problem-solving

## 💡 **Customization Notes**

### **For Experienced Users:**
- Reduce explanation depth for familiar tools
- Skip confirmation steps for routine operations
- Focus on advanced techniques and optimizations
- Enable more autonomous behavior

### **For New Users:**
- Provide detailed explanations for each tool
- Always use safety measures (dry-run, backups)
- Confirm understanding before proceeding
- Document learning for future reference

### **For Complex Projects:**
- Enable full session continuity features
- Track tool usage patterns and effectiveness
- Document workflow optimizations discovered
- Plan tool integration strategies

### **For Simple Tasks:**
- Disable session continuity overhead
- Focus on immediate tool usage
- Minimal documentation and tracking
- Direct, efficient tool recommendation

---

## 📋 **Template Usage Instructions**

1. **Copy this template** to `04-AI-COLLABORATION-GUIDE.md` in your project
2. **Customize the bracketed sections** based on your preferences and project needs
3. **Test with AI assistant** to ensure guidelines work as expected
4. **Adjust over time** based on what works well and what doesn't
5. **Share with team** if multiple people will be using the tools

**Integration with Tools**: This template works alongside all existing Obsidian tools without requiring any changes to the tools themselves. It simply provides guidance for how AI assistants should recommend and use the tools. 