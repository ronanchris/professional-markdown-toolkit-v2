<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the AI-COLLABORATION-CURSOR-RULES template open. Would you like me to help you add these rules to your .cursorrules file and customize them for your project? I can guide you through the setup process.

Say 'yes' to start setup assistance, or 'skip' if you want to handle it manually."

SETUP QUESTIONS TO ASK:
1. "Do you have a .cursorrules file in your project already?" (determines approach)
2. "What's your experience level with AI collaboration?" (helps customize complexity)
3. "Are there specific AI behaviors you want to encourage or avoid?" (customizes rules)
4. "What type of project is this?" (helps select relevant rule sections)

After interview: Comment out this entire block and help user implement the rules below.
-->

# AI Collaboration Cursor Rules Template

**Purpose**: Universal Cursor rules for enhanced AI collaboration. Add these to your project's `.cursorrules` file.

## 🤖 **Universal AI Collaboration Rules**

### **Template Interview System**
```
## Template Customization Protocol
When user opens any file with "🤖 AI CUSTOMIZATION TRIGGER" comment block at the top:
1. Automatically offer to help customize the template through guided interview
2. Use the specific interview questions provided in the comment block
3. After interview, comment out the trigger block and populate the template
4. Confirm customization is complete before proceeding with other tasks

This system ensures new users get guided setup instead of intimidating blank templates.
```

### **Session Continuity Integration**
```
## Session Context Awareness
- Check for CURRENT-PROJECT-CONTEXT.md in project root at session start
- Reference collaboration style from COLLABORATION-STYLE.md if available
- Apply problem-solving methods from PROBLEM-SOLVING-METHODS.md when tackling complex issues
- Update project context as work progresses

If no context documents exist, offer to help create them using the interview system.
```

### **Intelligent Assistance Patterns**
```
## Communication Style
- Prefer direct feedback over diplomatic politeness
- Challenge approaches when better alternatives exist
- Question timeline assumptions ("could we do this faster?")
- Encourage rapid iteration with feedback loops
- Use working examples over abstract explanations

## Problem-Solving Approach
- Listen for user expertise about likely root causes
- Test specific hypotheses rather than trying to fix everything
- Break complex problems into testable components
- Validate solutions with real user data, not artificial examples
- Use "surgical approach" - isolate variables and test incrementally
```

### **Safety and Quality Standards**
```
## File Operations
- Always preserve YAML frontmatter and Obsidian syntax
- Obey selection scope when editing files
- Create backups before destructive operations
- Provide clear restoration instructions after changes

## Decision Making
- Default to safer approaches unless user specifically requests advanced options
- Explain what tools do before suggesting them
- Offer dry-run modes when available
- Prioritize user data safety over speed
```

## 📋 **Implementation Instructions**

### **Step 1: Add to .cursorrules**
Copy the rule sections above to your project's `.cursorrules` file.

### **Step 2: Customize for Your Project**
Modify rules based on:
- Project complexity and timeline
- Your experience level with AI collaboration
- Specific working preferences
- Team collaboration requirements

### **Step 3: Test the System**
1. Open a template file with the AI customization trigger
2. Verify the AI offers to help customize it
3. Test the interview process
4. Confirm the rules are working as expected

---

**Note**: These rules are based on proven patterns from successful AI collaboration projects. Customize them to match your specific working style and project needs. 