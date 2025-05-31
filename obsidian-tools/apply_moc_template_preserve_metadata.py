import os
import re
import sys

def check_dependencies():
    """Check if required dependencies are available."""
    missing = []
    try:
        import yaml
    except ImportError:
        missing.append("PyYAML (install with: pip install pyyaml)")
    
    if missing:
        print("Error: Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        print("\nTo install all dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)

# Check dependencies before importing
check_dependencies()
import yaml

MOC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '00-MOCs')
TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '3-resources', 'templates', 'moc-template.md')

# Read the template YAML and Templater block
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_lines = f.readlines()

# Extract YAML lines (between first two ---)
yaml_start = None
yaml_end = None
for i, line in enumerate(template_lines):
    if line.strip() == '---':
        if yaml_start is None:
            yaml_start = i
        elif yaml_end is None:
            yaml_end = i
            break
if yaml_start is None or yaml_end is None or yaml_end <= yaml_start:
    raise ValueError('Template file does not have valid YAML frontmatter.')
template_yaml = ''.join(template_lines[yaml_start+1:yaml_end])
template_after_yaml = ''.join(template_lines[yaml_end+1:])

fields_to_preserve = ['tags', 'category', 'author', 'linked-notes']

changed_files = []

for file in os.listdir(MOC_DIR):
    if file.endswith('.md'):
        path = os.path.join(MOC_DIR, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Extract existing YAML frontmatter
        orig_yaml_dict = {}
        orig_yaml = ''
        if content.startswith('---'):
            match = re.match(r'^---(.*?)---\s*', content, re.DOTALL)
            if match:
                orig_yaml = match.group(1)
                try:
                    orig_yaml_dict = yaml.safe_load(orig_yaml) or {}
                except Exception:
                    orig_yaml_dict = {}
                content_after_yaml = content[match.end():]
            else:
                content_after_yaml = content
        else:
            content_after_yaml = content
        # Load template YAML as dict
        template_yaml_dict = yaml.safe_load(template_yaml)
        # Overwrite template fields with preserved fields from original
        for key in fields_to_preserve:
            if key in orig_yaml_dict:
                template_yaml_dict[key] = orig_yaml_dict[key]
        # Rebuild YAML frontmatter
        new_yaml = '---\n' + yaml.dump(template_yaml_dict, sort_keys=False, allow_unicode=True) + '---\n'
        # Add Templater block and rest of file
        updated = new_yaml + template_after_yaml + '\n' + content_after_yaml.lstrip('\n')
        if updated != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)
            changed_files.append(file)

print(f"Updated {len(changed_files)} files in 00-MOCs.")
if changed_files:
    print("Files changed:")
    for f in changed_files:
        print(f"- {f}") 