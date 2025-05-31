# Complete Setup Guide: Obsidian + Cursor Power User Workflow

This guide walks you through the complete setup process for using Cursor as a powerful companion editor for your Obsidian vaults. Follow these steps to create a professional, efficient workflow that leverages the strengths of both tools.

## 🎯 Overview

This setup optimizes your environment for:
- **Large vault management** (1,000+ notes)
- **Professional document generation**
- **Bulk metadata operations**
- **Team collaboration workflows**
- **Version control with Git**
- **AI-assisted editing with safety**

## 📋 Prerequisites

- **Obsidian** (latest version) *or other markdown-based writing tool*
- **Cursor** (AI-powered code editor)
- **Git** (for version control)
- **Python 3.8+** (for automation scripts)
- Basic familiarity with both Obsidian and Cursor

## 🌐 Beyond Obsidian: Cursor for Writing

While this guide focuses on Obsidian, **Cursor is an exceptional writing tool for any markdown-based system**. The collaborative editing environment transforms how you interact with AI assistance:

### **Why Cursor for Writing?**
- **In-context AI assistance** - Get help directly in your document, not in a separate chat
- **Document-aware suggestions** - AI understands your full text structure and context
- **Professional workflows** - Git integration, formatting tools, and publishing pipelines
- **Collaborative feel** - AI becomes a writing partner rather than a query-response tool
- **Distraction-free** - Stay focused on writing without switching between tools

### **Compatible Writing Systems**
These principles and many scripts work with other tools:

#### **Knowledge Management Systems:**
- **Roam Research** - Block-based notes, daily pages
- **LogSeq** - Local-first, block-based knowledge graphs
- **Dendron** - Hierarchical note-taking in VSCode
- **Foam** - Networked thought in VSCode
- **Notion** - Databases with markdown support

#### **Academic & Long-form Writing:**
- **Zettlr** - Academic writing with Zettelkasten method
- **Typora** / **Mark Text** - Distraction-free markdown editors
- **Pandoc workflows** - Academic publishing pipelines

#### **Simple & Cross-platform:**
- **Joplin** - Encrypted, synchronizable notes
- **Bear** - Elegant markdown writing (Mac/iOS)
- **Standard markdown** - Just files + folders + Git

#### **Team & Documentation:**
- **GitBook** / **Bookstack** - Team knowledge bases
- **MkDocs** / **Docusaurus** - Documentation sites
- **Jekyll** / **Hugo** - Static site generators

*The core principle: Use Cursor to enhance any text-based writing workflow with AI assistance.*

## 🚀 The Two-Window Workflow

### **🎯 Understanding Your Workspace**

**You'll have BOTH applications open simultaneously:**

1. **Obsidian** 📝 - Your Primary Interface
   - Keep this open for daily note-taking
   - Reading, writing, and linking notes
   - Mobile sync and plugins work normally
   - Graph view and search work as usual

2. **Cursor** 🚀 - Your Command Center
   - This is where you run scripts and get AI help
   - Think of it as your "vault maintenance workshop"
   - Where you type commands and make bulk changes
   - AI assistant helps you with everything

**Typical Workflow:**
```
Obsidian: Write notes, explore links, daily work
    ↓
Cursor: "I want to clean up 100 notes' formatting"
    ↓
AI helps you run scripts safely and explains everything
    ↓
Obsidian: See the improved results
```

### **🆘 New to Python/Command Line? DON'T PANIC!**

**You don't need to know Python or command-line tools!** Here's what to do:

1. **Download Cursor** (free from cursor.sh)
2. **Open your vault in Cursor**: File > Open Folder > Select your Obsidian vault
3. **Ask Cursor for help**: Copy this exact prompt:

```
I'm an Obsidian user new to Python and Cursor. I want to use the Professional Markdown Toolkit to improve my vault. Can you:

1. Explain what I'm looking at in simple terms
2. Help me install the scripts safely  
3. Walk me through running one script as a test
4. Show me how to backup my vault first

I'm nervous about breaking my notes, so please guide me step by step.
```

4. **Let Cursor teach you everything!** It will explain each step in plain English.

**Remember**: Cursor is designed to help beginners. Don't be intimidated by `.py` or `.sh` files - Cursor will explain what they do and help you use them safely.

See `cursor-prompts-guide.md` for dozens of example prompts to get help with anything!

## 🔧 Obsidian Configuration

### **1. Essential Obsidian Settings**

#### **Files & Links**
```
Settings > Files & Links:
✅ Automatically update internal links: ON
✅ New link format: Shortest path when possible
✅ Use [[Wikilinks]]: ON
✅ Default location for new notes: Same folder as current file
✅ New file location: Root folder of vault (or your preferred structure)
✅ Default location for new attachments: In subfolder under current folder
✅ Subfolder name: assets (or attachments)
```

#### **Editor Settings**
```
Settings > Editor:
✅ Show line numbers: ON (helpful for debugging)
✅ Readable line length: OFF (for full-width editing)
✅ Strict line breaks: OFF (for better compatibility with external editors)
✅ Tab size: 2 or 4 (match your Cursor preference)
✅ Use tabs: OFF (use spaces for better compatibility)
✅ Vim key bindings: Based on preference
```

#### **Appearance**
```
Settings > Appearance:
✅ Theme: Choose based on preference
✅ Font size: Readable size (14-16px recommended)
✅ Show inline title: ON (helps with navigation)
✅ Show tab title bar: ON
✅ Show vault name in sidebar: ON
```

### **2. Essential Core Plugins**

#### **Enable These Core Plugins:**
```
Settings > Core plugins:
✅ File explorer
✅ Search
✅ Quick switcher
✅ Graph view
✅ Backlinks
✅ Outgoing links
✅ Tag pane
✅ Command palette
✅ Markdown format importer
✅ Word count
✅ File recovery
```

#### **Configure Templates (Core Plugin)**
```
Settings > Templates:
✅ Template folder location: templates/ (create this folder)
✅ Date format: YYYY-MM-DD
✅ Time format: HH:mm
```

### **3. Recommended Community Plugins**

#### **Essential for Power Users:**
- **Templater** - Advanced template engine
- **Dataview** - Query and display vault data
- **Advanced Tables** - Better table editing
- **Calendar** - Visual date navigation
- **Tag Wrangler** - Bulk tag operations
- **Linter** - Automatic formatting rules
- **Git** - Version control integration (optional)

#### **Templater Configuration:**
```
Templater Settings:
✅ Template folder location: templates/
✅ Trigger Templater on new file creation: ON
✅ Enable Folder Templates: ON
✅ Startup Templates: Configure based on needs
```

#### **Dataview Configuration:**
```
Dataview Settings:
✅ Enable JavaScript Queries: ON (for advanced queries)
✅ Enable Inline Queries: ON
✅ Enable Dataview JS Queries: ON
```

### **4. Vault Structure Recommendations**

#### **Folder Organization:**
```
vault-root/
├── templates/              # Template files
├── assets/                 # Images, attachments
├── daily-notes/            # Daily notes (if using)
├── projects/              # Project-specific notes
├── areas/                 # Areas of responsibility
├── resources/             # Reference materials
├── archive/               # Completed/old content
├── inbox/                 # Unsorted/new notes
└── scripts/               # Professional markdown toolkit (optional)
```

#### **Installing Scripts in Your Vault**
For maximum convenience, you can place the Professional Markdown Toolkit directly in your vault:

```bash
# Navigate to your vault
cd /path/to/your/obsidian/vault

# Clone the toolkit (if using Git)
git clone https://github.com/ronanchris/professional-markdown-toolkit.git scripts

# Or copy the scripts folder
cp -r /path/to/professional-markdown-toolkit/ scripts/
```

#### **Configure Vault Exclusions**
To prevent scripts from cluttering your vault interface:

**Core Plugin Exclusions:**
```
Settings > Core plugins > Search:
Excluded files: path:scripts/

Settings > Core plugins > Graph view:
Files: path:-scripts/

Settings > Files & Links:
Excluded files: scripts/
```

**Obsidian Publish Exclusions** *(IMPORTANT - Prevents scripts from appearing on public sites)*:
```
Settings > Core plugins > Publish:
⚠️  CRITICAL: Add these to "Excluded files":
- scripts/                    # Entire scripts folder
- .cursorrules               # AI editing rules
- .gitignore                 # Git configuration
- LICENSE                    # License file
- requirements.txt           # Python dependencies
- *.py                       # All Python scripts
- *.sh                       # All shell scripts
- *.log                      # Log files
- consolidated-document/     # Generated documents (if desired)
```

**Obsidian Sync Exclusions** *(RECOMMENDED - Choose based on workflow)*:

*Option 1: Sync scripts across devices (recommended for most users)*
```
Settings > Core plugins > Sync > Settings > Selective sync:
✅ Keep scripts/ folder synced
⚠️  Add to excluded files:
- scripts/consolidated-document/    # Don't sync generated files
- scripts/**/output/               # Don't sync script outputs  
- scripts/**/*.log                 # Don't sync log files
```

*Option 2: Don't sync scripts (for device-specific automation)*
```
Settings > Core plugins > Sync > Settings > Selective sync:
❌ Exclude folders:
- scripts/                         # Don't sync entire scripts folder
Note: You'll need to install scripts manually on each device
```

**Community Plugin Exclusions:**
```
# If using Dataview plugin
Settings > Dataview:
Add to excluded folders: scripts/

# If using Tag Wrangler
Settings > Tag Wrangler:
Ignore folders: scripts/
```

#### **Template Examples:**
Create these templates in your `templates/` folder:

**Daily Note Template (`templates/daily-note.md`):**
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
type: daily-note
tags: [daily]
---

# {{date:YYYY-MM-DD dddd}}

## Today's Focus


## Notes


## Tasks
- [ ] 

## Links Created Today
```

**Project Template (`templates/project.md`):**
```markdown
---
title: {{title}}
created: {{date:YYYY-MM-DD}}
modified: {{date:YYYY-MM-DD}}
type: project
status: active
tags: [project]
---

# {{title}}

## Overview


## Goals
- 

## Resources
- 

## Notes

```

## ⚙️ Cursor Configuration

### **1. Install Essential Extensions**

#### **Must-Have Extensions:**
```
Extensions to install in Cursor:
✅ Markdown All in One - Enhanced markdown editing
✅ YAML - Better YAML frontmatter support
✅ GitLens - Advanced Git integration
✅ Regex Preview - Visual regex testing
✅ Path Intellisense - File path autocompletion
✅ Error Lens - Inline error/warning display
✅ Better Comments - Colored comment styling
```

#### **Optional but Helpful:**
```
✅ Markdown Preview Enhanced - Advanced preview
✅ Markdown Table Prettifier - Auto-format tables
✅ TODO Highlight - Highlight TODO/FIXME comments
✅ Bracket Pair Colorizer - Visual bracket matching
✅ vscode-icons - Better file icons
```

### **2. Cursor Settings Configuration**

#### **Create/Edit Cursor Settings** (`~/.cursor/User/settings.json`):

```json
{
    // Markdown-specific settings
    "markdown.preview.breaks": true,
    "markdown.preview.linkify": true,
    "markdown.extension.toc.updateOnSave": false,
    "markdown.extension.completion.respectVscodeSearchExclude": true,
    
    // Editor settings for large files
    "editor.largeFileOptimizations": false,
    "editor.maxTokenizationLineLength": 20000,
    "search.maxResults": 10000,
    "search.smartCase": true,
    
    // File associations
    "files.associations": {
        "*.md": "markdown"
    },
    
    // Git settings
    "git.enableSmartCommit": true,
    "git.confirmSync": false,
    "git.autofetch": true,
    
    // Workspace trust
    "security.workspace.trust.untrustedFiles": "open",
    
    // Search and replace
    "search.exclude": {
        "**/node_modules": true,
        "**/bower_components": true,
        "**/.obsidian": true,
        "**/assets": false
    },
    
    // Auto-save for vault editing
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    
    // Line endings (important for cross-platform)
    "files.eol": "\n",
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true
}
```

### **3. Setup .cursorrules File**

#### **Copy Obsidian Rules to Your Vault:**
```bash
# Navigate to your vault directory
cd /path/to/your/obsidian/vault

# Copy the rules template
cp /path/to/professional-markdown-toolkit/obsidian-cursor-workflow/cursor-rules-obsidian.md .cursorrules

# Edit to customize for your specific vault
cursor .cursorrules
```

#### **Key Rules Explained:**

**YAML Frontmatter Protection:**
- Prevents AI from accidentally removing metadata
- Ensures consistent date formats
- Maintains template compatibility

**WikiLink Preservation:**
- Protects `[[internal-links]]` from being converted to markdown links
- Preserves block references and embeds
- Maintains Obsidian's linking system

**Content Safety:**
- Never modifies meaning, only formatting
- Preserves voice and tone
- Protects code blocks and special syntax

## 🖥️ Markdown Viewer Optimization

### **1. Obsidian Preview Settings**

#### **Reading View Configuration:**
```
Settings > Editor > Reading view:
✅ Readable line length: ON (for better readability)
✅ Strict line breaks: OFF
✅ Show frontmatter: Based on preference
```

#### **Live Preview Settings:**
```
Settings > Editor > Live Preview:
✅ Show frontmatter: Based on preference  
✅ Show indentation guides: ON
✅ Show line numbers: Based on preference
```

### **2. Cursor Markdown Preview**

#### **Configure Markdown Preview:**
```
Cursor Settings:
"markdown.preview.fontSize": 14,
"markdown.preview.lineHeight": 1.6,
"markdown.preview.fontFamily": "system-ui, sans-serif",
"markdown.preview.theme": "light", // or "dark"
```

#### **Enable Enhanced Preview:**
If using Markdown Preview Enhanced extension:
```
✅ Enable math typesetting
✅ Enable mermaid diagrams  
✅ Enable code chunk execution (careful with this)
✅ Live update preview
```

## 🔄 Git Integration Setup

### **1. Vault-Level Git Configuration**

#### **Initialize Git in Your Vault:**
```bash
cd /path/to/your/obsidian/vault
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

#### **Create Vault .gitignore:**
```gitignore
# Obsidian workspace files
.obsidian/workspace*
.obsidian/hotkeys.json
.obsidian/appearance.json
.obsidian/workspace.json

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Temporary files
*.tmp
.temp/

# Cursor files (optional)
.cursor/

# Log files
*.log

# Script-generated files (if scripts are in vault)
scripts/consolidated-document/
scripts/*/output/
scripts/*/*.log

# Large binary files (adjust as needed)
*.pdf
*.mp4
*.avi
*.mov
```

#### **Git Submodule Approach** *(recommended for scripts in vault)*
If you want to keep the toolkit updated while having it in your vault:

```bash
# Add toolkit as a Git submodule
cd /path/to/your/vault
git submodule add https://github.com/ronanchris/professional-markdown-toolkit.git scripts

# Update submodule when needed
git submodule update --remote scripts

# Clone vault with submodules on new device
git clone --recurse-submodules /path/to/your/vault
```

### **2. Cursor Git Integration**

#### **GitLens Configuration:**
```json
{
    "gitlens.views.repositories.location": "scm",
    "gitlens.views.fileHistory.location": "explorer",
    "gitlens.views.lineHistory.location": "explorer",
    "gitlens.codeLens.enabled": true,
    "gitlens.currentLine.enabled": true,
    "gitlens.blame.highlight.enabled": true
}
```

## 🚀 Workflow Optimization

### **1. Keyboard Shortcuts**

#### **Essential Cursor Shortcuts for Obsidian Work:**
```
Ctrl/Cmd + Shift + F - Global search across vault
Ctrl/Cmd + Shift + H - Global find and replace
Ctrl/Cmd + G - Go to line (useful for large files)
Ctrl/Cmd + Shift + P - Command palette
F12 - Go to definition (works with some markdown links)
Ctrl/Cmd + ` - Open terminal (for running scripts)
```

#### **Configure Custom Keybindings** (`keybindings.json`):
```json
[
    {
        "key": "ctrl+shift+o",
        "command": "workbench.action.quickOpen"
    },
    {
        "key": "ctrl+shift+e",
        "command": "workbench.view.explorer"
    }
]
```

### **2. Workspace Setup**

#### **Recommended Panel Layout:**
```
Left Panel:
✅ File Explorer (primary)
✅ Search results
✅ Git changes (GitLens)

Right Panel:  
✅ Markdown preview (when needed)
✅ Problems panel
✅ Terminal (bottom panel)

Bottom Panel:
✅ Terminal for running scripts
✅ Output panel for extension messages
```

### **3. Multi-Vault Management**

#### **Workspace File for Multiple Vaults:**
```json
{
    "folders": [
        {
            "name": "Main Vault",
            "path": "/path/to/main/vault"
        },
        {
            "name": "Work Vault", 
            "path": "/path/to/work/vault"
        },
        {
            "name": "Archive Vault",
            "path": "/path/to/archive/vault"
        }
    ],
    "settings": {
        "files.exclude": {
            "**/.obsidian": true
        }
    }
}
```

## 🔍 Advanced Tips and Tricks

### **1. Bulk Operations**

#### **Using Cursor's Multi-Cursor:**
- `Ctrl/Cmd + D` - Select next occurrence
- `Ctrl/Cmd + Shift + L` - Select all occurrences
- `Alt + Click` - Add cursor at position
- Perfect for bulk metadata updates

#### **Regex Find/Replace Examples:**
```regex
# Fix inconsistent heading spacing
Find: ^(#+)([^\s])
Replace: $1 $2

# Standardize date formats in frontmatter
Find: created: (\d{1,2})/(\d{1,2})/(\d{4})
Replace: created: $3-$2-$1

# Add missing YAML frontmatter
Find: ^(?!---)(.*)
Replace: ---\ntitle: $1\ncreated: {{date}}\n---\n$1
```

### **2. Search and Analysis**

#### **Powerful Search Patterns:**
```
# Find notes without frontmatter
^[^-]

# Find orphaned notes (no backlinks - use with GitLens)
Search for files not mentioned in other files

# Find empty or stub notes
^\s*$|^#{1,6}\s+.+\s*$

# Find broken WikiLinks
\[\[.*\]\](?!\()
```

### **3. Quality Assurance**

#### **Pre-Commit Checklist:**
```bash
# Run these commands before major commits:

# 1. Check for broken frontmatter
grep -r "^---" vault/ | grep -v "^---$"

# 2. Validate YAML frontmatter
python -c "import yaml; [yaml.safe_load(open(f).read().split('---')[1]) for f in glob.glob('**/*.md', recursive=True) if '---' in open(f).read()]"

# 3. Run cleanup scripts
python scripts/markdown-processing/cleanup_markdown_batch.py vault/ --dry-run

# 4. Check Git status
git status
```

## 🛠️ Troubleshooting

### **Common Issues and Solutions**

#### **Sync Conflicts Between Obsidian and Cursor:**
```
Problem: Files getting corrupted when both apps are open
Solution: 
1. Close Obsidian before major Cursor operations
2. Use Git to track changes
3. Enable auto-save delay in Cursor
4. Use file watchers to detect external changes
```

#### **Performance Issues with Large Vaults:**
```
Problem: Slow search/indexing in Cursor
Solutions:
1. Exclude .obsidian folder from search
2. Use workspace-specific settings
3. Increase tokenization limits
4. Process subfolders individually
```

#### **Broken WikiLinks After Bulk Operations:**
```
Problem: Links not working in Obsidian after Cursor edits
Solution:
1. Check .cursorrules are properly configured
2. Use Obsidian's "Update internal links" feature
3. Run link verification scripts
4. Restore from Git if needed
```

## 📚 Next Steps

### **After Setup:**
1. **Test the workflow** with a small subset of notes
2. **Run the provided scripts** to clean up formatting
3. **Establish a routine** for vault maintenance
4. **Create backups** and version control workflow
5. **Customize** rules and settings for your specific needs

### **Advanced Workflows:**
- Set up automated backup scripts
- Create custom metadata schemas
- Implement team collaboration workflows  
- Develop project-specific templates
- Build analytics and reporting systems

---

**Remember**: This setup is designed to be powerful but safe. Always backup your vault before making major changes, and test new workflows on small subsets of content first.

The goal is to create a seamless experience where Obsidian handles daily note-taking and exploration, while Cursor manages bulk operations, quality control, and professional document generation. 