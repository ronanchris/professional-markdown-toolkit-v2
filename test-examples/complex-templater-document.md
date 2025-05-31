---
title: Complex Document with Templater
tags: [templater, testing, complex]
date-created: 2024-12-01
author: Test User
status: active
priority: high
linked-notes: [[Other Note]], [[Reference]]
source: "https://example.com/source"
category: projects
---

<%*
// Complex Templater code block with file operations
try {
    const folder = tp.file.folder(true);
    const dateTime = tp.file.creation_date("YYYY-MM-DD-HHmm");
    const currentName = tp.file.title;
    
    // Remove existing date prefix if present
    const nameWithoutDate = currentName.replace(/^\d{4}-\d{2}-\d{2}-\d{4}-?/, "");
    const newName = `${dateTime}-${nameWithoutDate}`;
    
    // Rename file with timestamp
    await tp.file.rename(newName);
    
    // Add to daily note
    const dailyNote = tp.date.now("YYYY-MM-DD");
    const dailyPath = `daily-notes/${dailyNote}.md`;
    
    if (await tp.file.exists(dailyPath)) {
        const content = await tp.file.read(dailyPath);
        const newContent = content + `\n- [[${newName}]] - Created at <% tp.date.now("HH:mm") %>`;
        await tp.file.write(newContent, dailyPath);
    }
    
} catch (error) {
    console.error("Templater: Complex operations failed!", error);
    tR += "\n\n**Templater Error:** Complex operations failed. Check console (Ctrl+Shift+I)\n\n";
}
-%>

# `= this.file.name`

## Metadata Information

**Created**: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
**Modified**: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
**Folder**: <% tp.file.folder() %>

## Dynamic Content

Current time: <% tp.date.now("HH:mm:ss") %>
Random ID: <% Math.random().toString(36).substr(2, 9) %>

### Templater Variables
- File path: <% tp.file.path() %>
- File extension: <% tp.file.extension %>
- File size: <% tp.file.size %>

<%*
// Secondary code block for additional processing
const words = ["innovation", "collaboration", "excellence", "growth"];
const randomWord = words[Math.floor(Math.random() * words.length)];
tR += `\n## Focus Area: ${randomWord}\n`;
-%>

## Regular Content

This document contains both Templater syntax and regular markdown content.

### Lists and Formatting

- Regular bullet point
- Another point with **bold** text
- Point with `inline code`

1. Numbered list item
2. Second numbered item
3. Third item with [external link](https://example.com)

### Code Block

```javascript
// Regular code block (not Templater)
function example() {
    console.log("This is regular code");
    return true;
}
```

### Links and References

- Internal link: [[Another Document]]
- External link: [Example](https://example.com)
- Email: contact@example.com

## Complex Tables

| Column 1 | Column 2 | Templater Date |
|----------|----------|----------------|
| Data 1   | Data 2   | <% tp.date.now("YYYY-MM-DD") %> |
| Info A   | Info B   | Static content |

---

## Footer Information

Document created with complex Templater integration.
File name reference: `= this.file.name`

<%*
// Final processing block
tR += "\n\n---\n**Auto-generated footer:** " + tp.date.now("YYYY-MM-DD HH:mm:ss");
-%> 