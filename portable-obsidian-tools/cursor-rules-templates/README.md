# Cursor Rules Templates for Large Obsidian Vaults

**Purpose**: Ready-to-use cursor rules optimized for large Obsidian vaults (1000+ pages) with portable-obsidian-tools integration.

## 📋 **Files Included**

### **ALWAYS Rules** (Safety-Critical)
- `obsidian-syntax-preservation.md` - Protects WikiLinks, embeds, and Obsidian syntax
- `large-vault-safety.md` - Safety protocols for bulk operations
- `selection-scope-obsidian.md` - Respects user selections and boundaries

### **MANUAL Rules** (Workflow Assistance)
- `portable-tools-integration.md` - Smart tool suggestions and integration

## 🚀 **Quick Setup**

### **Step 1: Copy to Your Project**
1. Copy the `portable-obsidian-tools/` folder to your Obsidian project root
2. Navigate to your project's cursor rules settings

### **Step 2: Add the Rules**
Copy the content from each `.md` file into separate cursor rules:

```markdown
Rule Name: obsidian-syntax-preservation
Type: ALWAYS
Content: [Copy from obsidian-syntax-preservation.md]

Rule Name: large-vault-safety  
Type: ALWAYS
Content: [Copy from large-vault-safety.md]

Rule Name: selection-scope-obsidian
Type: ALWAYS  
Content: [Copy from selection-scope-obsidian.md]

Rule Name: portable-tools-integration
Type: MANUAL
Content: [Copy from portable-tools-integration.md]
```

### **Step 3: Test the Integration**
Try this prompt to verify everything works:
```
I want to clean up markdown formatting in my vault. What's the safest approach?
```

## 🎯 **Why These Rules?**

### **Obsidian Syntax Preservation**
- Prevents accidental corruption of WikiLinks `[[]]`
- Protects embeds, block references, and tags
- Maintains Templater syntax integrity

### **Large Vault Safety**
- Prevents disasters in 1000+ page vaults
- Enforces testing before bulk operations
- Requires explicit confirmation for risky operations

### **Selection Scope**
- Respects user selections precisely
- Prevents unintended changes outside selection
- Handles Obsidian syntax boundaries intelligently

### **Portable Tools Integration**
- Provides smart tool suggestions
- Explains backup and safety features
- Offers appropriate commands for common tasks

## 🔧 **Customization**

### **For Smaller Vaults (< 500 pages)**
- Consider setting `large-vault-safety` to MANUAL instead of ALWAYS
- Reduce batch size suggestions in safety protocols

### **For Different Workflows**
- Modify tool suggestions in `portable-tools-integration.md`
- Add custom Obsidian syntax patterns to `obsidian-syntax-preservation.md`
- Adjust safety thresholds in `large-vault-safety.md`

## 📊 **Expected Behavior**

### **With These Rules Active**
- ✅ WikiLinks and embeds are never accidentally broken
- ✅ Bulk operations require confirmation and testing
- ✅ User selections are respected precisely
- ✅ Appropriate tools are suggested for common tasks
- ✅ Backup system is always explained before destructive operations

### **Safety Features**
- All destructive operations create automatic backups
- Dry-run mode is offered for testing
- Scope confirmation is required for bulk operations
- Restore instructions provided after operations

## 🚨 **Important Notes**

1. **Test First**: Always test rules on a small subset of files
2. **Backup**: Ensure your vault is backed up before applying rules
3. **Gradual Rollout**: Start with MANUAL rules, then enable ALWAYS rules
4. **Monitor**: Watch for any unexpected behavior and adjust as needed

---

**Status**: Production-ready for large Obsidian vaults  
**Compatibility**: Optimized for 1000+ page vaults with portable-obsidian-tools  
**Maintenance**: Update tool suggestions as new tools are added to the portable toolkit 