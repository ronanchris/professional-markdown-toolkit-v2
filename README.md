# Professional Markdown Toolkit - Executive Document Automation

**Purpose**: Comprehensive automation toolkit for document processing and project maintenance  
**Created**: 30 May 2025  
**Context**: Professional scripts collection for executive business analysis and markdown processing  

**Primary Use Case**: Designed for power users who manage large Obsidian vaults or markdown collections using Cursor as a companion editor for bulk operations, metadata management, and automated processing.

**Organization**: 
- **Universal Scripts** (`markdown-processing/`, `obsidian-tools/`, `metadata-tools/`) - Copy these to other projects
- **Project-Specific** (`company-executive/`) - Example executive document generation (customize for your organization)
- **Obsidian Workflow** (`obsidian-cursor-workflow/`) - Specialized guidance for Cursor + Obsidian users  


## **Organized Directory Structure**

```
scripts/
├── readme-project-overview.md                    # This comprehensive guide
├── company-executive/           # Example executive document generation
├── markdown-processing/         # UNIVERSAL - Advanced markdown cleanup and formatting
├── obsidian-tools/             # UNIVERSAL - Obsidian vault management utilities
├── metadata-tools/             # UNIVERSAL - YAML frontmatter and metadata processing
└── obsidian-cursor-workflow/   # Cursor + Obsidian workflow guidance and rules
```


## **Script Categories**

### **Executive Document Generation (`company-executive/`)**
**Example executive document consolidation workflow (customize for your organization)**

#### **`build-consolidated-doc.sh`** **EXECUTIVE CONSOLIDATION SCRIPT**
**Purpose**: Automated document consolidation for executive distribution  
**Function**: Combines multiple source documents into single professional report  
**Last Updated**: 31 May 2025 - Organized into company-executive subfolder  
**Created**: 30 May 2025 - Initial automation system  
**Scope**: Example implementation (customize for your organization)

**Usage** (can be run from anywhere):
```bash
# From anywhere in the repository
scripts/company-executive/build-consolidated-doc.sh

# Or navigate to the script directory
cd scripts/company-executive
./build-consolidated-doc.sh
```

**Output Location**: Always outputs to `consolidated-document/Executive-Analysis-Complete.md`

**Features**:
- ✅ Combines multiple documents in logical executive order
- ✅ Professional header formatting with contact information  
- ✅ Unicode-safe emoji cleanup for executive-level presentation
- ✅ Source attribution for audit trail
- ✅ Error handling for missing files
- ✅ Obsidian-compatible formatting (no YAML frontmatter conflicts)
- ✅ Executive-ready 236KB output document

### **🧹 Markdown Processing (`markdown-processing/`)**
**Advanced whitespace cleanup and formatting normalization**

#### **`cleanup_markdown_batch.py`** **RECOMMENDED for Files/Folders**
**Purpose**: Comprehensive markdown formatting cleanup with advanced processing  
**Features**: Line-by-line analysis, list formatting, robust whitespace handling

```bash
# Process a single file (thorough cleaning)
python scripts/markdown-processing/cleanup_markdown_batch.py path/to/file.md

# Process all markdown files in a directory
python scripts/markdown-processing/cleanup_markdown_batch.py path/to/directory

# Process recursively with detailed output
python scripts/markdown-processing/cleanup_markdown_batch.py path/to/directory --recursive --verbose
```

#### **`clean_all_markdown.sh`** **RECOMMENDED for Entire Vault**
**Purpose**: One-command cleanup for entire Obsidian vault  
**Engine**: Uses `cleanup_markdown_batch.py` for comprehensive processing

```bash
# Clean entire vault
scripts/markdown-processing/clean_all_markdown.sh

# Preview changes without applying
scripts/markdown-processing/clean_all_markdown.sh --dry-run

# Detailed processing information
scripts/markdown-processing/clean_all_markdown.sh --verbose
```

#### **`cleanup_markdown.py`**
**Purpose**: Basic single-file markdown cleanup  
**Note**: For production use, prefer `cleanup_markdown_batch.py` for superior results

### ** Obsidian Tools (`obsidian-tools/`)**
**Template management and vault organization utilities**

#### **Template Application Scripts**
- **`apply_inbox_template.py`** - Apply inbox templates to individual notes
- **`apply_inbox_template_to_folder.py`** - Batch apply templates to entire folders
- **`apply_moc_template_preserve_metadata.py`** - MOC templates with metadata preservation
- **`update_inbox_with_template.py`** - Update existing notes with template content

#### **Convenience Wrappers**
- **`apply_template.sh`** - Shell wrapper for template operations
- **`fix_template.sh`** - Template repair and maintenance

```bash
# Apply inbox template to specific file
python scripts/obsidian-tools/apply_inbox_template.py path/to/note.md

# Batch apply to folder
python scripts/obsidian-tools/apply_inbox_template_to_folder.py path/to/folder/
```

### ** Metadata Tools (`metadata-tools/`)**
**YAML frontmatter and metadata processing utilities**

#### **Core Metadata Scripts**
- **`safe_metadata_removal.py`** - Safely remove metadata while preserving content
- **`update_date_created_to_templater.py`** - Convert date formats for Templater compatibility

#### **Shell Wrappers**
- **`clean_files.sh`** - Batch file cleanup operations
- **`fix_metadata.sh`** - Metadata repair and normalization
- **`remove_metadata.sh`** - Safe bulk metadata removal

```bash
# Safely remove metadata from file
python scripts/metadata-tools/safe_metadata_removal.py path/to/note.md

# Update date formatting for Templater
python scripts/metadata-tools/update_date_created_to_templater.py path/to/note.md
```

### **✍️ Cursor as a Writing Tool**
**Beyond traditional AI chat interfaces - collaborative writing environment**

Before diving into the Obsidian-specific workflow, it's worth highlighting that **Cursor is an exceptional writing tool on its own**. Unlike ChatGPT, Claude, or Gemini chat interfaces, Cursor provides:

- **Direct document editing** - AI assistance within your actual writing environment
- **Collaborative writing experience** - AI as a writing partner, not a separate chat tool
- **Context-aware suggestions** - AI understands your entire document structure
- **Professional writing workflows** - Version control, formatting, and publishing integration
- **Distraction-free environment** - Focus on writing without switching between chat and editor

**Compatible with Many Writing Tools:**
This approach works excellently with various writing and knowledge management systems:
- **Obsidian** - Networked knowledge management (our primary focus)
- **Notion** - Databases and collaborative documentation  
- **Roam Research** / **LogSeq** - Networked thought and daily notes
- **Dendron** / **Foam** - VSCode-based knowledge management
- **Zettlr** - Academic writing and research
- **Standard Markdown** - Simple files + Git workflow
- **Joplin** / **Bear** - Cross-platform note-taking
- **Any markdown-based system** - The principles apply broadly

*Don't be afraid to use Cursor just for writing alone - it transforms how you interact with AI assistance.*

## **🎯 Cursor + Obsidian Workflow (`obsidian-cursor-workflow/`)**
**Specialized guidance for using Cursor as an Obsidian companion editor**

This toolkit is designed around a powerful workflow: **using Cursor as a companion editor for Obsidian vault management**. While Obsidian excels at note-taking and linking, Cursor provides superior capabilities for bulk operations, metadata management, and automated processing.

#### **Why Cursor + Obsidian?**
- **Bulk Operations** - Process hundreds/thousands of notes simultaneously
- **Advanced Search & Replace** - Regex, multi-file operations, AI-assisted editing
- **Metadata Management** - Efficient YAML frontmatter editing across entire vaults
- **Quality Control** - Automated formatting cleanup and consistency checks
- **AI Assistance** - Smart content processing and pattern recognition
- **Git Integration** - Professional version control for your knowledge base

#### **Complete Workflow Documentation**
- **`obsidian-cursor-setup.md`** - Complete setup guide for both applications
- **`cursor-rules-obsidian.md`** - Comprehensive `.cursorrules` template for vault safety
- **`cursor-prompts-guide.md`** - How to ask Cursor for help (perfect for beginners!)
- **`template-examples.md`** - Professional note templates for different use cases
- **`vault-analytics.py`** - Script to analyze vault health and generate optimization insights
- **`troubleshooting-guide.md`** - Solutions for common workflow issues

#### **Recommended Workflow**
1. **Primary editing** in Obsidian (linking, daily notes, graph view)
2. **Bulk operations** in Cursor (metadata updates, formatting cleanup, reorganization)
3. **Quality assurance** with these scripts (consistency, professional formatting)
4. **Version control** via Git (track changes, backup, collaboration)

#### **Key Use Cases**
- **Large vault maintenance** (10,000+ notes)
- **Template application** across multiple notes
- **Metadata standardization** and cleanup
- **Format migration** (e.g., Roam to Obsidian)
- **Content auditing** and quality improvement
- **Professional document generation** from vault content

See `obsidian-cursor-workflow/` directory for detailed guides, Cursor rules, and best practices.


## **Quick Start Guide**

### **For General Writing (Any Tool)**
```bash
# 1. Install Cursor and open your writing project
cursor /path/to/your/writing/project

# 2. Set up basic .cursorrules for your writing style
echo "Focus on clear, professional writing. Preserve author voice and intent." > .cursorrules

# 3. Use Cursor's AI assistance for:
# - In-context editing suggestions
# - Document structure improvements  
# - Grammar and style refinement
# - Research and fact-checking
# - Collaborative writing sessions

# 4. Clean up markdown formatting (if using markdown)
python scripts/markdown-processing/cleanup_markdown_batch.py . --recursive
```

### **For Executive Document Generation**
```bash
# Generate executive distribution document
cd scripts/company-executive
./build-consolidated-doc.sh
```

### **For Markdown Quality**
```bash
# Clean up markdown formatting issues in entire vault
scripts/markdown-processing/clean_all_markdown.sh --verbose

# Clean specific file or folder
python scripts/markdown-processing/cleanup_markdown_batch.py path/to/target --recursive
```

### **For Obsidian Management**
```bash
# Apply templates to inbox
python scripts/obsidian-tools/apply_inbox_template_to_folder.py path/to/inbox/

# Clean up metadata across vault
scripts/metadata-tools/clean_files.sh
```

### **For Obsidian Users New to Cursor/Python**
**🎯 The Two-Window Workflow - Don't be intimidated!**

You'll work with **TWO applications open**:
1. **Obsidian** - Your normal note-taking (keep this open)
2. **Cursor** - Your "command center" for running scripts (this is where the magic happens)

**Step-by-step for beginners:**
```bash
# 1. Download Cursor (free AI-powered editor)
# Download from: cursor.sh

# 2. Open your vault in Cursor (this is your "command center")
# In Cursor: File > Open Folder > Select your Obsidian vault

# 3. Ask Cursor for help! Copy this prompt into Cursor:
# "I'm an Obsidian user new to Python and Cursor. I want to use the 
#  Professional Markdown Toolkit. Can you guide me through setup step by step?"

# 4. Let Cursor help you install the scripts and run them safely
# Cursor will explain each step and help you test everything first
```

**Key insight**: You don't need to know Python! Cursor will teach you everything step by step. See `obsidian-cursor-workflow/cursor-prompts-guide.md` for exactly what to ask Cursor.

### **For Cursor + Obsidian Power Users**
```bash
# 1. First-time setup (follow complete guide)
open obsidian-cursor-workflow/obsidian-cursor-setup.md

# 2. Install scripts in your vault (recommended)
cd /path/to/your/vault
git clone https://github.com/ronanchris/professional-markdown-toolkit.git scripts

# 3. Set up your vault for Cursor editing
cp scripts/obsidian-cursor-workflow/cursor-rules-obsidian.md .cursorrules

# 4. Configure Obsidian exclusions (see setup guide)
# Settings > Search/Graph/Publish: Exclude scripts/ folder

# 5. Analyze your vault health
python scripts/obsidian-cursor-workflow/vault-analytics.py .

# 6. Open vault in Cursor for bulk operations
cursor .

# 7. Run comprehensive vault maintenance
python scripts/markdown-processing/cleanup_markdown_batch.py . --recursive --verbose
```


## **Technical Requirements**

### **Dependencies**
- **Python 3.x** - Required for all `.py` scripts
- **Bash** - Required for all `.sh` scripts
- **Perl** - Required for advanced Unicode regex processing (emoji cleanup)
- **Standard Unix tools** - awk, grep, sed, find, etc.

### **Platform Compatibility**
- **macOS** ✅ - Primary development and testing platform
- **Linux** ✅ - Full compatibility with standard installations
- **Windows** ⚠️ - Requires WSL or similar Unix environment


## **Command-Line Options Reference**

### **Markdown Processing Options**
```bash
# cleanup_markdown_batch.py options
-h, --help       # Show help message
-r, --recursive  # Process subdirectories recursively  
-d, --dry-run    # Preview changes without applying
-v, --verbose    # Show detailed processing information

# clean_all_markdown.sh options
--dry-run        # Preview changes without applying
--verbose        # Show detailed file processing
```

### **Common Usage Patterns**
```bash
# Preview what would be cleaned (safe)
python scripts/markdown-processing/cleanup_markdown_batch.py . --recursive --dry-run

# Apply comprehensive cleanup with feedback
python scripts/markdown-processing/cleanup_markdown_batch.py . --recursive --verbose

# Generate distribution document
scripts/document-generation/build-consolidated-doc.sh
```


## **What Gets Fixed**

### **Markdown Processing Fixes**
1. **Multiple consecutive blank lines** → Single blank line
2. **Extra whitespace between bullet points** → Proper list formatting
3. **Lines with only spaces/tabs** → Clean empty lines
4. **Inconsistent spacing around headers** → Proper markdown formatting
5. **Malformed horizontal rules** → Standard markdown syntax

### **Document Generation Enhancements**
1. **Professional header formatting** → Executive-ready presentation
2. **Emoji cleanup in headers** → Executive-level appropriate formatting
3. **Source attribution** → Clear audit trail
4. **Consistent section numbering** → Logical document flow
5. **YAML frontmatter handling** → Preserved metadata

### **Safety Features**
- **YAML frontmatter preservation** - Never modifies metadata
- **Content integrity** - Only addresses formatting, never content
- **Dry-run modes** - Preview changes before applying
- **Error handling** - Graceful failure with clear messaging
- **Backup recommendations** - Always use version control


## **Vault Integration**

### **⚠️ IMPORTANT: Configure Exclusions First**
Before installing scripts in your vault, configure these critical exclusions to prevent scripts from appearing in published sites or cluttering your interface:

**Obsidian Publish** - Add to excluded files: `scripts/`, `.cursorrules`, `*.py`, `*.sh`  
**Obsidian Sync** - Consider excluding script outputs: `scripts/consolidated-document/`, `scripts/**/output/`  
**Search/Graph** - Add exclusions: `path:scripts/` (search), `path:-scripts/` (graph view)

*See [complete setup guide](obsidian-cursor-workflow/obsidian-cursor-setup.md) for detailed configuration.*

### **Installing Scripts in Your Vault**
You can place these scripts directly in your Obsidian vault for convenient access:

```bash
# Clone or copy the toolkit to your vault
cd /path/to/your/obsidian/vault
git clone https://github.com/your-username/professional-markdown-toolkit.git scripts

# Or copy just the scripts folder
cp -r /path/to/professional-markdown-toolkit/ /path/to/vault/scripts/
```

### **Recommended Exclusions**
To keep scripts from cluttering your vault interface or appearing in published sites:

#### **Obsidian Publish Exclusions**
```
Settings > Core plugins > Publish:
Add to "Excluded files":
- scripts/
- .cursorrules
- .gitignore
- requirements.txt
```

#### **Obsidian Sync Exclusions** *(optional)*
```
Settings > Core plugins > Sync > Settings > Selective sync:
Exclude folders:
- scripts/ (if you don't want scripts synced across devices)
```

#### **Search and Graph Exclusions**
```
Settings > Core plugins > Search:
Add to "Excluded files":
- path:scripts/

Settings > Core plugins > Graph view:
Add to "Files":
- path:-scripts/
```

## **Integration Workflows**

### **Professional Document Creation**
1. **Edit source documents** (maintain single source of truth)
2. **Clean formatting** with markdown processing tools
3. **Generate distribution** with document generation scripts
4. **Verify quality** and commit both source and generated files

### **Vault Maintenance**
1. **Regular cleanup** with `clean_all_markdown.sh`
2. **Template management** with obsidian-tools scripts
3. **Metadata normalization** with metadata-tools utilities
4. **Quality verification** before important commits


## **Best Practices**

### **Script Usage**
- **Always use dry-run first** for unfamiliar scripts or large operations
- **Run from appropriate directory** - some scripts are path-sensitive
- **Check dependencies** before running production operations
- **Use version control** - commit before major batch operations

### **Project Integration**
- **Respect source/output separation** for document generation
- **Maintain professional standards** through automated quality tools
- **Document any customizations** for future maintenance
- **Test scripts** in development environment before production

### **Quality Assurance**
- **Preview changes** with dry-run modes
- **Verify output** after batch operations
- **Maintain backups** through git version control
- **Document workflow** for team consistency


## **Important Notes**

### **For Executive Document Generation**
- **Never edit consolidated document directly** - always edit source documents
- **Professional standards required** - designed for executive-level presentation
- **Quality automation** - scripts enforce professional presentation standards
- **Customizable formatting** - dates, contact information, and cultural considerations

### **For General Use**
- **Safe operations** - scripts designed to be non-destructive to content
- **Obsidian compatibility** - tested with large vault operations
- **Performance optimized** - efficient processing of thousands of files
- **Cross-project utility** - scripts useful beyond this specific project


**Maintenance**: Keep scripts current with evolving needs  
**Documentation**: Update README when adding new capabilities  
**Quality**: Maintain professional standards in all automation  
**Integration**: Ensure scripts work harmoniously across workflows

## **🎯 Key Benefits**

### **For Individual Users**
- **Collaborative writing environment** - AI assistance directly in your documents, not separate chat
- **Complete setup guidance** - No more guesswork about configuration
- **Professional templates** - Ready-to-use note structures for any use case
- **Automated analysis** - Understand your content's health and optimization opportunities
- **Problem prevention** - Comprehensive troubleshooting before issues occur
- **Tool-agnostic approach** - Works with Obsidian, Notion, Roam, standard markdown, and more

### **For Power Users**
- **Advanced workflows** - Multi-vault management, bulk operations
- **Quality assurance** - Automated consistency checks and metrics
- **Professional deliverables** - Templates for business and academic contexts
- **Safe AI-assisted editing** - Rules that protect Obsidian's unique features

### **For Teams**
- **Standardized setup** - Consistent configuration across team members
- **Best practices** - Proven workflows for collaborative knowledge management
- **Version control** - Professional Git integration for shared vaults
- **Quality standards** - Automated tools for maintaining vault consistency

## **🚀 What Makes This Unique**

This is the **first comprehensive resource** for using AI-powered editors (like Cursor) safely and effectively with Obsidian. The combination provides:

1. **AI-assisted bulk operations** while preserving Obsidian's linking system
2. **Professional document generation** from personal knowledge bases
3. **Automated quality control** for large-scale note collections
4. **Safe external editing** with comprehensive protection rules

The toolkit bridges the gap between personal knowledge management (Obsidian) and professional document production (Cursor + AI), creating a workflow that's greater than the sum of its parts.

This positions the project as a **pioneering resource** for the growing community of knowledge workers who want to leverage AI while maintaining the integrity of their personal knowledge systems.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Not sure what that means?** Check out [LICENSE-EXPLAINED.md](LICENSE-EXPLAINED.md) for a plain-language explanation of your rights and obligations. 