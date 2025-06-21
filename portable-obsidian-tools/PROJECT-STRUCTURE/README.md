# PROJECT-STRUCTURE Tool

**Universal project structure documentation generator for portable-obsidian-tools ecosystem**

Generate comprehensive PROJECT-STRUCTURE.md documentation for any project using the portable-obsidian-tools. This tool provides AI assistants with complete project context and hierarchical understanding.

## 🎯 Purpose

The PROJECT-STRUCTURE tool creates detailed documentation that includes:
- **Complete file inventory** with accurate counts and statistics
- **Hierarchical directory structure** with descriptions and annotations
- **Project-specific customization** through template system
- **AI-friendly context** for cross-project collaboration
- **Automated maintenance** for keeping documentation current

## 📁 Files in This Tool

### `generate_project_structure.py`
**Main script** - Universal project structure analyzer
- Automatically detects project root by finding `portable-obsidian-tools/` directory
- Generates accurate file counts and statistics for any project type
- Creates hierarchical directory trees with smart annotations
- Supports template-based customization for different project types
- Outputs to `portable-obsidian-tools/PROJECT-STRUCTURE.md`

### `project_template.json` 
**Template configuration** - Customizes output for specific project types
- Auto-generated on first run with intelligent defaults
- Fully customizable for project-specific needs
- Supports custom sections, descriptions, and features

### `README.md`
**This documentation** - Complete usage guide and examples

### `TEMPLATE-MAP.md`
**Template guide** - Shows AI assistants how to use this tool effectively

## 🚀 Quick Start

### Step 1: Copy to Your Project
Copy the entire `PROJECT-STRUCTURE/` folder to your project's `portable-obsidian-tools/` directory:

```bash
# From your project root
cp -r /path/to/master-tools/PROJECT-STRUCTURE portable-obsidian-tools/
```

### Step 2: Run the Generator
```bash
# From anywhere in your project
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### Step 3: Customize (Optional)
Edit the auto-generated `project_template.json` to customize output for your specific project needs.

## 📊 What Gets Generated

The tool creates a comprehensive `PROJECT-STRUCTURE.md` file with:

1. **Project Overview** - File counts, documentation system type, key features
2. **Complete Directory Structure** - Hierarchical tree with annotations
3. **Summary Statistics** - Detailed breakdowns by file type
4. **Key System Components** - Organized by functional areas
5. **Custom Sections** - Project-specific content from templates

## 🔧 Template Customization

### Auto-Generated Template
On first run, creates `project_template.json` with smart defaults:

```json
{
  "project_name": "Your Project Name",
  "project_type": "Obsidian Vault",
  "key_features": [
    "Markdown Documentation",
    "Portable Tools Integration",
    "Automated Processing"
  ],
  "custom_sections": [
    {
      "title": "📋 Project Workflow",
      "content": "- Document creation and maintenance\n- Automated link checking\n- Template application"
    }
  ],
  "directory_descriptions": {
    "portable-obsidian-tools": "Universal markdown toolkit",
    "docs": "Main documentation directory",
    "scripts": "Automation and utility scripts"
  }
}
```

### Customization Options

**Project Information:**
- `project_name` - Display name for your project
- `project_type` - Type of documentation system (Obsidian Vault, etc.)
- `key_features` - List of main project capabilities

**Custom Sections:**
- Add any number of custom sections with titles and content
- Supports markdown formatting in content
- Appears in the Key System Components area

**Directory Descriptions:**
- Map relative paths to descriptive comments
- Helps explain the purpose of each directory
- Appears as comments in the directory tree

## 💡 Usage Examples

### For Documentation Projects
```json
{
  "project_name": "API Documentation Hub",
  "project_type": "Technical Documentation",
  "key_features": [
    "API Reference",
    "Code Examples",
    "Integration Guides"
  ]
}
```

### For Knowledge Management
```json
{
  "project_name": "Research Knowledge Base",
  "project_type": "Obsidian PKM System",
  "key_features": [
    "Linked Notes",
    "Research Papers",
    "Concept Maps"
  ]
}
```

### For Software Projects
```json
{
  "project_name": "Development Documentation",
  "project_type": "Technical Specification",
  "key_features": [
    "Architecture Docs",
    "User Guides",
    "Development Setup"
  ]
}
```

## 🔄 When to Regenerate

Run the generator when:
- **Structure changes** - New directories or major reorganization
- **File count changes** - Significant additions or removals
- **Template updates** - Modified project_template.json
- **Regular maintenance** - Monthly or quarterly updates
- **Before sharing** - Ensure current context for collaborators

## 🤖 AI Integration

The generated PROJECT-STRUCTURE.md serves as:
- **Project context** for AI assistants in new sessions
- **Navigation guide** for understanding file organization
- **Scope reference** for determining what tools and processes exist
- **Integration map** for understanding how portable-obsidian-tools fits

## 🛠️ Advanced Features

### Smart Project Detection
- Automatically finds project root by locating `portable-obsidian-tools/`
- Works from any subdirectory within the project
- Handles nested projects gracefully

### Comprehensive File Analysis
- Counts all major file types (markdown, Python, shell, images, configs)
- Detects common documentation patterns (glossaries, field mappings)
- Excludes .git and hidden files automatically

### Template System
- Merges custom templates with intelligent defaults
- Preserves custom settings across regenerations
- Supports complex project structures

### Error Handling
- Graceful handling of permission errors
- Fallback behaviors for missing dependencies
- Clear error messages for troubleshooting

## 📋 Requirements

- **Python 3.7+** - Uses pathlib and modern Python features
- **Unix-like system** - Uses `find` command for file discovery
- **portable-obsidian-tools** - Must be in project structure

## 🔍 Troubleshooting

### "Error getting file list"
- Check permissions in project directory
- Ensure `find` command is available
- Verify not running from restricted location

### "Could not load template"
- Template JSON syntax error - check with JSON validator
- File permissions issue - ensure write access
- Delete template file to regenerate with defaults

### "Failed to generate project statistics"
- Permission denied in project directory
- Insufficient disk space
- Corrupted file system

## 📚 Integration with Other Tools

This tool works seamlessly with other portable-obsidian-tools:
- **Markdown processing** - Provides context for batch operations
- **Template application** - Understands project structure for templates
- **Link management** - Knows where to find and fix links
- **Metadata tools** - Identifies files that need metadata processing

---

**Status:** Production-ready universal tool  
**Compatibility:** All projects using portable-obsidian-tools  
**Maintenance:** Auto-updating statistics, manual template customization 