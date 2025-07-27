#!/bin/bash
# Obsidian AI Tools - Quick Installation Script

echo "🚀 Setting up Obsidian AI Tools..."

# Make scripts executable
echo "📝 Setting script permissions..."
chmod +x obsidian-tools/metadata-tools/*.sh
chmod +x obsidian-tools/template-management/*.sh
chmod +x obsidian-tools/markdown-processing/*.sh
chmod +x shared/*.sh

# Make Python scripts executable
echo "🐍 Setting Python script permissions..."
chmod +x obsidian-tools/project-structure/*.py
chmod +x obsidian-tools/markdown-processing/*.py
chmod +x obsidian-tools/metadata-tools/*.py
chmod +x obsidian-tools/template-management/*.py

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    echo "Please install Python 3.7+ and try again"
    exit 1
fi

# Check if pip is available
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip is required but not found"
    echo "Please install pip and try again"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
else
    pip install -r requirements.txt
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "🎯 Quick tests - run these from your project root:"
echo "   obsidian-ai-tools/obsidian-tools/template-management/apply_template.sh --help"
echo "   python obsidian-ai-tools/obsidian-tools/markdown-processing/notion_complete_fixer.py --help"
echo ""
echo "📚 See TOOLKIT-GUIDE.md or DEAD-SIMPLE.md for complete usage guide"
echo ""
echo "🧠 For AI collaboration enhancement:"
echo "   Use session continuity templates with AI interviews for guided setup" 