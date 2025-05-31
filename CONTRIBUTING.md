# Contributing to Professional Markdown Toolkit

Thank you for your interest in contributing to this professional Obsidian vault management toolkit!

## 🎯 **Project Vision**

- **Professional Quality**: All tools should meet enterprise standards
- **Obsidian Focus**: Specialized for Obsidian vault management and markdown processing
- **Security First**: Comprehensive backup systems and safe operations
- **User-Friendly**: Clear documentation and helpful error messages
- **Cross-Platform**: Works on macOS, Linux, and Windows WSL

## 🛠️ **Development Setup**

### **Prerequisites**
- Python 3.8+ 
- Bash shell environment
- Git for version control
- Obsidian vault for testing (recommended)

### **Local Setup**
```bash
# Clone the repository
git clone https://github.com/ronanchris/professional-markdown-toolkit.git
cd professional-markdown-toolkit

# Install dependencies
pip install -r requirements.txt

# Make scripts executable (if needed)
find . -name "*.sh" -exec chmod +x {} \;
```

## 📋 **Contribution Guidelines**

### **Types of Contributions Welcome**
1. **Bug fixes** - Security issues, script failures, documentation errors
2. **Feature enhancements** - New Obsidian tools, improved workflows
3. **Documentation** - Better guides, examples, troubleshooting
4. **Testing** - Cross-platform validation, edge case testing
5. **Security improvements** - Safer operations, better validation

### **Code Standards**

#### **Shell Scripts (.sh)**
```bash
#!/bin/bash
set -e  # Exit on error
set -u  # Exit on undefined variable

# Use relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Include backup functionality
source "$SCRIPT_DIR/../shared/backup-functions.sh"

# Add help option
if [[ "${1:-}" == "--help" ]]; then
    echo "Usage: $0 [options]"
    exit 0
fi
```

#### **Python Scripts (.py)**
```python
#!/usr/bin/env python3
import sys
import os

def check_dependencies():
    """Check required dependencies are available."""
    missing = []
    try:
        import yaml
    except ImportError:
        missing.append("PyYAML (pip install pyyaml)")
    
    if missing:
        print("Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        sys.exit(1)

# Always include dependency checks
check_dependencies()
```

### **Security Requirements**
- ✅ **No hardcoded paths** - Use relative path resolution
- ✅ **Backup integration** - All destructive operations must include backup options
- ✅ **Input validation** - Validate all user inputs and file paths
- ✅ **Error handling** - Graceful failure with helpful error messages
- ✅ **Safe operations** - No `eval`, proper quoting, validated commands

### **Testing Standards**
```bash
# Test with dry-run mode first
./your-script.sh --dry-run

# Test with minimal test data
# Test error conditions
# Test backup and restore functionality
```

## 🔧 **Development Workflow**

### **1. Issue Creation**
- Check existing issues first
- Use issue templates for bug reports
- Include clear reproduction steps
- Add appropriate labels

### **2. Development Process**
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes following code standards
# Test thoroughly in safe environment

# Commit with clear messages
git commit -m "feat: add backup functionality to metadata tools"

# Push and create pull request
git push origin feature/your-feature-name
```

### **3. Pull Request Guidelines**
- **Clear description** of changes made
- **Testing evidence** - show scripts work correctly  
- **Security review** - confirm no new vulnerabilities
- **Documentation updates** - update README if needed
- **Backward compatibility** - don't break existing workflows

## 🧪 **Testing Your Changes**

### **Required Testing**
```bash
# 1. Individual script testing
./your-script.sh --help
./your-script.sh --dry-run

# 2. Integration testing
# Test with real Obsidian vault (backup first!)

# 3. Error condition testing
# Test with missing files, invalid inputs, etc.

# 4. Backup system testing
# Verify backups are created and can be restored
```

### **Testing Checklist**
- [ ] Script runs without errors
- [ ] Help documentation is accurate
- [ ] Dry-run mode works correctly
- [ ] Backup functionality works
- [ ] Error messages are helpful
- [ ] No hardcoded paths used
- [ ] Works on intended platforms

## 📚 **Documentation Standards**

### **Code Documentation**
- Clear comments explaining complex logic
- Function docstrings for Python code
- Usage examples in script headers

### **User Documentation**
- Update README.md for new features
- Add troubleshooting entries when relevant
- Include real usage examples

## 🚀 **Release Process**

### **Pre-Release Checklist**
- [ ] All tests pass on target platforms
- [ ] Security audit completed
- [ ] Documentation updated
- [ ] Version numbers incremented
- [ ] Changelog updated

### **Versioning**
We use semantic versioning:
- **Major** (1.0.0) - Breaking changes
- **Minor** (0.1.0) - New features, backward compatible
- **Patch** (0.0.1) - Bug fixes, backward compatible

## 🤝 **Community Guidelines**

### **Communication**
- Be respectful and constructive
- Focus on technical merit
- Help others learn and improve
- Share knowledge and best practices

### **Issue Discussion**
- Stay on topic
- Provide helpful debugging information
- Test suggested solutions
- Report back on outcomes

## 📞 **Getting Help**

- **Documentation**: Check README.md and related guides first
- **Issues**: Search existing issues before creating new ones  
- **Discussions**: Use GitHub Discussions for general questions
- **Security**: Report security issues privately via email

## 🏆 **Recognition**

Contributors are recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special recognition for security improvements

Thank you for helping make Obsidian vault management more professional and reliable! 