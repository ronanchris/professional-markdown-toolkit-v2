#!/usr/bin/env python3
"""
Universal Project Structure Generator for Portable Obsidian Tools
================================================================
Generate PROJECT-STRUCTURE.md with hierarchical directory structure for any project.
Designed to be portable across different projects using the obsidian-tools ecosystem.

This tool can be run from anywhere within a project and will:
- Analyze the complete project structure
- Generate accurate file counts and statistics  
- Create hierarchical directory tree with annotations
- Output to portable-obsidian-tools/PROJECT-STRUCTURE.md
- Support template-based customization for different project types
"""

import subprocess
import os
import sys
from pathlib import Path
import json

def find_project_root():
    """Find the project root by looking for portable-obsidian-tools directory."""
    current = Path.cwd()
    
    # Look up the directory tree for portable-obsidian-tools
    while current != current.parent:
        if (current / 'portable-obsidian-tools').exists():
            return current
        current = current.parent
    
    # If not found, assume current directory is project root
    return Path.cwd()

def get_project_stats(project_root):
    """Get accurate project statistics for any project."""
    
    # Get file counts
    result = subprocess.run(['find', '.', '-type', 'f', '!', '-path', './.git/*'], 
                          capture_output=True, text=True, cwd=project_root)
    
    if result.returncode != 0:
        print("Error getting file list")
        return None
    
    all_files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
    
    stats = {
        'total_files': len(all_files),
        'markdown_files': sum(1 for f in all_files if f.endswith('.md')),
        'python_files': sum(1 for f in all_files if f.endswith('.py')),
        'shell_scripts': sum(1 for f in all_files if f.endswith('.sh')),
        'images': sum(1 for f in all_files if f.endswith(('.png', '.jpg', '.gif', '.jpeg', '.svg'))),
        'config_files': sum(1 for f in all_files if f.endswith(('.json', '.yml', '.yaml', '.toml', '.cfg', '.ini'))),
        'documentation_files': sum(1 for f in all_files if any(doc_dir in f for doc_dir in ['/docs/', '/documentation/', '/README', '/REFERENCE/']))
    }
    
    # Try to get specific counts for common documentation patterns
    try:
        # Look for glossary terms
        glossary_result = subprocess.run(['find', '.', '-path', '*/glossary/terms/*.md', '-o', '-path', '*/REFERENCE/glossary/terms/*.md'], 
                                       capture_output=True, text=True, cwd=project_root)
        glossary_files = [f for f in glossary_result.stdout.split('\n') if f.strip() and '_template' not in f and 'README' not in f]
        stats['glossary_terms'] = len(glossary_files)
        
        # Look for field mappings
        field_result = subprocess.run(['find', '.', '-path', '*/Field-Mappings*/*.md', '-o', '-path', '*/field-mappings*/*.md'], 
                                     capture_output=True, text=True, cwd=project_root)
        field_files = [f for f in field_result.stdout.split('\n') if f.strip() and not f.endswith('_index.md')]
        stats['field_mappings'] = len(field_files)
        
    except:
        stats['glossary_terms'] = 0
        stats['field_mappings'] = 0
    
    return stats

def load_project_template(project_root):
    """Load project-specific template if it exists, otherwise use default."""
    template_path = project_root / 'portable-obsidian-tools' / 'PROJECT-STRUCTURE' / 'project_template.json'
    
    default_template = {
        "project_name": "Documentation Project",
        "project_type": "Obsidian Vault",
        "key_features": [
            "Markdown Documentation",
            "Automated Tools",
            "Reference Materials"
        ],
        "custom_sections": [],
        "directory_descriptions": {}
    }
    
    if template_path.exists():
        try:
            with open(template_path, 'r') as f:
                template = json.load(f)
                # Merge with defaults
                for key, value in default_template.items():
                    if key not in template:
                        template[key] = value
                return template
        except:
            print(f"Warning: Could not load template from {template_path}, using defaults")
    
    return default_template

def create_structure_content(project_root, stats, template):
    """Create the PROJECT-STRUCTURE.md content with template customization."""
    
    project_name = template.get('project_name', 'Documentation Project')
    project_type = template.get('project_type', 'Obsidian Vault')
    
    content = f"""# {project_name} Structure

**Complete hierarchical sitemap of the {project_name.lower()} where these portable tools are deployed.**

## Project Overview
- **Total Files**: {stats['total_files']}
- **Documentation System**: {project_type} with {stats['markdown_files']} markdown files
- **Automation Scripts**: {stats['python_files']} Python scripts + {stats['shell_scripts']} shell scripts
- **Visual Assets**: {stats['images']} images and media files
- **Configuration**: {stats['config_files']} configuration files"""

    # Add custom overview sections if defined in template
    if stats['glossary_terms'] > 0:
        content += f"\n- **Glossary Terms**: {stats['glossary_terms']} term definitions"
    if stats['field_mappings'] > 0:
        content += f"\n- **Field Mappings**: {stats['field_mappings']} field definitions"
    
    for feature in template.get('key_features', []):
        if feature not in content:
            content += f"\n- **{feature}**: Integrated system component"

    content += f"""

## Complete Directory Structure

```
{project_root.name}/"""

    # Generate the tree structure
    content += generate_directory_tree(project_root, template.get('directory_descriptions', {}))
    
    content += f"""
```

## Summary Statistics
- **Total Project Files**: {stats['total_files']}
- **Markdown Documentation**: {stats['markdown_files']} files
- **Python Scripts**: {stats['python_files']} automation tools
- **Shell Scripts**: {stats['shell_scripts']} utilities
- **Visual Assets**: {stats['images']} media files
- **Configuration Files**: {stats['config_files']} config files

## Key System Components

### 📊 **Documentation Architecture**"""

    # Add template-specific documentation sections
    if stats['glossary_terms'] > 0:
        content += f"\n- **Glossary System**: {stats['glossary_terms']} term definitions"
    if stats['field_mappings'] > 0:
        content += f"\n- **Field Mapping System**: {stats['field_mappings']} field specifications"
    
    content += f"\n- **Markdown Processing**: Universal documentation tools"
    content += f"\n- **File Organization**: Structured hierarchy with {stats['total_files']} total files"

    content += """

### 🛠️ **Automation Infrastructure**
- **portable-obsidian-tools/**: Universal markdown processing suite
- **Automated Workflows**: Project-specific tools and utilities
- **Template System**: Reusable documentation patterns

### 🎯 **Integration Features**
- **Cross-Project Compatibility**: Portable tool ecosystem
- **AI Assistant Support**: Context-rich documentation
- **Workflow Automation**: Batch processing and maintenance tools"""

    # Add custom sections from template
    for section in template.get('custom_sections', []):
        content += f"\n\n### **{section['title']}**\n{section['content']}"

    content += f"\n\nThis represents the complete {project_name.lower()} ecosystem with proper hierarchical organization."
    
    return content

def generate_directory_tree(project_root, descriptions):
    """Generate the hierarchical directory tree structure."""
    tree_content = ""
    
    def add_directory(path, prefix="", is_last=True):
        nonlocal tree_content
        if path.name.startswith('.'):
            return
        
        connector = "└── " if is_last else "├── "
        
        # Get description from template if available
        rel_path = str(path.relative_to(project_root))
        description = descriptions.get(rel_path, "")
        if description:
            description = f"  # {description}"
        
        if path.is_dir():
            tree_content += f"\n{prefix}{connector}{path.name}/{description}"
            
            # Get subdirectories and files
            try:
                items = sorted([p for p in path.iterdir() if not p.name.startswith('.')], 
                             key=lambda x: (x.is_file(), x.name.lower()))
                
                for i, item in enumerate(items[:10]):  # Limit to prevent huge output
                    is_last_item = i == len(items) - 1
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    add_directory(item, new_prefix, is_last_item)
                
                if len(items) > 10:
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    tree_content += f"\n{new_prefix}└── [+{len(items)-10} more items...]"
                    
            except PermissionError:
                pass
        else:
            # File
            tree_content += f"\n{prefix}{connector}{path.name}{description}"
    
    # Start the tree generation
    try:
        items = sorted([p for p in project_root.iterdir() if not p.name.startswith('.')], 
                      key=lambda x: (x.is_file(), x.name.lower()))
        
        for i, item in enumerate(items):
            is_last_item = i == len(items) - 1
            add_directory(item, "", is_last_item)
            
    except Exception as e:
        tree_content += f"\n├── [Error reading directory structure: {e}]"
    
    return tree_content

def create_template_file(project_root):
    """Create a template configuration file for project customization."""
    template_path = project_root / 'portable-obsidian-tools' / 'PROJECT-STRUCTURE' / 'project_template.json'
    
    # Detect project characteristics
    project_name = project_root.name.replace('-', ' ').replace('_', ' ').title()
    
    # Basic template structure
    template = {
        "project_name": project_name,
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
            "README.md": "Project overview and setup",
            "docs": "Main documentation directory",
            "scripts": "Automation and utility scripts"
        }
    }
    
    # Write template if it doesn't exist
    if not template_path.exists():
        with open(template_path, 'w') as f:
            json.dump(template, f, indent=2)
        print(f"✅ Created template file: {template_path}")
    
    return template

def main():
    """Generate PROJECT-STRUCTURE.md with current accurate statistics."""
    print("🔍 Analyzing project structure...")
    
    # Find project root
    project_root = find_project_root()
    print(f"📁 Project root detected: {project_root}")
    
    # Get statistics
    stats = get_project_stats(project_root)
    if not stats:
        print("❌ Failed to generate project statistics")
        return 1
    
    # Load or create template
    template = load_project_template(project_root)
    
    # Generate content
    content = create_structure_content(project_root, stats, template)
    
    # Write to portable-obsidian-tools directory
    output_path = project_root / 'portable-obsidian-tools' / 'PROJECT-STRUCTURE.md'
    
    try:
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"✅ Successfully updated {output_path}")
        print(f"📊 Structure includes {stats['total_files']} files across {stats['markdown_files']} markdown documents")
        
        # Create template file for future customization
        create_template_file(project_root)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 