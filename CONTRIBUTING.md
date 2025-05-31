# Contributing to Professional Markdown Toolkit

Thank you for your interest in contributing to the Professional Markdown Toolkit! This project aims to provide robust, professional-grade tools for markdown processing and document automation.

## 🎯 Project Goals

- **Professional Quality**: All tools should meet enterprise/executive standards
- **Safety First**: Scripts should never destroy content, only improve formatting
- **Cross-Platform**: Support macOS, Linux, and Windows (via WSL)
- **Documentation**: Every script should be well-documented with clear usage examples

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** for your changes
4. **Test thoroughly** before submitting

## 📝 Types of Contributions

### **New Scripts**
- Markdown processing utilities
- Obsidian vault management tools
- Document generation automation
- Metadata processing scripts

### **Improvements**
- Performance optimizations
- Better error handling
- Enhanced documentation
- Cross-platform compatibility fixes

### **Bug Fixes**
- Content preservation issues
- Unicode/encoding problems
- Path handling bugs
- Platform-specific issues

## 🛠️ Development Guidelines

### **Code Standards**
- **Python**: Follow PEP 8 style guidelines
- **Bash**: Use `set -e` for error handling
- **Comments**: Explain complex logic and regex patterns
- **Error Handling**: Graceful failure with clear messages

### **Safety Requirements**
- **Never modify content** - only formatting
- **Preserve YAML frontmatter** in markdown files
- **Backup recommendations** in documentation
- **Dry-run modes** for destructive operations

### **Testing**
- Test with various file sizes (small, large, very large)
- Test with Unicode content and special characters
- Test error conditions (missing files, permissions, etc.)
- Test on different platforms when possible

## 📋 Submission Process

### **Before Submitting**
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Add usage examples** for new features
4. **Check for breaking changes**

### **Pull Request Guidelines**
- **Clear title** describing the change
- **Detailed description** of what and why
- **Test results** showing before/after
- **Documentation updates** included

### **Commit Messages**
```
feat: add batch markdown cleanup with dry-run mode
fix: preserve YAML frontmatter in template application
docs: update README with new script usage examples
refactor: improve error handling in metadata tools
```

## 🧪 Testing Your Changes

### **Basic Testing**
```bash
# Test markdown processing
python markdown-processing/cleanup_markdown_batch.py test_file.md --dry-run

# Test template application
python obsidian-tools/apply_inbox_template.py test_note.md

# Test document generation
cd company-executive && ./build-consolidated-doc.sh
```

### **Edge Cases to Test**
- Empty files
- Files with only YAML frontmatter
- Very large files (>1MB)
- Files with Unicode characters
- Files with Windows line endings
- Missing or corrupted files

## 📚 Documentation Standards

### **Script Documentation**
Each script should include:
- **Purpose**: What problem it solves
- **Usage**: Command-line examples
- **Options**: All available flags and parameters
- **Safety**: What it preserves/modifies
- **Examples**: Real-world usage scenarios

### **README Updates**
When adding new scripts:
- Add to appropriate category section
- Include usage examples
- Update the directory structure diagram
- Add to Quick Start Guide if applicable

## 🐛 Reporting Issues

### **Bug Reports**
Include:
- **Operating system** and version
- **Python version** (`python --version`)
- **Exact command** that failed
- **Error message** (full output)
- **Sample file** that reproduces the issue (if possible)

### **Feature Requests**
Include:
- **Use case**: What problem would this solve?
- **Proposed solution**: How should it work?
- **Alternatives**: What workarounds exist currently?

## 🏆 Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Invited to help maintain the project

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Documentation**: Check README and script comments first

## 🎉 Thank You!

Every contribution helps make this toolkit more useful for the community. Whether it's a bug fix, new feature, or documentation improvement, your help is appreciated!

---

**Remember**: This toolkit is used in professional environments, so quality and reliability are paramount. When in doubt, err on the side of caution and safety. 