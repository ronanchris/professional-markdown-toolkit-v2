---
title: Edge Cases Test Document
---

# Multiple File Name References

First reference: `= this.file.name`

Some content here.

Second reference: `= this.file.name`

## Multiple Templater Blocks

<%*
// First block
console.log("First block");
-%>

Content between blocks.

<%*
// Second block with complex logic
try {
    const result = await someComplexOperation();
    tR += `Result: ${result}`;
} catch (e) {
    tR += "Error occurred";
}
-%>

More content.

<%*
// Third block - simple
tR += "Simple addition";
-%>

## Inline Templater

Date: <% tp.date.now() %> and time: <% tp.date.now("HH:mm") %>

Multiple inline: <% tp.file.title %> in <% tp.file.folder() %>

## Mixed Content

Regular **bold** and *italic* text.

- List item with <% tp.date.now() %>
- Another item
- `= this.file.name` in a list

### Code Blocks vs Templater

```javascript
// This is a regular code block
function test() {
    return "not templater";
}
```

<%*
// This IS a templater block
function templaterFunction() {
    return "templater code";
}
-%>

## Empty and Minimal Cases

<%*
-%>

Empty templater block above.

`= this.file.name`

Just a file reference.

## Edge Case: No closing frontmatter

If frontmatter was malformed at start, content continues here... 