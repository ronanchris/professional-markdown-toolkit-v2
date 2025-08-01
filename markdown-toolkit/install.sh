#!/bin/bash
# Markdown Processing Tools - Installation Script

echo "🧹 Setting up Markdown Processing Tools..."

# Make scripts executable
echo "📝 Setting script permissions..."
chmod +x tools/*.sh
chmod +x shared/*.sh

# Make Python scripts executable
echo "🐍 Setting Python script permissions..."
chmod +x tools/*.py

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
echo "🎯 Available tools:"
echo "   📄 All-in-one fixer:     python tools/notion_complete_fixer.py"
echo "   🔤 Unicode cleaner:      python tools/unicode_cleaner.py"
echo "   🔗 WikiLink converter:   python tools/wikilink_converter.py"
echo "   🧹 Batch cleanup:        python tools/cleanup_markdown_batch.py"
echo ""
echo "📚 Usage guide: tools/README-NOTION-TOOLS.md"
echo "🎯 Quick start: python tools/notion_complete_fixer.py your-file.md" 