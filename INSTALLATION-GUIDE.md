# Installation Guide for Cursor & Obsidian Users

**Complete setup guide for integrating the Markdown Toolkit into your Cursor IDE and Obsidian projects.**

## 🎯 Overview

This guide shows you how to install and integrate the Professional Markdown Toolkit into your Cursor IDE and Obsidian vault for seamless markdown processing.

## 🚀 Quick Installation

### **Option 1: Install in Your Obsidian Vault** (Recommended)
```bash
# Navigate to your Obsidian vault
cd /path/to/your/obsidian-vault

# Clone the toolkit into a tools directory
git clone https://github.com/ronanchris/professional-markdown-toolkit-v2.git tools/markdown-toolkit

# Install the toolkit
cd tools/markdown-toolkit/markdown-toolkit
./install.sh
```

### **Option 2: Install in Your Cursor Project**
```bash
# Navigate to your Cursor project
cd /path/to/your/cursor-project

# Clone the toolkit
git clone https://github.com/ronanchris/professional-markdown-toolkit-v2.git .markdown-toolkit

# Install the toolkit
cd .markdown-toolkit/markdown-toolkit
./install.sh
```

## 📁 Recommended Project Structure

### **For Obsidian Vaults:**
```
your-obsidian-vault/
├── .obsidian/                    # Obsidian config
├── tools/                        # Your tools directory
│   └── markdown-toolkit/         # This toolkit
│       ├── tools/                # Processing scripts
│       ├── shared/               # Shared utilities
│       └── install.sh           # Installation script
├── docs/                         # Your documentation
├── notes/                        # Your notes
└── README.md                     # Your project README
```

### **For Cursor Projects:**
```
your-cursor-project/
├── .markdown-toolkit/            # Hidden toolkit directory
│   ├── tools/                    # Processing scripts
│   ├── shared/                   # Shared utilities
│   └── install.sh               # Installation script
├── docs/                         # Your documentation
├── content/                      # Your markdown content
└── README.md                     # Your project README
```

## 🛠️ Cursor IDE Integration

### **1. Terminal Integration**
Open Cursor's integrated terminal and run:
```bash
# Navigate to your project
cd /path/to/your/project

# Use the tools directly
python .markdown-toolkit/tools/cleanup_markdown_batch.py
python .markdown-toolkit/tools/notion_complete_fixer.py your-file.md
```

### **2. Task Runner Integration**
Create a `.vscode/tasks.json` file in your project:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Clean Markdown",
      "type": "shell",
      "command": "python",
      "args": [".markdown-toolkit/tools/cleanup_markdown_batch.py"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "Fix Notion Import",
      "type": "shell",
      "command": "python",
      "args": [".markdown-toolkit/tools/notion_complete_fixer.py", "${file}"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

### **3. Keyboard Shortcuts**
Add to your Cursor keybindings (`Ctrl/Cmd + K, Ctrl/Cmd + S`):
```json
[
  {
    "key": "ctrl+shift+m",
    "command": "workbench.action.tasks.runTask",
    "args": "Clean Markdown"
  },
  {
    "key": "ctrl+shift+n",
    "command": "workbench.action.tasks.runTask",
    "args": "Fix Notion Import"
  }
]
```

## 📝 Obsidian Integration

### **1. Shell Commands Plugin**
Install the "Shell commands" plugin in Obsidian and add these commands:

**Clean Current File:**
```bash
python tools/markdown-toolkit/tools/cleanup_markdown.py "${file}"
```

**Fix Notion Import:**
```bash
python tools/markdown-toolkit/tools/notion_complete_fixer.py "${file}"
```

### **2. Templater Plugin Integration**
Add to your Templater scripts:
```javascript
// Clean markdown before processing
const { execSync } = require('child_process');
const cleanedContent = execSync(`python tools/markdown-toolkit/tools/cleanup_markdown.py "${tp.file.path()}"`, { encoding: 'utf8' });
```

### **3. Quick Actions**
Create quick action buttons in Obsidian:
- **Clean Formatting**: Runs cleanup on current file
- **Prepare for Notion**: Runs Notion fixer on current file
- **Batch Clean**: Runs cleanup on all files in current folder

## 🔧 Advanced Setup

### **Environment Variables**
Add to your shell profile (`.bashrc`, `.zshrc`, etc.):
```bash
# Add toolkit to PATH
export MARKDOWN_TOOLKIT="/path/to/your/project/tools/markdown-toolkit"
export PATH="$MARKDOWN_TOOLKIT/tools:$PATH"

# Create aliases for common commands
alias mdclean="python $MARKDOWN_TOOLKIT/tools/cleanup_markdown_batch.py"
alias mdnotion="python $MARKDOWN_TOOLKIT/tools/notion_complete_fixer.py"
```

### **Git Integration**
Add to your `.gitignore`:
```gitignore
# Ignore processed files (optional)
*-cleaned.md
*-notion-ready.md
*.backup

# Keep toolkit in version control
!tools/markdown-toolkit/
!.markdown-toolkit/
```

### **Automated Workflows**
Create a pre-commit hook (`.git/hooks/pre-commit`):
```bash
#!/bin/bash
# Clean markdown files before committing
find . -name "*.md" -not -path "./tools/*" -not -path "./.markdown-toolkit/*" | \
  xargs python tools/markdown-toolkit/tools/cleanup_markdown.py
```

## 🎯 Usage Examples

### **In Cursor Terminal:**
```bash
# Clean all markdown in current directory
python .markdown-toolkit/tools/cleanup_markdown_batch.py

# Fix specific file for Notion
python .markdown-toolkit/tools/notion_complete_fixer.py docs/important-note.md

# Analyze what needs fixing
python .markdown-toolkit/tools/notion_complete_fixer.py docs/important-note.md --analyze
```

### **In Obsidian:**
1. Open command palette (`Ctrl/Cmd + P`)
2. Run "Shell commands: Clean Current File"
3. Or use quick action buttons

### **Batch Processing:**
```bash
# Clean all markdown files in your project
find . -name "*.md" -not -path "./tools/*" | \
  xargs python tools/markdown-toolkit/tools/cleanup_markdown.py

# Prepare all files for Notion import
find . -name "*.md" -not -path "./tools/*" | \
  xargs python tools/markdown-toolkit/tools/notion_complete_fixer.py
```

## 🚨 Troubleshooting

### **Common Issues:**

#### **"Command not found"**
**Solution:** Make sure you're in the correct directory and the toolkit is installed:
```bash
cd /path/to/your/project
ls tools/markdown-toolkit/tools/  # Should show the Python scripts
```

#### **"Permission denied"**
**Solution:** Make scripts executable:
```bash
chmod +x tools/markdown-toolkit/tools/*.py
chmod +x tools/markdown-toolkit/tools/*.sh
```

#### **"Python not found"**
**Solution:** Install Python 3.7+ and ensure it's in your PATH:
```bash
python3 --version  # Should show Python 3.7+
```

### **Cursor-Specific Issues:**

#### **Terminal not recognizing commands**
**Solution:** Restart Cursor or reload the terminal window after installation.

#### **Task runner not working**
**Solution:** Check that the paths in `tasks.json` match your actual project structure.

### **Obsidian-Specific Issues:**

#### **Shell commands plugin not working**
**Solution:** 
1. Enable the plugin in Obsidian settings
2. Check that the Python path is correct
3. Test commands in terminal first

#### **Permission issues on macOS/Linux**
**Solution:** Make sure the toolkit directory has proper permissions:
```bash
chmod -R 755 tools/markdown-toolkit/
```

## 📚 Next Steps

After installation:

1. **Test the setup** with a sample markdown file
2. **Configure your workflow** using the examples above
3. **Read the main README** for detailed tool usage
4. **Explore the documentation** in `docs/` for advanced features

## 🆘 Support

- **Main Documentation**: See `README.md` for tool details
- **Notion Guide**: See `docs/NOTION-IMPORT-GUIDE.md` for Notion-specific help
- **Issues**: Create an issue on GitHub for bugs or feature requests

---

**Happy markdown processing! 🎉**