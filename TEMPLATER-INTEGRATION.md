# Templater Integration Guide

## 🔧 Templater Plugin Dependency

This toolkit is heavily integrated with the **Templater** Obsidian plugin. Many scripts are designed to process or generate Templater-specific syntax.

## 📋 What is Templater?

**Templater** is a popular Obsidian plugin that provides advanced template functionality using JavaScript-like syntax.

- **GitHub**: https://github.com/SilentVoid13/Templater
- **Installation**: Available in Obsidian's Community Plugins
- **Documentation**: https://silentvoid13.github.io/Templater/

## ⚠️ Scripts That Require Templater

### **Template Generation Scripts**
These scripts create files with Templater syntax:

1. **`obsidian-tools/apply_template.sh`**
   - Adds Templater code blocks to files
   - Includes `<%* ... -%>` JavaScript execution blocks
   - Adds `` `= this.file.name` `` dynamic file name references

2. **`obsidian-tools/fix_template.sh`** 
   - Repairs existing Templater syntax in files
   - Standardizes Templater code formatting

### **Template Processing Scripts**
These scripts clean or remove Templater syntax:

1. **`metadata-tools/remove_metadata.sh`**
   - Removes `<%* ... -%>` code blocks
   - Removes `` `= this.file.name` `` references
   - Cleans files of all Templater syntax

2. **`metadata-tools/fix_metadata.sh`**
   - Processes and cleans Templater code blocks
   - Maintains content while removing template syntax

3. **`metadata-tools/clean_files.sh`**
   - Removes Templater syntax during file cleaning
   - Part of comprehensive file cleanup process

## 🔍 Templater Syntax Processed

### **Code Execution Blocks**
```javascript
<%*
// JavaScript code executed by Templater
try {
    const folder = tp.file.folder(true);
    const dateTime = tp.file.creation_date("YYYY-MM-DD-HHmm");
    const currentName = tp.file.title;
    const nameWithoutDate = currentName.replace(/^\d{4}-\d{2}-\d{2}-\d{4}-?/, "");
    const newName = `${dateTime}-${nameWithoutDate}`;
    await tp.file.rename(newName);
} catch (error) {
    console.error("Templater: File rename failed!", error);
}
-%>
```

### **Dynamic References**
```markdown
`= this.file.name`
```
This displays the current file name dynamically.

### **Date Functions**
```markdown
date-created: <% tp.file.creation_date("YYYY-MM-DD") %>
date-updated: <% tp.date.now("YYYY-MM-DD") %>
```

## 🚀 Setup Instructions

### **1. Install Templater Plugin**
1. Open Obsidian Settings
2. Go to Community Plugins
3. Browse and search for "Templater"
4. Install and enable the plugin

### **2. Configure Templater**
Recommended settings:
```
✅ Enable Templater
✅ Template folder location: templates/
✅ Trigger Templater on new file creation: ON
✅ Enable System Commands: ON (for advanced features)
```

### **3. Test Installation**
Create a test note with this content:
```markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
---

# `= this.file.name`

Test content.
```

If Templater is working, you should see:
- Date automatically filled in
- File name displayed as heading

## 🔄 Working Without Templater

### **What Happens If Templater Is Not Installed?**

**Scripts will still run** but:
- Templater syntax will remain as literal text
- Dynamic features won't work
- You may see unprocessed code blocks in your notes

### **Example Without Templater:**
```markdown
---
created: <% tp.date.now("YYYY-MM-DD") %>
---

# `= this.file.name`

Content here...
```

### **Alternative Approaches**
If you don't want to use Templater:

1. **Use Basic Templates**: Create simple markdown templates without dynamic code
2. **Manual Processing**: Edit dates and filenames manually
3. **Skip Template Scripts**: Use only the metadata and markdown processing tools

## 🧪 Testing Templater Integration

### **Quick Test**

#### **🖥️ Command Line Testing**
```bash
# Navigate to your vault scripts directory
cd /path/to/vault/scripts

# Test template application (requires Templater)
./obsidian-tools/apply_template.sh

# Test template cleanup (works with or without Templater)
./metadata-tools/remove_metadata.sh
```

#### **🤖 Testing with Cursor's Assistance**
**Ask Cursor**: 
```
I want to test if the Templater integration is working correctly in my vault. Can you help me:

1. Create a test file with Templater syntax
2. Run the appropriate script to test it
3. Show me what the script did
4. Help me restore the test file if needed

I want to make sure I understand how Templater syntax is processed before using this on my real notes.
```

**Cursor will guide you through safe testing and explain each step!**

### **Verify Templater Syntax Processing**
1. Create a test file with Templater syntax
2. Run `remove_metadata.sh` 
3. Check that Templater code blocks are removed
4. Restore from backup if needed

## 📚 Advanced Integration

### **Custom Template Modification**
The template content in `apply_template.sh` can be customized:

```bash
# Edit the TEMPLATE variable in apply_template.sh
TEMPLATE=$(cat <<'EOF'
---
date-created: <% tp.file.creation_date("YYYY-MM-DD") %>
# Add your custom frontmatter here
---
<%*
// Add your custom JavaScript here
-%>
`= this.file.name`

EOF
)
```

### **Integration with Other Plugins**
This toolkit works well with:
- **Dataview** - For querying templated metadata
- **QuickAdd** - For automated template triggering  
- **Folder Note** - For folder-based templates

## 🔧 Troubleshooting

### **Common Issues**

**Issue**: "Templater syntax not processing"
**Solution**: Ensure Templater plugin is enabled and configured

**Issue**: "Template code appears as literal text"  
**Solution**: Check Templater installation and template folder settings

**Issue**: "Scripts remove too much content"
**Solution**: Use `--no-backup` flag carefully, always test with backups first

### **Getting Help**
1. Check Templater documentation: https://silentvoid13.github.io/Templater/
2. Review script output for specific error messages
3. Test with simple templates first
4. Use backup restoration if needed

## 📄 Summary

Templater integration provides powerful dynamic template functionality but is not strictly required for all scripts. The toolkit is designed to work gracefully whether Templater is installed or not, with clear benefits when it is available.

**Key Points**:
- ✅ Templater enhances template functionality significantly
- ✅ Scripts work without Templater but with reduced features  
- ✅ All template-modifying operations have backup systems
- ✅ Clear documentation provided for both use cases 