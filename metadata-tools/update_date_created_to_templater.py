import os
import re

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATER_SYNTAX = 'date-created: <% tp.file.creation_date("YYYY-MM-DD") %>'

changed_files = []

for root, dirs, files in os.walk(VAULT_ROOT):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Regex to find static date-created (not already Templater)
            pattern = r'^(date-created: )(?!<% tp\.file\.creation_date\()[^\n]+$'
            if re.search(pattern, content, re.MULTILINE):
                new_content = re.sub(pattern, TEMPLATER_SYNTAX, content, flags=re.MULTILINE)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                changed_files.append(path)

print(f"Updated {len(changed_files)} files.")
if changed_files:
    print("Files changed:")
    for p in changed_files:
        print(f"- {os.path.relpath(p, VAULT_ROOT)}") 