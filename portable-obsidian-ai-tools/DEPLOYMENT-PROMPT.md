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

6. **Set Up Blog Learning Moments:**
   ```bash
   cp portable-obsidian-ai-tools/ai-collaboration/universal-session-continuity/BLOG-LEARNING-MOMENTS-TEMPLATE.md ./BLOG-LEARNING-MOMENTS.md
   ```

7. **Session Continuity Setup Interview:**
   Please offer to help me set up my complete session continuity system by saying:
   
   "Great! The toolkit is deployed and ready. Now I can help you set up a personalized AI collaboration system for your project through guided interviews. This usually takes 10-15 minutes and gives you a completely customized system.
   
   I can help you configure:
   - 📋 **Project context and goals** (session-continuity/CURRENT-PROJECT-CONTEXT.md)
   - 🤝 **Collaboration style preferences** (session-continuity/COLLABORATION-STYLE.md)  
   - 📝 **Blog learning moments** (BLOG-LEARNING-MOMENTS.md)
   - 🤖 **AI collaboration enhancements** (session-continuity/AI-COLLABORATION-CURSOR-RULES.md)
   
   Would you like me to walk you through setting up all of these, or would you prefer to customize them manually? I recommend the guided setup - it ensures everything works together perfectly."
   
   If I say yes, guide me through customizing each template using their built-in AI interview triggers.

8. **Verify Blog Auto-Creation System:**
   - Confirm that `BLOG-LEARNING-MOMENTS.md` file exists in project root
   - Test blog auto-creation by saying "This insight about [something innovative] could help others"
   - Verify AI offers to create blog post automatically

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

### **Complete System Setup:**
- ✅ Offers comprehensive session continuity configuration
- ✅ Guides you through customizing ALL key templates via interviews
- ✅ Creates a fully personalized AI collaboration system
- ✅ Tests and verifies everything works together

## 🚀 **Usage Instructions:**

1. **Open your new project** (e.g., Parkinson's documentation)
2. **Copy the entire deployment prompt** from the box above
3. **Paste it to your Cursor agent**
4. **Follow the cursor rules setup** when prompted
5. **Start using the toolkit** immediately

## 🎯 **Benefits:**

- **One command** deploys everything
- **Zero manual file copying** (except cursor rules)
- **Complete system configuration** through guided interviews
- **Personalized AI collaboration setup** (10-15 minutes)
- **Ready-to-use templates** customized for your specific project
- **No technical knowledge required**

This makes the toolkit truly **"drop-in ready"** for any project! 🚀 