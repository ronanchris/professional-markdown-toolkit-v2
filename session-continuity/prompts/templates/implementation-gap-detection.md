# Implementation Gap Detection Template

## 🔍 **Template Usage**
Use this template when you suspect there's a disconnect between how a system is designed to work and how it actually works in practice.

## 📋 **Gap Detection Prompt Template**

```
I see the system is designed to [DESCRIBE EXPECTED BEHAVIOR]. If it were working correctly, wouldn't we see [DESCRIBE EXPECTED EVIDENCE]? 

Let's validate whether our design matches our implementation:

**EXPECTED BEHAVIOR**:
- [What should be happening automatically?]
- [What should trigger without manual intervention?]
- [What evidence should we see if it's working?]

**ACTUAL REALITY**:
- [What's actually happening instead?]
- [What requires manual intervention that shouldn't?]
- [What evidence is missing or different?]

**VALIDATION APPROACH**:
- [How can we test this specific gap?]
- [What would prove the system is working as designed?]
- [How can we test this recursively to catch similar gaps?]

**FOCUS QUESTIONS**:
- Are we solving the right problem or just symptoms?
- Is this a design issue or implementation issue?
- What's the simplest test that would reveal the truth?

Focus on reality vs. aspiration. Let's test with real scenarios, not artificial examples.
```

## 🔧 **Common Implementation Gaps**

**Session Management Systems:**
- **Design**: Session continuity should auto-update documents
- **Reality**: Updates require manual intervention
- **Test**: "If I complete a task, does SESSION-PLAN.md automatically update?"

**Automation Triggers:**
- **Design**: AI should auto-detect completion phrases
- **Reality**: AI responds only when explicitly told
- **Test**: Say "That's complete" and see if checkboxes auto-update

**Template Systems:**
- **Design**: Templates should auto-trigger interview process
- **Reality**: Templates sit unused without manual activation
- **Test**: Open template file and see if AI offers customization

**Date Validation:**
- **Design**: AI should always ask for date confirmation
- **Reality**: AI assumes dates or uses wrong timestamps
- **Test**: Ask AI to add a timestamp and see if it validates first

## 🎯 **Effective Gap Detection Phrases**

**Trigger Phrases for Gap Detection:**
- "If the system were working, wouldn't X happen?"
- "Did you just do X because I asked, or is that automatic?"
- "I don't see Y having been updated"
- "This should be working automatically, but..."
- "The design says X, but I'm seeing Y"

**Follow-up Questions:**
- "How can we test if this gap exists elsewhere?"
- "What other automations might have similar issues?"
- "Is this a documentation problem or implementation problem?"
- "What would make this work automatically next time?"

## 📊 **Gap Resolution Protocol**

**When Gap Detected:**
1. ✅ **Acknowledge** the gap between design and implementation
2. ✅ **Document** the specific mismatch discovered
3. ✅ **Test** whether it's isolated or systematic
4. ✅ **Fix** the immediate implementation gap
5. ✅ **Update** documentation and rules to prevent recurrence
6. ✅ **Validate** the fix actually works automatically

**Success Metrics:**
- Gap is closed, not just papered over
- Automation works without manual intervention
- Similar gaps are prevented by systemic fixes
- System behavior matches designed expectations 