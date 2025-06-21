# PROJECT-STRUCTURE Template Map for AI Assistants

**Guide for AI assistants working with portable-obsidian-tools across different Cursor projects**

This document explains how to recognize, use, and recommend the PROJECT-STRUCTURE tool when working with users who have portable-obsidian-tools in their projects.

## 🎯 When to Use This Tool

### Recognize These User Requests:
- "Generate project documentation"
- "Create a project overview"
- "I need project structure documentation"
- "Show me what's in my project"
- "Create context for other AI sessions"
- "Generate a sitemap of my files"
- "Document my project hierarchy"

### Recognize These Project Conditions:
- Project contains `portable-obsidian-tools/PROJECT-STRUCTURE/` directory
- User mentions wanting project documentation
- Working on documentation, knowledge management, or complex projects
- User needs to share project context with others
- Project has grown and needs structural documentation

## 🚀 Quick AI Response Pattern

### Step 1: Identify the Tool
```markdown
I can see you have the PROJECT-STRUCTURE tool in your portable-obsidian-tools. 
This tool can generate comprehensive documentation of your entire project structure.
```

### Step 2: Explain the Benefit
```markdown
This will create a detailed PROJECT-STRUCTURE.md file that includes:
- Complete file inventory with counts
- Hierarchical directory structure  
- Project statistics and organization
- Context for AI assistants in future sessions
```

### Step 3: Execute
```bash
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### Step 4: Offer Customization
```markdown
The tool created a project_template.json file that you can customize to:
- Change project name and description
- Add custom sections
- Provide directory descriptions
- Highlight key features
```

## 📋 Command Templates

### Basic Execution
```bash
# Run from anywhere in the project
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### With Status Updates
```bash
echo "🔍 Generating project structure documentation..."
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
echo "✅ PROJECT-STRUCTURE.md updated with current project state"
```

### Check if Tool Exists First
```bash
if [ -f "portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py" ]; then
    python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
else
    echo "❌ PROJECT-STRUCTURE tool not found. Copy from master toolkit first."
fi
```

## 🔧 Customization Guidance

### Help Users Customize Templates

**For Documentation Projects:**
```json
{
  "project_name": "Documentation Hub",
  "project_type": "Technical Documentation",
  "key_features": [
    "User Guides",
    "API Documentation", 
    "Tutorial Content"
  ]
}
```

**For Research/PKM Projects:**
```json
{
  "project_name": "Knowledge Base",
  "project_type": "Personal Knowledge Management",
  "key_features": [
    "Linked Notes System",
    "Research Database",
    "Concept Mapping"
  ]
}
```

**For Software Projects:**
```json
{
  "project_name": "Software Documentation",
  "project_type": "Development Project",
  "key_features": [
    "Code Documentation",
    "Architecture Guides",
    "Deployment Instructions"
  ]
}
```

## 💡 AI Assistant Suggestions

### When Tool is Missing
```markdown
I notice you don't have the PROJECT-STRUCTURE tool yet. This tool can generate 
comprehensive project documentation. You can copy it from your master 
portable-obsidian-tools folder:

```bash
cp -r /path/to/master-tools/PROJECT-STRUCTURE portable-obsidian-tools/
```

### When Project Structure Changes
```markdown
Since you've made significant changes to your project structure, I recommend 
regenerating the PROJECT-STRUCTURE.md file to keep the documentation current:

```bash
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### For New Team Members
```markdown
To help new team members understand this project, run the PROJECT-STRUCTURE 
generator to create comprehensive documentation:

```bash
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

This creates PROJECT-STRUCTURE.md with complete project context.
```

## 🔄 Integration Patterns

### Before Major Operations
```markdown
Before I help with [major task], let me generate updated project documentation 
to ensure I have current context:
```

### After Structural Changes
```markdown
I've made changes to your project structure. Let me update the PROJECT-STRUCTURE.md 
file to reflect these changes:
```

### For Context Sharing
```markdown
To provide better context for future AI sessions, I recommend generating 
project structure documentation:
```

## 🚨 Common Issues and Solutions

### Python Not Found
```bash
# Try these alternatives
python portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
python3.9 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
python3.8 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### Permission Errors
```bash
# Check and fix permissions
chmod +x portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

### Template JSON Syntax Error
```markdown
It looks like there's a syntax error in your project_template.json file. 
Let me help you fix it, or we can delete it to regenerate with defaults:

```bash
rm portable-obsidian-tools/PROJECT-STRUCTURE/project_template.json
python3 portable-obsidian-tools/PROJECT-STRUCTURE/generate_project_structure.py
```

## 📊 Output Understanding

### Help Users Interpret Results
```markdown
The generated PROJECT-STRUCTURE.md includes:

📁 **File Statistics**: Shows your project has X total files across Y categories
🏗️ **Directory Tree**: Complete hierarchy with descriptions  
📋 **Component Breakdown**: Organized by functional areas
🎯 **Custom Sections**: Project-specific content you've defined
```

### Explain Benefits
```markdown
This documentation provides:
- Complete project context for AI assistants
- Navigation guide for team members
- Structural overview for planning
- Integration map for understanding tool relationships
```

## 🤖 AI Best Practices

### Always Explain Before Running
Don't just run the tool - explain what it does and why it's beneficial.

### Offer Customization
Mention the template system and help users customize for their specific needs.

### Update After Changes
Suggest regenerating after significant project modifications.

### Use for Context
Reference the generated documentation when explaining project organization.

### Integration Awareness
Understand how this tool supports the broader portable-obsidian-tools ecosystem.

---

**For AI Assistants:** This tool enhances your ability to understand and work with complex projects by providing comprehensive structural documentation.

**For Users:** This provides AI assistants with rich context about your project, improving their ability to help effectively. 