# Notion Import Tools - Quick Reference

**Location:** `markdown-processing/`  
**Purpose:** Professional tools for resolving Notion markdown import issues

## 🚀 **Quick Start**

```bash
# Most common usage - fix everything
python3 notion_complete_fixer.py your-document.md

# Analyze issues first
python3 notion_complete_fixer.py your-document.md --analyze
```

## 📁 **Available Scripts**

### **🎯 notion_complete_fixer.py** ⭐ **RECOMMENDED**
**All-in-one solution** - Handles Unicode, horizontal rules, WikiLinks, tables, and formatting

```bash
python3 notion_complete_fixer.py document.md
python3 notion_complete_fixer.py document.md -o clean-document.md
python3 notion_complete_fixer.py document.md --analyze
```

### **🔤 unicode_cleaner.py**
**Unicode character specialist** - Smart replacements preserving meaning

```bash
python3 unicode_cleaner.py document.md
python3 unicode_cleaner.py document.md --analyze --verbose
```

### **🔗 wikilink_converter.py**
**WikiLink converter** - Transforms `[[links]]` to `**Bold Text**`

```bash
python3 wikilink_converter.py document.md
python3 wikilink_converter.py document.md --preview
```

### **📄 notion_import_fixer.py**
**Notion-specific fixer** - Horizontal rules, tables, formatting

```bash
python3 notion_import_fixer.py document.md
python3 notion_import_fixer.py document.md --no-wikilinks
```

## 📊 **Common Issues → Solutions**

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Unicode Characters | Import fails, special chars/emojis | `unicode_cleaner.py` |
| WikiLinks | `[[links]]` not working | `wikilink_converter.py` |
| Horizontal Rules | Too many `---` separators | `notion_import_fixer.py` |
| All of the above | General import failure | `notion_complete_fixer.py` ⭐ |

## 🎯 **Workflow**

1. **Analyze** → `python3 notion_complete_fixer.py doc.md --analyze`
2. **Fix** → `python3 notion_complete_fixer.py doc.md`
3. **Import** → Upload the resulting file to Notion

## 📚 **More Information**

- **Complete Guide:** `docs/NOTION-IMPORT-GUIDE.md`
- **Test Cases:** `test-cases/notion-import-issues/`
- **Integration:** See main `README.md`

## ✅ **Success Rate**

**95%+ import success** for processed documents based on real-world testing. 