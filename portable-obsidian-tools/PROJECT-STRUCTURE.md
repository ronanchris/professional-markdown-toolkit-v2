# Project Structure Context

**Purpose**: Provide AI assistants with complete project context for optimal tool selection and guidance.

## 🗂️ **ASCII Project Sitemap**

**Instructions**: Replace this placeholder with your project's actual structure using the prompt below.

```
[REPLACE WITH YOUR PROJECT SITEMAP]

Example:
project-root/
├── .cursor/
│   └── rules/
├── portable-obsidian-tools/          # 👈 This toolkit
│   ├── obsidian-tools/
│   ├── metadata-tools/
│   ├── markdown-processing/
│   └── session-continuity/
├── docs/
│   ├── user-guides/
│   └── technical/
├── src/
│   ├── components/
│   └── pages/
└── README.md
```

## 🔄 **How to Generate/Update Your Sitemap**

### **Initial Setup Prompt:**
```
Create an ASCII directory tree sitemap of this entire project. 
Include all major folders and key files, but exclude:
- node_modules, .git, build artifacts
- Individual files inside large directories (just show the directory)
- Temporary or cache files

Format as a clean ASCII tree structure. Focus on the logical organization 
that would help an AI assistant understand the project structure.
```

### **Update Prompt:**
```
Update the ASCII sitemap in portable-obsidian-tools/PROJECT-STRUCTURE.md 
to reflect the current project structure. Keep the same format and 
exclusion criteria as the original.
```

## 📋 **Project Context Summary**

**Update this section with key details:**

### **Project Type**: [Web app / Documentation site / Data analysis / etc.]
### **Primary Technologies**: [React, Python, Obsidian, etc.]  
### **Key Working Areas**: [Where you spend most time editing]

### **Important Directories for AI Tool Selection:**
- **Documentation/Notes**: [Path] → Use obsidian-tools, metadata-tools
- **Markdown Content**: [Path] → Use markdown-processing tools
- **Technical Files**: [Path] → May need special handling
- **Archive/Old Content**: [Path] → Good for batch cleanup operations

## 🎯 **AI Assistant Guidance**

**Based on this project structure:**

### **Most Likely Tool Usage:**
- **Bulk operations**: Use markdown-processing batch tools
- **Template management**: Use obsidian-tools for structured content
- **Cleanup operations**: Use metadata-tools for YAML/frontmatter
- **Import fixes**: Use Notion import tools for external content

### **Working Patterns:**
- **When user mentions [specific directory]** → Suggest [appropriate tools]
- **For large-scale changes** → Always mention backup systems first
- **For new content** → Consider template application tools

---

**Last Updated**: [Date]  
**Next Review**: [When project structure significantly changes] 