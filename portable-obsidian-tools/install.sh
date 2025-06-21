#!/bin/bash
# Portable Obsidian Tools - Quick Installation Script

echo "🚀 Setting up Portable Obsidian Tools..."

# Make scripts executable
echo "📝 Setting script permissions..."
chmod +x obsidian-tools/*.sh
chmod +x metadata-tools/*.sh
chmod +x shared/*.sh
chmod +x PROJECT-STRUCTURE/*.py

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
echo "🎯 Quick test - run this from your project root:"
echo "   portable-obsidian-tools/obsidian-tools/apply_template.sh --help"
echo ""
echo "📚 See README.md for complete usage guide" 