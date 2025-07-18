# One-Shot Deployment Prompt for Portable Obsidian AI Tools

Copy and paste this entire prompt to your Cursor agent in any new project to automatically deploy the complete toolkit.

---

## 🚀 **DEPLOYMENT PROMPT** (Copy Everything Below)

```
Please help me deploy the Portable Obsidian AI Tools from GitHub into this project. Here's what I need you to do:

1. **Clone and Deploy:**
   ```bash
   git clone https://github.com/ronanchris/professional-markdown-toolkit.git temp-toolkit
   cp -r temp-toolkit/portable-obsidian-ai-tools ./
   rm -rf temp-toolkit
   ```

2. **Run Installation:**
   ```bash
   cd portable-obsidian-ai-tools
   chmod +x install.sh
   ./install.sh
   cd ..
   ```

3. **Set Up Session Continuity Templates:**
   ```bash
   cp -r portable-obsidian-ai-tools/ai-collaboration/universal-session-continuity ./session-continuity
   ```

4. **Display Cursor Rules Setup Instructions:**
   After completing the above, please:
   - Read the contents of `portable-obsidian-ai-tools/.cursorrules`
   - Tell me: "The toolkit is deployed! Now you need to copy the cursor rules. I'll show you the complete rules file content below. Please copy it and paste it into your `.cursor/rules/cursorrules.mdc` file."
   - Display the complete contents of the `.cursorrules` file for me to copy

5. **Verify Installation:**
   ```bash
   ls -la portable-obsidian-ai-tools/
   echo "🎯 Available tools:"
   echo "- Notion import fixes: portable-obsidian-ai-tools/obsidian-tools/markdown-processing/"
   echo "- Metadata tools: portable-obsidian-ai-tools/obsidian-tools/metadata-tools/"
   echo "- Template management: portable-obsidian-ai-tools/obsidian-tools/template-management/"
   echo "- AI collaboration: portable-obsidian-ai-tools/ai-collaboration/"
   echo "- Quick reference: portable-obsidian-ai-tools/DEAD-SIMPLE.md"
   ```

6. **Test Template Interview System:**
   - Open `session-continuity/CURRENT-PROJECT-CONTEXT.md`
   - Offer to run the AI customization interview to set up my project context
   - Walk me through the guided setup if I say yes

Please execute all these steps and let me know when the deployment is complete and ready for the cursor rules setup.
```

---

## 🎯 **What This Prompt Does:**

### **Automated Setup:**
- ✅ Clones repo and copies toolkit
- ✅ Runs installation script
- ✅ Sets up session continuity templates
- ✅ Verifies all tools are available

### **Guided Cursor Rules Setup:**
- ✅ Shows you the complete rules content
- ✅ Tells you exactly where to paste it
- ✅ No guessing about file paths or content

### **Immediate Activation:**
- ✅ Tests the template interview system
- ✅ Offers to customize your first template
- ✅ Confirms everything is working

## 🚀 **Usage Instructions:**

1. **Open your new project** (e.g., Parkinson's documentation)
2. **Copy the entire deployment prompt** from the box above
3. **Paste it to your Cursor agent**
4. **Follow the cursor rules setup** when prompted
5. **Start using the toolkit** immediately

## 🎯 **Benefits:**

- **One command** deploys everything
- **Zero manual file copying** (except cursor rules)
- **Immediate verification** that everything works
- **Guided first-time setup** with template interviews
- **No technical knowledge required**

This makes the toolkit truly **"drop-in ready"** for any project! 🚀 