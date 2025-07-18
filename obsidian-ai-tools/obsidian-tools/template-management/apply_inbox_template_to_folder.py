import os
import re

INBOX_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '0-inbox')
TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '3-resources', 'templates', 'inbox-template.md')

# Read the template YAML and Templater block
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template_content = f.read()

# Split template at the second ---
template_parts = template_content.split('---')
if len(template_parts) < 3:
    raise ValueError('Template file does not have two --- YAML delimiters.')
template_yaml = '---' + template_parts[1] + '---\n' + template_parts[2].lstrip('\n')

changed_files = []

for file in os.listdir(INBOX_DIR):
    if file.endswith('.md'):
        path = os.path.join(INBOX_DIR, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove existing YAML frontmatter if present
        new_content = content
        if content.startswith('---'):
            # Remove everything from the first --- to the next ---
            match = re.match(r'^---.*?---\s*', content, re.DOTALL)
            if match:
                new_content = content[match.end():]
        # Prepend the template YAML and Templater block
        updated = template_yaml + '\n' + new_content.lstrip('\n')
        if updated != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(updated)
            changed_files.append(file)

print(f"Updated {len(changed_files)} files in 0-inbox.")
if changed_files:
    print("Files changed:")
    for f in changed_files:
        print(f"- {f}") 