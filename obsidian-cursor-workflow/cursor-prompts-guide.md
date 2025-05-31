# How to Talk to Cursor: Prompts for Non-Technical Users

This guide helps Obsidian users who are new to Python, command-line tools, or Cursor itself. **Don't be intimidated** - Cursor can walk you through everything step by step!

## 🎯 The Basic Workflow

**You'll have TWO windows open:**
1. **Obsidian** - Your normal note-taking interface
2. **Cursor** - Where you run scripts and get AI help

**Key principle**: You run scripts FROM Cursor, not from Obsidian. Cursor is your "command center" for vault operations.

## 🗣️ Essential Cursor Prompts

### **Getting Started**

#### **"Help me set up this toolkit"**
```
I'm an Obsidian user new to Python and Cursor. I've downloaded the Professional Markdown Toolkit and want to set it up in my vault. Can you guide me through:

1. How to open my vault in Cursor
2. Where to put these scripts
3. How to configure the .cursorrules file
4. How to exclude scripts from Obsidian's interface

My vault is located at: [paste your vault path here]
```

#### **"Explain what this script does"**
```
I see a file called [script name]. Can you explain:
- What this script does in simple terms
- Whether it's safe to run on my vault
- What changes it will make
- Whether I should backup first

I'm not familiar with Python, so please explain like I'm new to programming.
```

### **Running Scripts Safely**

#### **"Help me test a script safely"**
```
I want to try running [script name] but I'm nervous about changing my vault. Can you help me:

1. Create a backup first
2. Run it on just one test file
3. Show me how to use the --dry-run option
4. Explain what the output means

My vault has [number] notes, and I want to be very careful.
```

#### **"Walk me through running this step by step"**
```
I want to run [specific script] to [what you want to accomplish]. I've never run Python scripts before. Can you give me exact step-by-step instructions, including:

1. Which window to type in
2. Exactly what to type
3. What I should see if it's working
4. How to tell if something goes wrong
5. How to stop it if needed
```

### **Understanding Output**

#### **"What do these error messages mean?"**
```
I tried to run [script name] and got this error message:
[paste the error here]

Can you explain:
- What went wrong in simple terms
- How to fix it
- Whether my files are okay
- What to try next
```

#### **"Interpret these results for me"**
```
I ran [script name] and got this output:
[paste the output here]

Can you help me understand:
- What changes were made
- Whether this is what I wanted
- If I need to do anything else
- Whether the results look normal
```

## 🛠️ Specific Script Prompts

### **Vault Analysis**

#### **"Analyze my vault health"**
```
I want to understand my vault better using the vault-analytics.py script. Can you:

1. Help me run it safely
2. Explain what each metric means
3. Tell me which recommendations I should prioritize
4. Suggest what I should improve first

I have about [number] notes and I'm particularly interested in [your specific concerns].
```

### **Markdown Cleanup**

#### **"Clean up my markdown formatting"**
```
My notes have inconsistent formatting and I want to clean them up. Can you help me:

1. Run the cleanup script safely on a test folder first
2. Show me what changes it will make
3. Make sure it won't break my [[wikilinks]] or frontmatter
4. Apply it to my whole vault if the test looks good

I'm worried about: [list your specific concerns]
```

### **Template Application**

#### **"Help me apply templates to my notes"**
```
I want to add consistent frontmatter to my notes using the template scripts. Can you:

1. Show me how to customize a template for my needs
2. Test it on one note first
3. Help me apply it to a folder of notes
4. Make sure it doesn't overwrite anything important

My notes are organized like: [describe your structure]
```

## 💡 Problem-Solving Prompts

### **"Something went wrong, help me fix it"**
```
I was trying to [what you were doing] and now:
- [describe what's wrong]
- [what you're seeing]
- [what you expected]

I'm worried I broke something. Can you help me:
1. Figure out what happened
2. Check if my files are okay
3. Fix any problems
4. Prevent this in the future
```

### **"I don't understand this documentation"**
```
I'm looking at [specific documentation section] and I don't understand:
- [specific part that's confusing]
- [what you're trying to accomplish]

Can you explain it in simpler terms and give me a concrete example for my situation?
```

### **"Customize this for my workflow"**
```
I see this script/template does [what it does], but I need it to [what you want instead]. Can you:

1. Explain how to modify it
2. Show me the specific changes to make
3. Help me test the changes
4. Make sure I don't break anything

I'm not comfortable editing code myself, so please guide me carefully.
```

## 🎨 Creative Workflow Prompts

### **"Design a workflow for my specific needs"**
```
I'm a [your role/context] who uses Obsidian for [your main use cases]. Based on this toolkit, can you suggest:

1. Which scripts would be most useful for me
2. A weekly/monthly maintenance routine
3. How to organize my vault for best results
4. Automation I should set up

My main challenges are: [list your pain points]
```

### **"Help me understand what's possible"**
```
I'm new to using AI for vault management. Can you show me:

1. Examples of powerful things I can do with this toolkit
2. Common workflows other users find helpful
3. How to gradually adopt more advanced features
4. What I should learn next

I'm comfortable with: [list your current skills]
I'd like to learn: [list your goals]
```

## 🚨 Emergency Prompts

### **"I think I broke something, help!"**
```
URGENT: I ran [script name] and now my vault seems broken. I'm seeing:
- [describe the problem]

Can you help me:
1. Check if this is actually a problem
2. Restore from backup if needed
3. Fix any real issues
4. Prevent this from happening again

I'm very stressed and need clear, step-by-step guidance.
```

### **"Restore my vault from backup"**
```
I need to restore my vault from a backup because [what went wrong]. Can you walk me through:

1. How to check what Git backups I have
2. How to restore to a previous state
3. How to verify everything is working
4. How to avoid losing recent work if possible

I'm not familiar with Git, so please explain each step clearly.
```

## 📚 Learning Prompts

### **"Teach me about version control for my vault"**
```
I keep hearing about Git and version control. Can you:

1. Explain why it's important for my vault
2. Walk me through setting it up
3. Show me basic commands I should know
4. Help me create a backup routine

I'm intimidated by command-line tools but want to learn.
```

### **"Help me understand .cursorrules"**
```
I see there's a .cursorrules file that's important. Can you:

1. Explain what it does in simple terms
2. Show me how to customize it for my writing style
3. Give me examples of useful rules
4. Help me set it up properly

I want to make sure AI editing respects my Obsidian setup.
```

## 💬 General Communication Tips

### **Be Specific About Your Context**
Instead of: "Help me clean up my vault"
Try: "I have 500 notes with inconsistent heading formats and want to standardize them without breaking my [[wikilinks]]"

### **Mention Your Comfort Level**
- "I'm new to Python"
- "I'm comfortable with basic scripts"
- "I'm nervous about changing my files"
- "I want to understand what's happening"

### **Ask for Examples**
- "Can you show me exactly what to type?"
- "What should I expect to see?"
- "Can you give me a concrete example?"

### **Request Step-by-Step Guidance**
- "Walk me through this slowly"
- "What's the first thing I should do?"
- "How do I know if it's working?"

## 🎯 Remember

**Cursor is designed to help you!** Don't be afraid to:
- Ask for clarification if something is confusing
- Request simpler explanations
- Ask for examples specific to your situation
- Get help testing things safely
- Ask the same question in different ways if needed

**You're not expected to know Python or command-line tools.** Cursor can teach you everything you need to know, step by step.

---

**Start with**: "I'm an Obsidian user new to Cursor and Python. Can you help me get started with this toolkit?" and let Cursor guide you from there! 

## 🌟 Day-in-the-Life Scenarios

*Real-world problems you encounter and exactly how to solve them*

### **📋 "I copied content from ChatGPT/websites and now my notes have ugly extra spaces"**

**The Problem**: You copy content from ChatGPT, websites, or other apps and when you paste into Obsidian, it looks fine in preview mode but edit mode shows tons of extra blank lines and weird spacing.

**The Script**: `cleanup_markdown_batch.py`

**The Cursor Prompt**:
```
I just copied content from [ChatGPT/website/app] into my Obsidian notes and now I have a bunch of extra vertical spaces that look messy in edit mode. I think I need to use the cleanup_markdown_batch.py script. Can you:

1. Show me how to run it on just one file first to test
2. Explain what changes it will make to fix the spacing
3. Help me apply it to all my recent notes if the test looks good
4. Make sure it won't break my [[wikilinks]] or frontmatter

The messy file is: [path to your file]
```

**What It Fixes**: Multiple consecutive blank lines → single blank lines, extra whitespace → clean formatting, malformed spacing → proper markdown structure.

---

### **📝 "My headings are inconsistent after importing notes from [Notion/Roam/Word]"**

**The Problem**: After migrating from another tool or importing content, your headings have inconsistent spacing, some missing the space after #, different heading levels for similar content.

**The Script**: `cleanup_markdown_batch.py` + Cursor's find/replace

**The Cursor Prompt**:
```
I imported notes from [Notion/Roam/Word/etc] and now my headings are a mess. Some have #Heading (no space), others have proper spacing, and the hierarchy is inconsistent. I need to:

1. Fix heading spacing (# Heading not #Heading)
2. Standardize heading levels for similar content types
3. Make sure this doesn't break anything else

Can you help me use cleanup_markdown_batch.py and show me the right find/replace patterns to standardize my headings across [number] notes?
```

**What It Fixes**: Inconsistent heading formats → proper markdown spacing, heading hierarchy → logical structure.

---

### **⚠️ "My frontmatter is broken/missing after bulk operations"**

**The Problem**: After moving files around or using templates, some notes have broken YAML frontmatter, missing metadata, or inconsistent date formats.

**The Script**: `apply_inbox_template.py` or metadata repair scripts

**The Cursor Prompt**:
```
I was reorganizing my vault and now some of my notes have broken or missing frontmatter. I'm seeing notes without proper YAML headers, inconsistent date formats, and missing required fields like 'created' or 'modified'. 

Can you help me:
1. Identify which notes have broken/missing frontmatter
2. Use the right script to fix or add proper frontmatter
3. Standardize the date formats (I prefer YYYY-MM-DD)
4. Make sure I don't overwrite any existing metadata that's correct

My vault has about [number] notes and I use these standard frontmatter fields: [list your fields]
```

**What It Fixes**: Missing frontmatter → proper YAML headers, inconsistent dates → standard formats, broken metadata → valid structure.

---

### **🔗 "My bullet points and lists look terrible after copy-pasting"**

**The Problem**: Lists from different sources have inconsistent indentation, mixed bullet styles (-, *, +), improper spacing between items.

**The Script**: `cleanup_markdown_batch.py`

**The Cursor Prompt**:
```
I've been copying lists and bullet points from various sources (emails, websites, other apps) and now my notes have inconsistent list formatting. Some use -, others use *, the indentation is all over the place, and spacing between items varies.

I want to:
1. Standardize all bullet points to use - (dash)
2. Fix indentation to be consistent (2 or 4 spaces)
3. Clean up spacing between list items
4. Make sure nested lists still work properly

Can you help me run the cleanup script on my notes folder and show me what changes it will make?
```

**What It Fixes**: Mixed bullet styles → consistent dashes, improper indentation → standard spacing, messy list formatting → clean markdown lists.

---

### **📅 "My date formats are inconsistent across my vault"**

**The Problem**: Some notes use MM/DD/YYYY, others use DD-MM-YYYY, some use text dates, creating chaos in Dataview queries and templates.

**The Script**: `update_date_created_to_templater.py`

**The Cursor Prompt**:
```
My vault has dates in all different formats - some notes use MM/DD/YYYY, others DD-MM-YYYY, some have text dates like "January 15, 2024". This breaks my Dataview queries and makes organization impossible.

I need to:
1. Find all the different date formats in my frontmatter
2. Convert everything to YYYY-MM-DD format
3. Make sure this works with my Templater setup
4. Not break any existing dates that are already correct

Can you help me use the date conversion script and show me how to handle this safely across my [number] notes?
```

**What It Fixes**: Mixed date formats → consistent YYYY-MM-DD, broken Dataview queries → working data views, template incompatibility → proper Templater integration.

---

### **🏗️ "I need to apply templates to a bunch of existing notes"**

**The Problem**: You've created great templates but have 50+ existing notes that need the template structure added without losing their content.

**The Script**: `apply_inbox_template_to_folder.py`

**The Cursor Prompt**:
```
I have a great template for [project/meeting/daily] notes but I have [number] existing notes that don't use the template structure. I want to add the template's frontmatter and structure to these existing notes without losing their content.

Can you help me:
1. Test the template application on one note first
2. Show me how it will merge the template with existing content
3. Apply it to the whole folder if the test looks good
4. Make sure it doesn't overwrite anything important

My template is: [path to template]
The notes that need updating are in: [path to folder]
```

**What It Fixes**: Unstructured notes → consistent template format, missing metadata → complete frontmatter, inconsistent organization → standardized structure.

---

### **🧹 "My vault feels messy and I don't know what needs fixing"**

**The Problem**: Your vault has grown organically and you sense it needs cleanup but don't know where to start or what's wrong.

**The Script**: `vault-analytics.py`

**The Cursor Prompt**:
```
My Obsidian vault has grown to [number] notes and it feels messy, but I don't know exactly what needs fixing. Can you help me:

1. Run the vault analytics script to get a health report
2. Explain what each metric means in simple terms
3. Prioritize which issues I should tackle first
4. Give me a step-by-step plan to improve my vault's quality

I want to understand what's working well and what needs attention before I start making changes.
```

**What It Reveals**: Broken links, orphaned notes, metadata inconsistencies, formatting issues, optimization opportunities, vault health metrics.

---

### **📄 "I need to create a professional document from my scattered notes"**

**The Problem**: You have research, notes, and ideas scattered across many files but need to combine them into a professional document for sharing.

**The Script**: `build-consolidated-doc.sh` (customized)

**The Cursor Prompt**:
```
I have research and notes scattered across multiple files about [topic] and I need to create a professional document to share with [colleagues/clients/team]. The notes are in:
- [list your relevant files/folders]

Can you help me:
1. Understand how the document consolidation script works
2. Customize it for my specific content
3. Create a professional-looking combined document
4. Make sure the formatting is appropriate for [your audience]
5. Include proper source attribution

I want the final document to be ready for [email/presentation/publication].
```

**What It Creates**: Scattered notes → cohesive document, informal notes → professional presentation, multiple files → single deliverable.

---

### **🔍 "I think I have broken WikiLinks after reorganizing"**

**The Problem**: After moving files around or renaming folders, you suspect some of your [[WikiLinks]] might be broken but don't want to check hundreds manually.

**The Solution**: Cursor's search + link verification

**The Cursor Prompt**:
```
I recently reorganized my vault by [moving files/renaming folders/etc] and I'm worried some of my [[WikiLinks]] might be broken. I have [number] notes with lots of internal links.

Can you help me:
1. Search for patterns that might indicate broken links
2. Find links to files that no longer exist
3. Identify any links with typos or formatting issues
4. Show me how to fix them efficiently
5. Prevent this from happening again in the future

I want to make sure all my connections are still working properly.
```

**What It Finds**: Broken [[links]], missing files, malformed link syntax, orphaned references, connection gaps.

---

### **🆘 "I imported a bunch of files and everything looks wrong"**

**The Problem**: You imported files from another system (Roam, Notion, Word documents) and the formatting is a disaster.

**The Scripts**: Multiple cleanup scripts in sequence

**The Cursor Prompt**:
```
HELP! I just imported [number] files from [Roam/Notion/Word/etc] and they look terrible in Obsidian. I'm seeing:
- Weird spacing and formatting
- Broken or missing frontmatter  
- Inconsistent heading styles
- Messed up bullet points
- [other specific issues you notice]

Can you help me create a systematic cleanup plan? I need to:
1. Understand what went wrong during import
2. Run the right scripts in the right order
3. Test everything on a few files first
4. Fix the whole batch if tests work
5. Make sure I don't lose any content

I'm overwhelmed and need step-by-step guidance to rescue my import.
```

**What It Fixes**: Import disasters → clean markdown, broken formatting → Obsidian-compatible structure, chaos → organized content.

---

### **⚡ "I want to set up a weekly vault maintenance routine"**

**The Problem**: You want to prevent problems before they happen by establishing regular maintenance.

**The Scripts**: Multiple scripts for different maintenance tasks

**The Cursor Prompt**:
```
I want to be proactive about vault maintenance instead of waiting for problems. My vault has [number] notes and I add about [number] new notes per week.

Can you help me create a weekly maintenance routine that includes:
1. Checking for formatting issues and fixing them
2. Standardizing new notes that don't follow my templates
3. Finding and fixing any broken links
4. Updating metadata consistency
5. General health check and optimization

I want to spend maybe 15-30 minutes per week keeping everything clean and organized. What should my routine look like and which scripts should I run when?
```

**What It Creates**: Reactive fixes → proactive maintenance, accumulating problems → consistent quality, chaos → systematic care.

---

## 💡 Quick Reference: Problem → Script

| **Problem** | **Script** | **Quick Prompt** |
|-------------|------------|------------------|
| Extra spaces from copy-paste | `cleanup_markdown_batch.py` | "Fix spacing issues in my notes from copy-paste" |
| Inconsistent headings | `cleanup_markdown_batch.py` + find/replace | "Standardize my heading formats" |
| Missing frontmatter | `apply_inbox_template.py` | "Add frontmatter to notes missing it" |
| Messy bullet points | `cleanup_markdown_batch.py` | "Clean up my list formatting" |
| Mixed date formats | `update_date_created_to_templater.py` | "Standardize date formats in frontmatter" |
| Need templates applied | `apply_inbox_template_to_folder.py` | "Apply template to existing notes" |
| Vault feels messy | `vault-analytics.py` | "Analyze my vault health" |
| Need professional doc | `build-consolidated-doc.sh` | "Create professional document from notes" |
| Broken links suspected | Cursor search features | "Find and fix broken WikiLinks" |
| Import disaster | Multiple scripts | "Help me clean up my import mess" |
| Want maintenance routine | Various scripts | "Create weekly vault maintenance routine" |

Remember: **Always start with "I'm new to this, please guide me step by step"** and Cursor will help you safely accomplish any of these tasks! 