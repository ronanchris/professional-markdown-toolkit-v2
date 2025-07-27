<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the SESSION-PLAN template open. Would you like me to help you create a session plan for your current work through a quick interview? I'll ask you about your goals, timeline, and which Obsidian tools you need, then create a customized plan. This usually takes 5-10 minutes.

Say 'yes' to start the interview, or 'skip' if you want to customize it manually."

INTERVIEW QUESTIONS TO ASK:
1. What is your main goal for this session or project phase?
2. Are you working on: Notion imports, metadata cleanup, template management, or markdown processing?
3. What specific files or folders need attention?
4. What timeline are you working with?
5. What does success look like for this session?
6. Do you want basic progress tracking or full session continuity?

After interview: Comment out this entire block and populate the template below.
-->

# Session Plan - [USER TO CONFIRM DATE]
**Goal**: [Main objective for this session/project phase]

## 🎯 **Primary Goals** (Focus on 4-6 items max):
- [ ] [Specific goal 1 - be concrete and actionable]
- [ ] [Specific goal 2 - be concrete and actionable]
- [ ] [Specific goal 3 - be concrete and actionable]
- [ ] [Specific goal 4 - be concrete and actionable]

## 🛠️ **Tools & Methods**:
**Primary Tools Needed**:
- [ ] **Notion Import Tools**: `notion_complete_fixer.py`, `unicode_cleaner.py`, `wikilink_converter.py`
- [ ] **Metadata Management**: `fix_metadata.sh`, `remove_metadata.sh`, `safe_metadata_removal.py`
- [ ] **Template Management**: `apply_template.sh`, `fix_template.sh`
- [ ] **Markdown Processing**: `cleanup_markdown_batch.py`, `cleanup_markdown.py`
- [ ] **Project Structure**: `generate_project_structure.py`

**Approach**: [Describe methodology - systematic, iterative, surgical, etc.]  
**Timeline**: [Estimated completion time]

## 📂 **Target Files & Directories**:
- **Primary Target**: [Main files/folders to work on]
- **Test Cases**: [Files to test tools with]
- **Backup Location**: [Where backups will be stored]

## 🔄 **Implementation Phases**:

### **Phase 1: Setup & Preparation**
- [ ] Navigate to correct directory: `cd portable-obsidian-ai-tools`
- [ ] Verify dependencies: `pip install -r requirements.txt`
- [ ] Create backup: Use built-in backup functions
- [ ] Test target files accessibility

### **Phase 2: [Specific Work Phase]**
- [ ] [Tool-specific task 1] - Use `[specific script name]`
- [ ] [Tool-specific task 2] - Use `[specific script name]`
- [ ] [Tool-specific task 3] - Use `[specific script name]`
- [ ] Validate results and check for issues

### **Phase 3: [Specific Work Phase]**
- [ ] [Tool-specific task 1] - Use `[specific script name]`
- [ ] [Tool-specific task 2] - Use `[specific script name]`
- [ ] [Tool-specific task 3] - Use `[specific script name]`
- [ ] Document any patterns or discoveries

### **Phase 4: Validation & Documentation**
- [ ] Test processed files work correctly
- [ ] Document any tool improvements needed
- [ ] Update project structure if significant changes
- [ ] Backup final results

## 📊 **Progress Tracking**:
- ✅ **Completed**: [List completed items as they finish]
- 🔄 **In Progress**: [Current work]
- ⏸️ **Pending**: [Future work]

## 🔧 **Tool-Specific Notes**:

### **Notion Import Issues:**
- **Unicode problems**: Use `unicode_cleaner.py --strip-emojis --replace-chars`
- **WikiLink issues**: Use `wikilink_converter.py --preview` first
- **Complex formatting**: Use `notion_complete_fixer.py` for comprehensive fix
- **Large files**: Consider `--split-docs` option if files too large

### **Metadata Management:**
- **Batch cleanup**: Use `fix_metadata.sh` for standard YAML fixes
- **Specific removal**: Use `safe_metadata_removal.py --dry-run` first
- **Template integration**: Use `apply_template.sh` after metadata cleanup

### **Markdown Processing:**
- **Batch processing**: Use `cleanup_markdown_batch.py --verbose --recursive`
- **Single files**: Use `cleanup_markdown.py` for individual files
- **Quality check**: Always run with `--dry-run` first

## 🚨 **Common Issues & Solutions**:
- **Permission errors**: Check file permissions, use backup functions
- **Path issues**: Use relative paths, verify working directory
- **Large file processing**: Monitor memory usage, use chunking options
- **Dependency issues**: Reinstall requirements.txt if problems

## 🔄 **Deviations**:
*(Added automatically when approach changes)*

## 📝 **Session Notes**:
- [Key insights from using tools]
- [Tool performance observations]
- [Files that need special attention]
- [Improvements for future sessions]

## 🎯 **Success Criteria**:
- [ ] All target files processed successfully
- [ ] No data loss or corruption
- [ ] Tools performed as expected
- [ ] Documentation updated appropriately
- [ ] Results verified and tested

## 🔄 **Next Session Preparation**:
- **What to continue**: [Items for next session]
- **Tool improvements needed**: [Observations about tools]
- **Files to focus on**: [Remaining work]

---

**Next Action**: [Clear next step to begin work]

---

## 📋 **Template Usage Guide**

### **For Notion Import Projects:**
1. Focus Phase 2-3 on import tools (`notion_complete_fixer.py`, `unicode_cleaner.py`)
2. Use test files to validate approaches before processing all files
3. Document which fixes work best for different issue types

### **For Metadata Management:**
1. Start with `safe_metadata_removal.py --dry-run` to understand scope
2. Use `fix_metadata.sh` for batch standardization
3. Apply templates after metadata is clean

### **For Markdown Processing:**
1. Always start with `--dry-run` and `--verbose` to understand changes
2. Process in small batches to catch issues early
3. Verify formatting improvements don't break existing links

### **Session Continuity Integration:**
- **Session lens approach**: Focus on 4-6 items per session maximum
- **Auto-completion tracking**: Say "That's complete" when finishing tasks
- **Tool integration**: Session continuity tracks progress, tools do the work
- **Context preservation**: End-of-session notes capture tool performance insights 