import re

TEST_FILE = '0-inbox/2025-05-05-1302-Untitled.md'
TEMPLATE_YAML = '''---
date-created: <% tp.file.creation_date("YYYY-MM-DD") %>
date-updated: <% tp.date.now("YYYY-MM-DD") %>
status: []
category:
tags:
author:
linked-notes:
source: ""
priority:
---
'''
TEMPLATER_BLOCK = '''<%*
try {
    const folder = tp.file.folder(true);
    const dateTime = tp.file.creation_date("YYYY-MM-DD-HHmm");
    const currentName = tp.file.title;
    const nameWithoutDate = currentName.replace(/^\\d{4}-\\d{2}-\\d{2}-\\d{4}-?/, "");
    const newName = `${dateTime}-${nameWithoutDate}`;
    await tp.file.rename(newName);
} catch (error) {
    console.error("Templater: File rename failed!", error);
    tR += "\n\n**Templater Error:** File rename failed. Check console (Ctrl+Shift+I)\n\n";
}
-%>\n'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any YAML frontmatter (from --- to ---)
    content_no_yaml = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

    # Find the file name display line (first line starting with `= this.file.name`)
    lines = content_no_yaml.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.strip().startswith('`= this.file.name`'):
            file_name_line = line
            rest_of_content = ''.join(lines[i+1:])
            break
    else:
        file_name_line = ''
        rest_of_content = content_no_yaml

    new_content = TEMPLATE_YAML + TEMPLATER_BLOCK + file_name_line + rest_of_content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")

if __name__ == '__main__':
    update_file(TEST_FILE) 