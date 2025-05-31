# Professional Markdown Toolkit

**A comprehensive collection of production-ready scripts for Obsidian vault management and markdown processing.**

**Context**: Professional scripts collection for Obsidian vault management, markdown processing, and automated workflows

## 🎯 **Two Ways to Use This Toolkit**

This toolkit is designed to be accessible to everyone, regardless of technical comfort level:

- **🖥️ Terminal Users**: Direct command-line usage with full control
- **🤖 AI-Assisted Users**: Step-by-step guidance through Cursor AI

**Both approaches are equally valid and powerful!** Choose what feels comfortable to you.

*New to terminal commands?* The Cursor AI approach will teach you as you go, turning every interaction into a learning opportunity without the intimidation factor.

## 📋 **Prerequisites & Dependencies**

### **Required Obsidian Plugins**
This toolkit is designed for advanced Obsidian workflows and requires:

- **[Templater](https://github.com/SilentVoid13/Templater)** ⚠️ **ESSENTIAL** - Core template functionality
  - Processes `<%* ... -%>` code blocks
  - Handles `` `= this.file.name` `` references  
  - Required for template scripts (`apply_template.sh`, `fix_template.sh`)
- **[Dataview](https://github.com/blacksmithgu/obsidian-dataview)** (Optional) - For advanced analytics

### **System Requirements**
- **Python 3.7+** with PyYAML (`pip install -r requirements.txt`)
- **Bash shell** (macOS/Linux) or WSL (Windows)
- **Obsidian vault** with `scripts/` folder structure

### **Templater Configuration**
If using Templater-dependent scripts:
1. Install Templater plugin in Obsidian
2. Enable "Trigger Templater on new file creation"
3. Set template folder if using templates (optional)

⚠️ **Note**: Scripts will work without Templater but may show warnings for unprocessed Templater syntax.

## 📁 **Directory Structure**

- **Core Tools** (`metadata-tools/`, `obsidian-tools/`, `markdown-processing/`) - Universal Obsidian vault management
- **Workflow Integration** (`obsidian-cursor-workflow/`) - Cursor AI editor integration with Obsidian  
- **Shared Resources** (`shared/`) - Common backup and utility functions

```
scripts/
├── metadata-tools/              # YAML frontmatter and metadata management  
├── obsidian-tools/             # Obsidian-specific template and structure tools
├── markdown-processing/        # General markdown cleanup and processing
├── obsidian-cursor-workflow/   # Cursor AI editor integration guide
└── shared/                     # Shared backup and utility functions
```

## 🛠️ **Core Tool Categories**

### **Metadata Management (`metadata-tools/`)**
**Professional YAML frontmatter and metadata processing**

#### **`remove_metadata.sh`** **PRODUCTION METADATA REMOVAL**
**Purpose**: Clean removal of YAML frontmatter and templater code
**Templater Integration**: Removes Templater syntax (`<%* ... -%>`, `` `= this.file.name` ``)
**Features**: 
- ✅ Comprehensive backup system with restoration
- ✅ YAML frontmatter detection and removal
- ✅ Templater code block cleaning (`<%* ... -%>`)
- ✅ `= this.file.name` reference removal
- ✅ Professional error handling and user feedback

**Usage**:
```bash
# Basic usage with automatic backups
scripts/metadata-tools/remove_metadata.sh

# Advanced usage without backups
scripts/metadata-tools/remove_metadata.sh --no-backup
```

**Output**: Professional-grade cleaning with detailed backup information

#### **`fix_metadata.sh`** & **`clean_files.sh`**
**Purpose**: Advanced metadata cleaning and standardization  
**Features**: Template code removal, metadata normalization, content preservation

### **Obsidian Integration (`obsidian-tools/`)**
**Professional Obsidian vault structure and template management**

#### **Template Management Scripts** ⚠️ **Requires Templater**
- **`apply_template.sh`** - Apply inbox templates to markdown files (includes Templater code)
- **`fix_template.sh`** - Repair and standardize template formatting (processes Templater syntax)
- **`apply_inbox_template.py`** - Python-based template application with dry-run mode

#### **Metadata Processing**
- **`apply_moc_template_preserve_metadata.py`** - MOC template application with metadata preservation

### **Markdown Processing (`markdown-processing/`)**
**Professional markdown formatting and cleanup**

#### **`cleanup_markdown_batch.py`** **COMPREHENSIVE MARKDOWN CLEANER**
**Purpose**: Batch markdown formatting and whitespace normalization  
**Features**: 
- ✅ Recursive directory processing
- ✅ YAML frontmatter preservation  
- ✅ Bullet point and list formatting optimization
- ✅ Comprehensive whitespace cleanup
- ✅ Dry-run mode for safe testing
- ✅ Detailed progress reporting

#### **`clean_all_markdown.sh`** **VAULT-WIDE PROCESSING**
**Purpose**: Execute markdown cleanup across entire Obsidian vault

### **Cursor Integration (`obsidian-cursor-workflow/`)**
**Complete integration guide for using Cursor AI editor with Obsidian**

#### **Core Integration Files**
- **`cursor-rules-obsidian.md`** - Cursor AI rules optimized for Obsidian workflows
- **`cursor-prompts-guide.md`** - 200+ professional prompts for Obsidian tasks
- **`obsidian-cursor-setup.md`** - Complete setup and configuration guide
- **`vault-analytics.py`** - Comprehensive vault analysis and insights

## 🚀 **Quick Start Guide**

### **Installation**

**Choose your comfort level:**

#### **🖥️ Terminal-Savvy Users**
```bash
# Clone into your Obsidian vault
cd /path/to/your/obsidian-vault
git clone https://github.com/ronanchris/professional-markdown-toolkit.git scripts
```

#### **🤖 Prefer AI Guidance?**
1. **Download Cursor** (free from cursor.sh) if you don't have it
2. **Open your Obsidian vault in Cursor**: File > Open Folder > Select your vault
3. **Let Cursor help you install**: Type this into Cursor's chat:

```
I want to install the Professional Markdown Toolkit in my Obsidian vault. Can you:

1. Help me safely clone or download the toolkit into my vault's scripts folder
2. Explain what each step does as we go
3. Install any needed dependencies (like Python packages)
4. Show me how to test that everything is working
5. Walk me through running my first script safely

My vault is located at: [paste your vault path here]
```

**Cursor will handle everything step-by-step and explain what's happening!**

### **Basic Usage**

#### **🖥️ Command Line**
```bash
# Clean metadata from inbox files (with backup)
scripts/metadata-tools/remove_metadata.sh

# Apply templates to files  
scripts/obsidian-tools/apply_template.sh

# Clean up markdown formatting vault-wide
scripts/markdown-processing/clean_all_markdown.sh --dry-run
```

#### **🤖 With Cursor's Help**
**Ask Cursor**: *"I want to clean up metadata in my inbox folder. Can you help me run the right script safely and explain what it does?"*

**Cursor will:**
- Guide you to the right script for your task
- Explain what the script does before running it
- Help you understand the backup system
- Show you how to restore files if needed
- Suggest the best options for your situation

### **Advanced Features**
```bash
# Disable backups for advanced users
scripts/metadata-tools/remove_metadata.sh --no-backup

# Recursive markdown cleanup with verbose output
scripts/markdown-processing/clean_all_markdown.sh --verbose

# Vault analytics and insights
python scripts/obsidian-cursor-workflow/vault-analytics.py
```

## 📚 **Integration Workflows**

### **Standard Obsidian Workflow**
1. **Metadata Management** → Clean and standardize YAML frontmatter
2. **Template Application** → Apply consistent structure to notes  
3. **Content Processing** → Format and clean markdown content
4. **Analytics & Insights** → Understand vault structure and optimization opportunities

### **Cursor AI Enhanced Workflow**  
1. **Setup Integration** → Configure Cursor with Obsidian-optimized rules
2. **Use Professional Prompts** → Leverage 200+ tested prompts for content creation
3. **Automate Processing** → Use scripts for repetitive markdown tasks
4. **Analyze & Optimize** → Use analytics to improve vault structure

## 🔧 **Technical Features**

### **Enterprise-Grade Reliability**
- **Comprehensive backup system** → Automatic file protection with easy restoration
- **Error handling** → Professional error messages and graceful failure handling  
- **Input validation** → Robust parameter checking and path validation
- **Cross-platform compatibility** → Works on macOS, Linux, and Windows WSL

### **Professional Documentation**
1. **Professional header formatting** → Clean, consistent presentation
2. **Comprehensive progress reporting** → Detailed operation feedback
3. **Advanced error recovery** → Clear instructions for problem resolution
4. **Extensive configuration options** → Customizable for different use cases

### **Security & Safety**
- **No hardcoded paths** → Works in any vault structure
- **Safe file operations** → No risk of data loss with backup system
- **Dependency validation** → Clear error messages for missing requirements
- **Professional coding standards** → Enterprise-grade shell and Python practices

## 🎯 **Advanced Configuration**

### **Backup System**
All destructive operations automatically create timestamped backups:
```bash
# Backup location: scripts/backups/YYYYMMDD_HHMMSS/
# Restore instructions provided after each operation
```

### **Customization Options**
- **Vault structure detection** → Automatically adapts to your folder organization
- **Template customization** → Modify templates for your specific needs  
- **Processing scope control** → Target specific directories or file types
- **Output formatting** → Customize progress reports and feedback

## 📖 **Documentation & Support**

- **`README.md`** → This comprehensive guide
- **`TEMPLATER-INTEGRATION.md`** → Complete Templater plugin integration guide
- **`SECURITY-AUDIT.md`** → Detailed security analysis and validation
- **`PROJECT-SECURITY-PLAN.md`** → Development roadmap and testing plans
- **`CONTRIBUTING.md`** → Contribution guidelines and development standards

### **Cursor AI Integration**
- **`obsidian-cursor-workflow/README.md`** → Complete Cursor integration guide
- **`cursor-prompts-guide.md`** → Professional prompt library for content creation
- **`troubleshooting-guide.md`** → Common issues and solutions

## 🚀 **Production Readiness**

This toolkit is designed for professional use with:
- **Enterprise backup systems** → No data loss risk
- **Professional error handling** → Clear recovery instructions  
- **Comprehensive testing** → Validated across multiple environments
- **Security audited** → No hardcoded paths or security vulnerabilities
- **Cross-platform support** → macOS, Linux, Windows WSL compatibility

**Status**: ✅ **Production Ready** - Comprehensive security audit completed, full backup system implemented

## 🚀 **Future Roadmap**

### **Multi-Edition Strategy** (Planned)
This toolkit currently focuses on **Templater plugin integration**. Future development will include:

- **📦 Core Templates Edition** - Support for Obsidian's built-in Core Templates (`{{title}}`, `{{date}}` syntax)
- **📦 Universal Edition** - Multi-template system support with auto-detection
- **📦 Template-Agnostic Tools** - Processing tools that work regardless of template system

**Current Focus**: Templater Edition (fully functional)  
**Next Priority**: Community feedback and Core Templates research  
**Timeline**: Based on user demand and contribution availability

See `PROJECT-SECURITY-PLAN.md` for detailed roadmap and implementation phases.

## 📄 **License**

MIT License - See `LICENSE` and `LICENSE-EXPLAINED.md` for complete details.

**Free for commercial and personal use** - No restrictions, just keep the license text. 