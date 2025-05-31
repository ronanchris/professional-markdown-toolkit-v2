---
title: Malformed Frontmatter Test
tags: [test, malformed]
date-created: 2024-12-01
# This comment should not be in frontmatter
status: draft
# Another problematic comment
nested:
  key1: value1
  key2: value2
  # Nested comment (problematic)
---

# Test Document with Malformed Frontmatter

This document has some issues in the frontmatter that should be handled gracefully.

## Content Section

Regular content here.

<%*
// Some Templater code
const name = tp.file.title;
tR += `Processing file: ${name}`;
-%>

More content with `= this.file.name` reference.

Another section here. 