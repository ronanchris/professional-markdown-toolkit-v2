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
   cd portable-obsidian-ai-tools && ./install.sh && cd ..
   ```

2. **Set Up Session Continuity Framework:**
   ```bash
   mkdir -p session-continuity
   echo "Session continuity templates available in portable-obsidian-ai-tools/session-continuity/"
   echo "Ready for guided customization through AI interviews"
   ```

3. **Display Cursor Rules Setup Instructions:**
   After completing the above, please:
   - Read the contents of `portable-obsidian-ai-tools/.cursorrules`
   - Tell me: "The toolkit is deployed! Now you need to copy the cursor rules. I'll show you the complete rules file content below. Please copy it and paste it into your project's `.cursorrules` file."
   - Display the complete contents of the `.cursorrules` file for me to copy

4. **Verify Installation:**
   ```bash
   ls -la portable-obsidian-ai-tools/
   echo "🎯 Available tools:"
   echo "- Notion import fixes: portable-obsidian-ai-tools/obsidian-tools/markdown-processing/"
   echo "- Metadata tools: portable-obsidian-ai-tools/obsidian-tools/metadata-tools/"
   echo "- Template management: portable-obsidian-ai-tools/obsidian-tools/template-management/"
   echo "- AI collaboration: portable-obsidian-ai-tools/ai-collaboration/"
   echo "- Quick reference: portable-obsidian-ai-tools/DEAD-SIMPLE.md"
   ```

5. **Set Up Blog Learning Moments:**
   ```bash
   cp portable-obsidian-ai-tools/session-continuity/12-BLOG-LEARNING-MOMENTS-TEMPLATE.md ./BLOG-LEARNING-MOMENTS.md
   ```

6. **Session Continuity Setup Interview:**
   Please offer to help me set up my complete session continuity system by saying:
   
   "Great! The toolkit is deployed and ready. Now I can help you set up a personalized AI collaboration system for your project through guided interviews. The session continuity templates in `portable-obsidian-ai-tools/session-continuity/` have AI customization triggers that make setup easy.
   
   **Standard Operating Procedure:**
   1. **Choose templates** you want (start with core 4: PROJECT-REQUIREMENTS, SESSION-PLAN, CURRENT-STATE, AI-COLLABORATION)
   2. **Open each template** → I'll automatically offer guided interview
   3. **Complete interviews** → I'll customize templates for your project  
   4. **Save customized versions** → In your project's `session-continuity/` folder (remove -TEMPLATE from filename)
   5. **Keep templates unchanged** → For future projects
   
   Would you like me to start with the 4 core templates, or do you want to customize them manually? The guided interviews usually take 10-15 minutes total and ensure everything works together perfectly."
   
   If I say yes, guide me through customizing each template:
   - Open `portable-obsidian-ai-tools/session-continuity/01-PROJECT-REQUIREMENTS-TEMPLATE.md` and trigger the AI interview
   - Then `02-SESSION-PLAN-TEMPLATE.md`, `03-CURRENT-STATE-TEMPLATE.md`, `04-AI-COLLABORATION-TEMPLATE.md`
   - For each: Complete interview → Save as `session-continuity/[filename without -TEMPLATE].md`

7. **Verify Blog Auto-Creation System:**
   - Confirm that `BLOG-LEARNING-MOMENTS.md` file exists in project root
   - Test blog auto-creation by saying "This insight about [something innovative] could help others"
   - Verify AI offers to create blog post automatically

8. **Final Setup Instructions:**
   After completing all steps above, please say:
   
   "🎉 Deployment complete! The Portable Obsidian AI Tools are now installed in your project. 
   
   **Next steps:**
   1. See `POST-DEPLOYMENT-GUIDE.md` for what to do next
   2. Use `SESSION-ENTRANCE-PROMPT-GENERIC.md` to set up AI context for this specific project
   3. Test the automation by saying 'Let's start working on the project'
   
   The toolkit is ready to enhance your AI collaboration with session continuity, automatic progress tracking, and intelligent triggers!"

Please execute all these steps and let me know when the deployment is complete.
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