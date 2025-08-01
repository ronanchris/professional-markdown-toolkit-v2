# Professional Markdown Toolkit

**Professional tools for markdown cleanup and Notion import fixing.**

## 🎯 What This Is

A collection of **portable markdown processing tools** that you copy to your projects. It provides:

- ✅ **Markdown formatting cleanup** from copy-paste issues
- ✅ **Unicode and emoji cleaning** with smart replacements
- ✅ **WikiLink conversion** to compatible formats
- ✅ **Notion import problem solving** (95%+ success rate)
- ✅ **Automatic backups** for all operations

## 🚀 Quick Start

```bash
# Get the tools
git clone https://github.com/ronanchris/professional-markdown-toolkit-v2.git
cd professional-markdown-toolkit-v2/markdown-toolkit
./install.sh

# Most common usage - clean up messy formatting
python tools/cleanup_markdown_batch.py

# Fix document that won't import to Notion
python tools/notion_complete_fixer.py your-document.md
```

## 🛠️ Available Tools

### **Markdown Cleanup Tools** (Start Here)

- **🧹 cleanup_markdown_batch.py** - Fix formatting and spacing issues
- **📝 cleanup_markdown.py** - Single file cleanup
- **🔤 unicode_cleaner.py** - Smart Unicode and emoji handling
- **🔗 wikilink_converter.py** - Convert WikiLinks to bold text
- **⚡ clean_all_markdown.sh** - Batch processing script

### **Notion Import Tools** (Use After Cleanup)

- **📄 notion_complete_fixer.py** - All-in-one Notion solution (recommended)
- **🎯 notion_import_fixer.py** - Notion-specific formatting fixes

### **🛡️ Safety Tools**

- **🛡️ backup-functions.sh** - Safety and backup utilities

## 📋 Quick Reference

| **Problem** | **Tool** | **Command** |
|-------------|----------|-------------|
| Messy formatting from copy-paste | `cleanup_markdown_batch.py` | `python tools/cleanup_markdown_batch.py` |
| Emojis/special characters broken | `unicode_cleaner.py` | `python tools/unicode_cleaner.py file.md` |
| WikiLinks not compatible | `wikilink_converter.py` | `python tools/wikilink_converter.py file.md` |
| Document won't import to Notion | `notion_complete_fixer.py` | `python tools/notion_complete_fixer.py file.md` |
| Need to clean many files | `clean_all_markdown.sh` | `tools/clean_all_markdown.sh` |

## 📚 Documentation

- **[Tool Details →](markdown-toolkit/README.md)** - Complete guide with examples
- **[Notion Tools →](markdown-toolkit/tools/README-NOTION-TOOLS.md)** - Notion-specific solutions

## 🚨 Safety Features

- **Automatic backups** for all operations
- **Dry-run modes** available (`--dry-run` flag)
- **Analysis modes** to preview changes (`--analyze` flag)

## 💡 Usage Tips

1. **Start with cleanup tools** for general formatting issues
2. **Use Notion tools only** if you're having import problems
3. **Always use `--analyze` first** to see what will change
4. **Test on single files** before batch operations

## 📄 License

MIT License - See `LICENSE` for details.

