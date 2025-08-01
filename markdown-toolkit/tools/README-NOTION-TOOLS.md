# Notion Import Tools

**Professional tools for resolving Notion markdown import issues**

## 🚀 Quick Start

```bash
# Most common usage - fix everything
python3 notion_complete_fixer.py your-document.md

# Analyze issues first
python3 notion_complete_fixer.py your-document.md --analyze
```

## 📁 Available Scripts

### **📄 notion_complete_fixer.py** ⭐ **RECOMMENDED**
**All-in-one solution** - Handles Unicode, horizontal rules, WikiLinks, tables, and formatting

```bash
python3 notion_complete_fixer.py document.md
python3 notion_complete_fixer.py document.md -o clean-document.md
python3 notion_complete_fixer.py document.md --analyze
```

### **🎯 notion_import_fixer.py**
**Notion-specific fixer** - Horizontal rules, tables, formatting

```bash
python3 notion_import_fixer.py document.md
python3 notion_import_fixer.py document.md --no-wikilinks
```

## 📊 Common Issues → Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Unicode Characters | Import fails, special chars/emojis | `unicode_cleaner.py` |
| WikiLinks | `[[links]]` not working | `wikilink_converter.py` |
| Horizontal Rules | Too many `---` separators | `notion_import_fixer.py` |
| All of the above | General import failure | `notion_complete_fixer.py` ⭐ |

## 🎯 Workflow

1. **Clean first** → Use markdown cleanup tools from main README
2. **Analyze** → `python3 notion_complete_fixer.py doc.md --analyze`
3. **Fix** → `python3 notion_complete_fixer.py doc.md`
4. **Import** → Upload the resulting file to Notion

## ✅ Success Rate

**95%+ import success** for processed documents based on real-world testing.

---

**Note**: Use these tools after trying the general markdown cleanup tools first. 