# Generic Session Entrance Prompt

**PURPOSE**: This document provides the complete context needed for any AI assistant to effectively collaborate on a project using the Portable Obsidian AI Tools.

## ⚠️ **CRITICAL PREREQUISITE**

**Before using this prompt, you MUST have the cursor rules installed:**

1. **Copy the cursor rules** from `portable-obsidian-ai-tools/.cursorrules`
2. **Paste into** your project's `.cursor/rules/cursorrules.mdc` file
3. **Restart Cursor** to activate the rules

**Without cursor rules:** You'll get project context but **no automatic session continuity behaviors** (auto-triggers, session lens monitoring, completion detection, etc.)

**[📋 See DEPLOYMENT-PROMPT.md for complete setup instructions →](../../DEPLOYMENT-PROMPT.md)**

---

## 🎯 **COPY-PASTE ENTRANCE PROMPT** (Customize for Your Project)

```
I'm working on [YOUR PROJECT NAME]. Please read the following context carefully:

**PROJECT**: [YOUR PROJECT NAME] - [Brief description of your project]
**TOOLKIT**: Portable Obsidian AI Tools deployed for enhanced AI collaboration
**CURRENT STATUS**: [Your project status - e.g., "Starting documentation system for family coordination"]

**KEY CONTEXT**:
1. This project uses the Portable Obsidian AI Tools for enhanced AI collaboration
2. We have comprehensive backup systems and safety features built-in
3. Complete plan-driven session management system with automatic triggers and documentation
4. User prefers rapid iteration, challenges assumptions, and values honest feedback over politeness
5. All scripts include backup functionality - NEVER disable without explicit user request
6. **CRITICAL**: Always check for session-continuity/SESSION-PLAN.md and follow session lens approach (4-6 items focus)

**PROJECT-SPECIFIC GOALS**: [Customize this section]
- [Your main project goal]
- [Your secondary goals]
- [Any urgent priorities]

**WORKING PRINCIPLES**:
- Question timeline assumptions ("could we do this faster?")
- Challenge approaches when you see better alternatives  
- Focus on working examples over theoretical explanations
- Preserve YAML frontmatter, Obsidian embeds ([[links]]), and block references (^block-id)
- Apply session lens approach - focus on 4-6 items maximum per session

**IMMEDIATE ACTIONS**:
1. **FIRST**: Check for session-continuity/SESSION-PLAN.md (if no plan exists, offer to create via interview with date validation)
2. Read session-continuity/CURRENT-STATE-SNAPSHOT.md for current project status (if exists)
3. Read session-continuity/BLOG-LEARNING-MOMENTS.md to understand learning capture system
4. Apply session lens approach - focus on 4-6 items maximum per session
5. **ACTIVELY MONITOR** for these trigger phrases during conversation:
   - "That's complete" / "We've finished X" → Auto-check SESSION-PLAN.md checkboxes
   - "Actually, let's..." / "Change of plan" → Document deviation with date validation
   - "If system were working, wouldn't X happen?" → Implementation gap detection
   - "Let's wrap up" / "Session complete" → Archive session and update snapshots

**USER PREFERENCES**: [Customize based on your style]
- Direct, honest communication over diplomatic language
- Rapid iteration and execution over extensive planning
- Real-world validation over theoretical solutions
- System-thinking and reusability mindset
- Meta-conversation about improving the collaboration itself

Please confirm you understand this context and are ready to collaborate effectively on [YOUR PROJECT NAME].
```

---

## 📋 **Customization Instructions**

When deploying to a new project, replace these placeholders:

- **[YOUR PROJECT NAME]** - E.g., "Parkinson's Family Documentation System"
- **[Brief description]** - E.g., "Comprehensive family coordination and medical documentation system"
- **[Your project status]** - E.g., "Urgent documentation setup due to rapid progression"
- **[Your main project goal]** - E.g., "Create systematic documentation of father's care needs"
- **[Your secondary goals]** - E.g., "Coordinate family communication and decisions"
- **[Any urgent priorities]** - E.g., "Document current state before upcoming medical appointments"
- **[Customize based on your style]** - Adjust collaboration preferences as needed

## 🎯 **Quick Customization Example: Parkinson's Project**

```
I'm working on the Parkinson's Family Documentation System. Please read the following context carefully:

**PROJECT**: Parkinson's Family Documentation System - Comprehensive family coordination and medical documentation system
**TOOLKIT**: Portable Obsidian AI Tools deployed for enhanced AI collaboration  
**CURRENT STATUS**: Urgent documentation setup due to rapid progression of father's condition

**PROJECT-SPECIFIC GOALS**:
- Create systematic documentation of father's care needs and medical information
- Coordinate family communication and decision-making processes
- Establish sustainable system for tracking appointments, medications, and changes
- Prepare comprehensive information for medical consultations

**IMMEDIATE PRIORITIES**:
- Document current state before upcoming medical appointments
- Set up family coordination workflow
- Create templates for ongoing documentation
```

---

## 💡 **Tips for Effective Usage**

1. **Customize thoroughly** - Generic prompts are less effective than specific ones
2. **Update regularly** - As your project evolves, update the prompt context
3. **Test the automation** - Verify cursor rules are working by using trigger phrases
4. **Use session lens** - Keep focus on 4-6 items per session for best results
5. **Document learning** - Use the blog learning moments system to capture insights

This generic template ensures you get the full AI collaboration system benefits in any project! 