---
created: 12/25/2023
date-updated: Dec 25, 2023
title:  My Messy Note   
tags: project,important,#work
status:draft
---

<%*
// This is unprocessed Templater code that should be cleaned up
try {
    const folder = tp.file.folder(true);
    const dateTime = tp.file.creation_date("YYYY-MM-DD-HHmm");
    const currentName = tp.file.title;
    const nameWithoutDate = currentName.replace(/^\d{4}-\d{2}-\d{2}-\d{4}-?/, "");
    const newName = `${dateTime}-${nameWithoutDate}`;
    await tp.file.rename(newName);
} catch (error) {
    console.error("Templater: File rename failed!", error);
}
-%>

#This heading has no space
##  This one has too many spaces
###Inconsistent formatting everywhere

File name: `= this.file.name`

- Mixed bullet types
* Different symbols  
+ Even more variation
    - Inconsistent indentation
  - Wrong indentation


Here's some content with    trailing spaces    
And multiple blank lines below:




More content with inconsistent formatting.

*  Another list with bad formatting
   *  Weird indentation 
*Wrong indentation

## Another   heading with   weird spacing

Content here. 