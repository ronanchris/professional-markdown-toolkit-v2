# Obsidian Template Examples

This file contains practical template examples for different types of notes in your Obsidian vault. Copy these templates to your vault's `templates/` folder and customize them for your needs.

## 📋 Basic Templates

### **Daily Note Template**
File: `templates/daily-note.md`
```markdown
---
title: {{date:YYYY-MM-DD dddd}}
created: {{date:YYYY-MM-DD}}
type: daily-note
tags: [daily]
date: {{date:YYYY-MM-DD}}
---

# {{date:YYYY-MM-DD dddd}}

## Today's Focus
- 

## Journal


## Tasks
- [ ] 

## Notes


## Links Created Today


## Review
- What went well:
- What could improve:
- Tomorrow's priority:

---
*Previous: [[{{date-1:YYYY-MM-DD}}]] | Next: [[{{date+1:YYYY-MM-DD}}]]*
```

### **Meeting Notes Template**
File: `templates/meeting-notes.md`
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
type: meeting
tags: [meeting]
attendees: []
project: 
date: {{date:YYYY-MM-DD}}
time: {{time:HH:mm}}
---

# {{title}}

**Date:** {{date:YYYY-MM-DD}}  
**Time:** {{time:HH:mm}}  
**Attendees:** 
**Project:** 

## Agenda
1. 
2. 
3. 

## Discussion Notes


## Decisions Made
- [ ] 
- [ ] 

## Action Items
- [ ] **Person:** Task - Due: 
- [ ] **Person:** Task - Due: 

## Follow-up
- Next meeting: 
- Related notes: 

## Resources
- 

---
*Meeting series: [[]] | Previous: [[]] | Next: [[]]* 
```

### **Project Template**
File: `templates/project.md`
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
type: project
status: active
priority: medium
tags: [project]
start_date: 
due_date: 
---

# {{title}}

## Overview


## Goals & Objectives
- **Primary Goal:** 
- **Success Metrics:** 
- **Key Deliverables:** 

## Status: {{status}}
- **Progress:** _%
- **Next Milestone:** 
- **Blockers:** 

## Timeline
- **Start Date:** 
- **Due Date:** 
- **Key Milestones:**
  - [ ] Milestone 1 - Date
  - [ ] Milestone 2 - Date
  - [ ] Final Delivery - Date

## Team & Stakeholders
- **Project Lead:** 
- **Team Members:** 
- **Stakeholders:** 

## Resources
- **Budget:** 
- **Tools:** 
- **References:** 

## Tasks
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

## Notes & Updates


## Related Projects
- 

---
*Project Portfolio: [[Projects MOC]] | Status: {{status}}*
```

## 📚 Knowledge Management Templates

### **Book Notes Template**
File: `templates/book-notes.md`
```markdown
---
title: "{{title}}"
created: {{date:YYYY-MM-DD}}
type: book-notes
tags: [book, reading]
author: 
genre: 
published: 
pages: 
rating: 
status: reading
---

# {{title}}

**Author:** 
**Genre:** 
**Published:** 
**Pages:** 
**My Rating:** ⭐⭐⭐⭐⭐
**Status:** {{status}}

## Summary


## Key Concepts
1. **Concept 1** - Description
2. **Concept 2** - Description
3. **Concept 3** - Description

## Important Quotes
> "Quote 1" - Page X

> "Quote 2" - Page Y

## Personal Insights


## Action Items
- [ ] Apply concept 1 to...
- [ ] Research more about...
- [ ] Share with...

## Related Reading
- [[Similar Book 1]]
- [[Author's Other Work]]
- [[Topic-related Book]]

## Chapter Notes
### Chapter 1: Title
- Key points
- Personal thoughts

### Chapter 2: Title
- Key points
- Personal thoughts

---
*Reading List: [[Books MOC]] | Genre: [[{{genre}}]] | Author: [[{{author}}]]*
```

### **Person Template**
File: `templates/person.md`
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
type: person
tags: [person]
organization: 
role: 
contact_method: 
last_contact: 
---

# {{title}}

## Basic Info
- **Organization:** 
- **Role/Title:** 
- **Department:** 
- **Location:** 

## Contact Information
- **Email:** 
- **Phone:** 
- **LinkedIn:** 
- **Other:** 

## Relationship Context
- **How we met:** 
- **Relationship type:** 
- **Mutual connections:** 

## Interaction History
### {{date:YYYY-MM-DD}} - Initial Contact


### Previous Interactions
- **Date:** Topic/context

## Projects & Collaborations
- [[Project 1]] - Role
- [[Project 2]] - Role

## Notes & Insights
- **Professional interests:** 
- **Personal interests:** 
- **Communication style:** 
- **Key achievements:** 

## Follow-up Actions
- [ ] Action 1 - Due date
- [ ] Action 2 - Due date

---
*Network: [[People MOC]] | Organization: [[{{organization}}]]*
```

### **Concept/Learning Template**
File: `templates/concept.md`
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
type: concept
tags: [concept, learning]
domain: 
difficulty: 
source: 
---

# {{title}}

## Definition


## Key Components
1. **Component 1** - Description
2. **Component 2** - Description
3. **Component 3** - Description

## Explanation


## Examples
### Real-world Example 1


### Real-world Example 2


## Related Concepts
- **Prerequisite:** [[Concept A]] - Why it's needed first
- **Similar:** [[Concept B]] - How they relate
- **Builds to:** [[Advanced Concept]] - Next level concepts

## Applications
- **Use case 1:** Description
- **Use case 2:** Description

## Learning Resources
- **Primary source:** 
- **Additional reading:** 
- **Video explanations:** 
- **Practice exercises:** 

## Personal Understanding
- **Confidence level:** /10
- **Areas needing work:** 
- **Teaching test:** Can I explain this to someone else?

## Questions & Research
- [ ] Question 1 to explore
- [ ] Question 2 to research

---
*Domain: [[{{domain}} MOC]] | Difficulty: {{difficulty}} | Source: [[{{source}}]]*
```

## 🎯 Specialized Templates

### **Weekly Review Template**
File: `templates/weekly-review.md`
```markdown
---
title: Week of {{date:YYYY-MM-DD}}
created: {{date:YYYY-MM-DD}}
type: weekly-review
tags: [review, planning]
week_of: {{date:YYYY-[W]WW}}
---

# Week of {{date:YYYY-MM-DD}}

## Week Overview
**Theme:** 
**Key Focus Areas:** 

## Accomplishments ✅
- 
- 
- 

## Challenges & Lessons 🎯
- **Challenge:** Solution/Learning
- **Challenge:** Solution/Learning

## Metrics & Progress
- **Goal 1:** Progress description
- **Goal 2:** Progress description
- **Health:** Exercise/wellness notes

## Upcoming Week Planning
### Priority Projects
1. **High:** Project/task
2. **Medium:** Project/task
3. **Low:** Project/task

### Scheduled Events
- **Monday:** 
- **Tuesday:** 
- **Wednesday:** 
- **Thursday:** 
- **Friday:** 

### Next Week's Focus
- Primary goal:
- Key deliverables:
- Important deadlines:

## Gratitude & Reflection
- **Grateful for:** 
- **Personal growth:** 
- **Relationships:** 

---
*Previous: [[{{date-7:YYYY-MM-DD}}]] | Next: [[{{date+7:YYYY-MM-DD}}]] | Monthly: [[{{date:YYYY-MM}} Monthly Review]]*
```

### **Decision Log Template**
File: `templates/decision-log.md`
```markdown
---
title: "Decision: {{title}}"
created: {{date:YYYY-MM-DD}}
type: decision
tags: [decision]
status: pending
impact: medium
deadline: 
stakeholders: []
---

# Decision: {{title}}

## Context & Background


## Decision Statement
**We need to decide:** 

**By when:** 
**Who decides:** 
**Impact level:** {{impact}}

## Options Considered
### Option 1: Name
- **Pros:** 
- **Cons:** 
- **Cost/Effort:** 
- **Risk:** 

### Option 2: Name
- **Pros:** 
- **Cons:** 
- **Cost/Effort:** 
- **Risk:** 

### Option 3: Name
- **Pros:** 
- **Cons:** 
- **Cost/Effort:** 
- **Risk:** 

## Evaluation Criteria
1. **Criterion 1** (Weight: %)
2. **Criterion 2** (Weight: %)
3. **Criterion 3** (Weight: %)

## Analysis & Research
- **Data points:** 
- **Expert opinions:** 
- **Similar cases:** 

## Recommendation
**Recommended option:** 
**Rationale:** 

## Implementation Plan
- [ ] Step 1 - Owner - Due date
- [ ] Step 2 - Owner - Due date
- [ ] Step 3 - Owner - Due date

## Success Metrics
- **Metric 1:** Target/measurement
- **Metric 2:** Target/measurement

## Review & Follow-up
- **Review date:** 
- **Success criteria:** 

---
*Decisions: [[Decisions MOC]] | Impact: {{impact}} | Status: {{status}}*
```

## 🔧 Technical Templates

### **Troubleshooting Template**
File: `templates/troubleshooting.md`
```markdown
---
title: "Issue: {{title}}"
created: {{date:YYYY-MM-DD}}
type: troubleshooting
tags: [issue, technical]
system: 
severity: 
status: open
assignee: 
---

# Issue: {{title}}

## Problem Description
**What happened:** 
**Expected behavior:** 
**Actual behavior:** 

## Environment
- **System:** 
- **Version:** 
- **Browser/Platform:** 
- **User:** 
- **Date/Time:** {{date:YYYY-MM-DD HH:mm}}

## Steps to Reproduce
1. 
2. 
3. 

## Error Messages


## Investigation Notes
### Initial Analysis


### Testing Results


### Root Cause


## Solution
### Immediate Fix


### Permanent Solution


### Prevention Measures


## Implementation
- [ ] Deploy fix - Owner - Due
- [ ] Test solution - Owner - Due
- [ ] Update documentation - Owner - Due
- [ ] Monitor results - Owner - Due

## Related Issues
- Similar: [[Issue 123]]
- Caused by: [[Issue 456]]
- May cause: [[Issue 789]]

---
*Status: {{status}} | Severity: {{severity}} | System: [[{{system}}]]*
```

## 🎨 Creative Templates

### **Idea Capture Template**
File: `templates/idea.md`
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
type: idea
tags: [idea]
status: new
category: 
priority: 
---

# 💡 {{title}}

## The Idea


## Context & Inspiration
**Where it came from:** 
**What triggered it:** 
**Related thoughts:** 

## Potential & Value
**Who would benefit:** 
**Problem it solves:** 
**Unique angle:** 

## Development Path
### Immediate Next Steps
- [ ] Research step 1
- [ ] Test step 2
- [ ] Validate step 3

### Longer-term Development
- **Phase 1:** 
- **Phase 2:** 
- **Phase 3:** 

## Resources Needed
- **Time:** 
- **Skills:** 
- **People:** 
- **Budget:** 

## Success Scenarios
**Best case:** 
**Realistic case:** 
**Minimum viable:** 

## Risks & Challenges
- **Risk 1:** Mitigation
- **Risk 2:** Mitigation

## Related Ideas
- Builds on: [[Previous Idea]]
- Combines with: [[Other Idea]]
- Could lead to: [[Future Possibility]]

---
*Ideas: [[Ideas MOC]] | Category: {{category}} | Status: {{status}}*
```

## 📝 Usage Tips

### **Template Variables**
These templates use Templater plugin syntax:
- `{{date:YYYY-MM-DD}}` - Today's date in ISO format
- `{{time:HH:mm}}` - Current time
- `{{title}}` - Prompts for title input
- `{{date-7:YYYY-MM-DD}}` - Date 7 days ago
- `{{date+7:YYYY-MM-DD}}` - Date 7 days ahead

### **Customization**
1. **Modify metadata fields** to match your vault structure
2. **Adjust tag hierarchies** to fit your organization system
3. **Add/remove sections** based on your needs
4. **Change link patterns** to match your MOC structure

### **Installation**
1. Create a `templates/` folder in your vault
2. Copy desired templates to that folder
3. Configure Templater plugin to use `templates/` folder
4. Set up hotkeys for frequently used templates

### **Folder Templates**
Configure folder-specific templates in Templater:
- `daily-notes/` → `daily-note.md`
- `meetings/` → `meeting-notes.md`
- `projects/` → `project.md`
- `people/` → `person.md`

---

**Remember:** These templates are starting points. Customize them to match your specific workflow, vault structure, and personal preferences. The key is consistency across your vault for better organization and searchability. 