# SignPilot Documentation Structure

**Complete hierarchical sitemap of the signpilot documentation where these portable tools are deployed.**

## Project Overview
- **Total Files**: 153
- **Documentation System**: Obsidian Vault with 81 markdown files
- **Automation Scripts**: 37 Python scripts + 21 shell scripts
- **Visual Assets**: 0 images and media files
- **Configuration**: 5 configuration files
- **Field Survey System**: Integrated system component
- **Sign Type Classification**: Integrated system component
- **Mobile App Documentation**: Integrated system component
- **Dashboard Platform Guides**: Integrated system component
- **Glossary Database (400+ terms)**: Integrated system component
- **Field Mapping System**: Integrated system component
- **Portable Tools Integration**: Integrated system component

## Complete Directory Structure

```
professional-markdown-toolkit/
├── company-executive/
├── cursor-tools/
│   ├── universal-session-continuity/
│   │   ├── AI-COLLABORATION-CURSOR-RULES.md
│   │   ├── COLLABORATION-STYLE.md
│   │   ├── CURRENT-PROJECT-CONTEXT.md
│   │   ├── PROBLEM-SOLVING-METHODS.md
│   │   ├── README.md
│   │   └── SESSION-PATTERNS.md
│   └── README.md
├── docs/
│   ├── examples/
│   │   ├── after/
│   │   │   ├── complex-formatting-mess.md
│   │   │   └── messy-frontmatter-example.md
│   │   ├── before/
│   │   │   ├── complex-formatting-mess.md
│   │   │   └── messy-frontmatter-example.md
│   │   └── QUICK-EXAMPLES.md
│   └── NOTION-IMPORT-GUIDE.md
├── markdown-processing/
│   ├── clean_all_markdown.sh
│   ├── cleanup_markdown.py
│   ├── cleanup_markdown_batch.py
│   ├── notion_complete_fixer.py
│   ├── notion_import_fixer.py
│   ├── README-NOTION-TOOLS.md
│   ├── unicode_cleaner.py
│   └── wikilink_converter.py
├── metadata-tools/
│   ├── clean_files.sh
│   ├── fix_metadata.sh
│   ├── remove_metadata.sh
│   ├── safe_metadata_removal.py
│   └── update_date_created_to_templater.py
├── obsidian-cursor-workflow/
│   ├── cursor-prompts-guide.md
│   ├── cursor-rules-obsidian.md
│   ├── obsidian-cursor-setup.md
│   ├── README.md
│   ├── template-examples.md
│   ├── troubleshooting-guide.md
│   └── vault-analytics.py
├── obsidian-tools/
│   ├── apply_inbox_template.py
│   ├── apply_inbox_template_to_folder.py
│   ├── apply_moc_template_preserve_metadata.py
│   ├── apply_template.sh
│   ├── fix_template.sh
│   └── update_inbox_with_template.py
├── portable-obsidian-ai-tools/
│   ├── ai-collaboration/
│   │   ├── universal-session-continuity/
│   │   │   ├── AI-COLLABORATION-CURSOR-RULES.md
│   │   │   ├── BLOG-LEARNING-MOMENTS-EXAMPLES.md
│   │   │   ├── BLOG-LEARNING-MOMENTS-TEMPLATE.md
│   │   │   ├── COLLABORATION-STYLE.md
│   │   │   ├── CURRENT-PROJECT-CONTEXT.md
│   │   │   ├── PROBLEM-SOLVING-METHODS.md
│   │   │   ├── README.md
│   │   │   └── SESSION-PATTERNS.md
│   │   └── README.md
│   ├── integration-guides/
│   │   ├── cursor-prompts-guide.md
│   │   ├── cursor-rules-obsidian.md
│   │   ├── obsidian-cursor-setup.md
│   │   ├── README.md
│   │   ├── template-examples.md
│   │   ├── troubleshooting-guide.md
│   │   └── vault-analytics.py
│   ├── obsidian-tools/
│   │   ├── markdown-processing/
│   │   │   ├── clean_all_markdown.sh
│   │   │   ├── cleanup_markdown.py
│   │   │   ├── cleanup_markdown_batch.py
│   │   │   ├── notion_complete_fixer.py
│   │   │   ├── notion_import_fixer.py
│   │   │   ├── README-NOTION-TOOLS.md
│   │   │   ├── unicode_cleaner.py
│   │   │   └── wikilink_converter.py
│   │   ├── metadata-tools/
│   │   │   ├── clean_files.sh
│   │   │   ├── fix_metadata.sh
│   │   │   ├── remove_metadata.sh
│   │   │   ├── safe_metadata_removal.py
│   │   │   └── update_date_created_to_templater.py
│   │   ├── project-structure/
│   │   │   ├── generate_project_structure.py
│   │   │   ├── INSTALL.md
│   │   │   ├── project_template.json
│   │   │   ├── README.md
│   │   │   └── TEMPLATE-MAP.md
│   │   └── template-management/
│   │       ├── apply_inbox_template.py
│   │       ├── apply_inbox_template_to_folder.py
│   │       ├── apply_moc_template_preserve_metadata.py
│   │       ├── apply_template.sh
│   │       ├── fix_template.sh
│   │       └── update_inbox_with_template.py
│   ├── shared/
│   │   └── backup-functions.sh
│   ├── DEAD-SIMPLE.md
│   ├── DEPLOYMENT-PROMPT.md
│   ├── install.sh
│   ├── requirements.txt
│   └── TOOLKIT-GUIDE.md
├── session-continuity/
│   ├── notion/
│   │   ├── AI-INSTRUCTIONS.md
│   │   ├── AI-PROMPTS.md
│   │   ├── AI-RULES.md
│   │   └── AI-USE-CASES.md
│   ├── SESSION-PLAN-ARCHIVE/
│   ├── BLOG-LEARNING-MOMENTS.md
│   ├── CONVERSATIONAL-INSIGHTS.md
│   ├── CURRENT-STATE-SNAPSHOT.md
│   ├── DEPLOYMENT-GUIDE.md
│   ├── DEVIATION-TRACKING-PROTOCOL.md
│   ├── PROBLEM-SOLVING-PATTERNS.md
│   ├── README-FOR-FUTURE-AI.md
│   ├── README.md
│   └── [+5 more items...]
├── shared/
│   └── backup-functions.sh
├── test-cases/
│   └── notion-import-issues/
│       ├── cleaned/
│       │   ├── README-project-description-notion-ready.md
│       │   ├── signpilot-host-transition-report-v2-complete.md
│       │   └── signpilot-hosting-deep-research-complete.md
│       ├── original/
│       │   ├── README-project-description.md
│       │   ├── signpilot-host-transition-report-v2.md
│       │   └── signpilot-hosting-deep-research.md
│       ├── processed/
│       ├── notion_complete_fixer.py
│       ├── notion_import_fixer.py
│       ├── test-table-sample.md
│       ├── unicode_cleaner.py
│       └── wikilink_converter.py
├── test-examples/
│   ├── complex-templater-document.md
│   ├── edge-cases.md
│   └── malformed-frontmatter.md
├── test-vault/
│   ├── 0-inbox/
│   │   └── test-document.md
│   ├── 01-projects/
│   ├── scripts/
│   │   ├── backups/
│   │   │   ├── 20250531_183037/
│   │   │   │   └── metadata_removal/
│   │   │   │       └── test-document.md
│   │   │   ├── 20250531_183140/
│   │   │   │   └── metadata_removal/
│   │   │   │       └── test-document.md
│   │   │   └── 20250531_183152/
│   │   │       └── file_cleaning/
│   │   │           └── test-document.md
│   │   ├── metadata-tools/
│   │   │   ├── clean_files.sh
│   │   │   ├── fix_metadata.sh
│   │   │   ├── remove_metadata.sh
│   │   │   ├── safe_metadata_removal.py
│   │   │   └── update_date_created_to_templater.py
│   │   ├── obsidian-tools/
│   │   │   ├── apply_inbox_template.py
│   │   │   ├── apply_inbox_template_to_folder.py
│   │   │   ├── apply_moc_template_preserve_metadata.py
│   │   │   ├── apply_template.sh
│   │   │   ├── fix_template.sh
│   │   │   └── update_inbox_with_template.py
│   │   └── shared/
│   │       └── backup-functions.sh
│   └── templates/
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-EXPLAINED.md
├── PROGRESS-SUMMARY.md
├── PROJECT-ROADMAP.md
├── PROJECT-SECURITY-PLAN.md
├── README.md
├── README.pdf
├── requirements.txt
├── SECURITY-AUDIT.md
└── TEMPLATER-INTEGRATION.md
```

## Summary Statistics
- **Total Project Files**: 153
- **Markdown Documentation**: 81 files
- **Python Scripts**: 37 automation tools
- **Shell Scripts**: 21 utilities
- **Visual Assets**: 0 media files
- **Configuration Files**: 5 config files

## Key System Components

### 📊 **Documentation Architecture**
- **Markdown Processing**: Universal documentation tools
- **File Organization**: Structured hierarchy with 153 total files

### 🛠️ **Automation Infrastructure**
        - **portable-obsidian-ai-tools/**: Universal AI-enhanced markdown processing suite
- **Automated Workflows**: Project-specific tools and utilities
- **Template System**: Reusable documentation patterns

### 🎯 **Integration Features**
- **Cross-Project Compatibility**: Portable tool ecosystem
- **AI Assistant Support**: Context-rich documentation
- **Workflow Automation**: Batch processing and maintenance tools

### **📱 Platform Components**
- **Dashboard Platform**: Web-based management interface for shop owners
- **Mobile Application**: Field survey app for data collection
- **API System**: Backend integration and data synchronization
- **Reporting Tools**: Analytics and project management features

### **🏗️ Survey Workflow**
- **6-Step Process**: Comprehensive sign assessment workflow
- **23 Sign Types**: Complete taxonomy (8 indoor + 15 outdoor)
- **Field Mapping**: 400+ individual field definitions
- **Data Validation**: Automated quality control and verification

### **🔧 Documentation Architecture**
- **Hierarchical Organization**: Structured by platform and workflow
- **Cross-Referenced**: Extensive linking between concepts
- **Template-Driven**: Consistent formatting and organization
- **AI-Enhanced**: Optimized for AI assistant collaboration

This represents the complete signpilot documentation ecosystem with proper hierarchical organization.