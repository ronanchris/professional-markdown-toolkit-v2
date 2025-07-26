<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the Session Prompts Index template open. Would you like me to help you create your first session prompt and set up the historical tracking system for your project? I'll ask about your project type, current challenges, and collaboration needs.

Say 'yes' to start the setup interview, or 'skip' if you want to handle it manually."

SETUP QUESTIONS TO ASK:
1. "What's your project name and type?" (creates project-specific context)
2. "What are your main challenges or urgent issues right now?" (creates first session prompt)
3. "What's your preferred collaboration style?" (customizes prompt templates)
4. "Do you need any specialized prompt types?" (determines which templates to create)
5. "How do you want session IDs organized?" (sets up naming convention)

After interview: Comment out this entire block and populate the index below with actual session files.
-->

# Session Prompts Index
*Navigation guide for AI assistants - Most recent prompts first*

## 📋 **Active Session Prompts** (Most Recent First)

### [DATE-session-NN-description.md]
**Type:** [PROMPT TYPE]  
**Context:** [SESSION CONTEXT]  
**Use for:** [WHEN TO USE THIS PROMPT]  

*Add actual session prompt files here as you create them*

## 🔧 **Reusable Template Prompts**

### templates/session-start.md
Standard session initiation prompt with full context loading

### templates/urgent-troubleshooting.md
High-stakes troubleshooting with comprehensive context

### templates/problem-solving.md  
Systematic problem analysis with surgical approach methodology

### templates/implementation-gap-detection.md
Validation prompt for checking design vs. reality

### templates/timeline-reality-check.md
Prompt for challenging complexity assumptions

## 🤖 **AI Usage Instructions**

**For Session Start:**
1. Always check this index first for latest prompts
2. Use most recent session prompt that matches current context
3. Fall back to templates/ for general patterns
4. When creating new prompts, follow naming: `YYYY-MM-DD-session-NN-description.md`

**Prompt Selection Guide:**
- **Urgent Issues:** Use latest deployment/troubleshooting prompt
- **New Features:** Use session management or foundation prompts  
- **Complex Problems:** Use problem-solving template
- **Timeline Pressure:** Use timeline-reality-check template

**Metadata Format:**
Each prompt file includes YAML frontmatter with session_id, date, type, tags, and status for systematic tracking.

## 🎯 **Customization Guide**

**To Set Up Your Prompt System:**
1. **Create your first session prompt** using templates/session-start.md as a base
2. **Customize templates** for your specific domain and working style
3. **Update this index** with your actual session files as you create them
4. **Follow naming convention** for chronological organization
5. **Track effectiveness** by updating session files with results

**Example Session Progression:**
```
2025-01-16-session-01-project-setup.md      # Initial setup
2025-01-17-session-02-core-features.md      # Feature development  
2025-01-18-session-03-deployment.md         # Deployment issues
2025-01-19-session-04-optimization.md       # Performance tuning
```

**Domain-Specific Customizations:**
- **Technical Projects**: Focus on debugging, testing, deployment templates
- **Documentation Projects**: Emphasize clarity, structure, review templates
- **Research Projects**: Prioritize analysis, validation, hypothesis templates
- **Creative Projects**: Balance structure with flexibility, iteration templates 