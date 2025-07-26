# Session Continuity System - Human Test Plan
*Complete end-to-end validation protocol for real-world usage*

## 🎯 **Test Overview**
This test plan validates that the session continuity system works correctly from a user's perspective across multiple sessions and scenarios.

**Estimated Time**: 45-60 minutes  
**Prerequisites**: Fresh cursor session, Professional Markdown Toolkit project open

---

## 📋 **Test Scenario 1: Brand New Project (No Plan Exists)**

### **Setup:**
1. Delete or rename `session-continuity/02-SESSION-PLAN.md` (backup first)
2. Start fresh Cursor session
3. Open Professional Markdown Toolkit project

### **Expected Behavior:**
- [ ] AI should automatically detect missing 02-SESSION-PLAN.md
- [ ] AI should offer to create plan via interview process
- [ ] AI should ask about project goals and approach
- [ ] AI should validate current date with user
- [ ] AI should create 02-SESSION-PLAN.md with 4-6 focused items

### **Test Actions:**
1. **Say**: "Let's start working on the project"
2. **Observe**: Does AI check for 02-SESSION-PLAN.md?
3. **Respond**: Accept plan creation offer
4. **Validate**: Does AI ask for current date confirmation?
5. **Check**: Is 02-SESSION-PLAN.md created with proper structure?

### **Success Criteria:**
- [ ] Automatic plan detection works
- [ ] Date validation occurs
- [ ] 02-SESSION-PLAN.md follows template structure
- [ ] Session lens approach applied (4-6 items max)

---

## 📋 **Test Scenario 2: Existing Project (Plan Exists)**

### **Setup:**
1. Ensure `session-continuity/02-SESSION-PLAN.md` exists with checkboxes
2. Start fresh Cursor session
3. Open project

### **Expected Behavior:**
- [ ] AI should automatically load existing 02-SESSION-PLAN.md
- [ ] AI should focus on current phase items (session lens)
- [ ] AI should summarize current status
- [ ] AI should ask about session goals

### **Test Actions:**
1. **Say**: "I'm ready to continue working"
2. **Observe**: Does AI load and summarize current plan?
3. **Check**: Does AI focus on 4-6 current items only?
4. **Validate**: Does AI understand current progress?

### **Success Criteria:**
- [ ] Automatic plan loading works
- [ ] Session lens focus applied
- [ ] Current status accurately summarized
- [ ] Ready to continue from where left off

---

## 📋 **Test Scenario 3: Auto-Checkbox Completion Detection**

### **Setup:**
1. Have 02-SESSION-PLAN.md with unchecked items
2. Work on completing actual tasks

### **Test Actions & Expected Responses:**

#### **Test 3A: Direct Completion Phrases**
1. **Say**: "That's complete" (after finishing a task)
   - [ ] **Expected**: AI checks off related item in 02-SESSION-PLAN.md
   
2. **Say**: "We've finished the cursor rules integration"
   - [ ] **Expected**: AI checks off cursor rules item
   
3. **Say**: "Done with the template creation"
   - [ ] **Expected**: AI checks off template-related item

#### **Test 3B: Indirect Completion Indicators**
1. **Say**: "Successfully implemented the auto-checkbox system"
   - [ ] **Expected**: AI checks off implementation item
   
2. **Say**: "Task accomplished - the README is updated"
   - [ ] **Expected**: AI checks off README-related item

#### **Test 3C: Session Lens Scope Validation**
1. **Say**: "That's complete" (referring to item NOT in current 4-6 focus)
   - [ ] **Expected**: AI should NOT check off out-of-scope items
   - [ ] **Expected**: AI should only act on current session focus

### **Success Criteria:**
- [ ] Completion phrases trigger checkbox updates
- [ ] Only items in session lens scope are affected
- [ ] 02-SESSION-PLAN.md file is actually updated
- [ ] Updates happen automatically without manual intervention

---

## 📋 **Test Scenario 4: Deviation Detection & Documentation**

### **Setup:**
1. Have established plan and approach
2. Prepare to change direction mid-session

### **Test Actions & Expected Responses:**

#### **Test 4A: Deviation Trigger Phrases**
1. **Say**: "Actually, let's try a different approach to this"
   - [ ] **Expected**: AI detects deviation
   - [ ] **Expected**: AI validates current date with user
   - [ ] **Expected**: AI updates 02-SESSION-PLAN.md deviations section
   
2. **Say**: "Change of plan - I want to focus on testing first"
   - [ ] **Expected**: DEVIATION DETECTED response
   - [ ] **Expected**: Cascade updates to tracking documents
   
3. **Say**: "Better approach would be to automate this part"
   - [ ] **Expected**: Deviation documentation triggered

#### **Test 4B: Date Validation Protocol**
1. **Trigger deviation detection**
2. **Observe**: Does AI ask "What is today's date?" or similar
3. **Test**: Provide incorrect date
4. **Expected**: AI should use user-provided date, not assume

#### **Test 4C: Cascade Update Verification**
1. **After deviation detected**, check files:
   - [ ] 02-SESSION-PLAN.md has new entry in deviations section
   - [ ] 11-DEVIATION-TRACKING-PROTOCOL.md updated (if exists)
   - [ ] 03-CURRENT-STATE-SNAPSHOT.md updated (if major change)
   - [ ] All updates include verified timestamps

### **Success Criteria:**
- [ ] Deviation phrases trigger automatic detection
- [ ] Date validation prevents AI timestamp errors
- [ ] Multiple documents updated in cascade
- [ ] Timestamps are accurate across all files

---

## 📋 **Test Scenario 5: Session End & Archiving**

### **Setup:**
1. Complete significant work in session
2. Have updated 02-SESSION-PLAN.md with progress

### **Test Actions & Expected Responses:**

#### **Test 5A: Session End Triggers**
1. **Say**: "Let's wrap up for today"
   - [ ] **Expected**: AI recognizes session end indicator
   - [ ] **Expected**: AI offers to archive current session
   - [ ] **Expected**: AI proposes updating 03-CURRENT-STATE-SNAPSHOT.md
   
2. **Alternative**: "Session complete - good stopping point"
   - [ ] **Expected**: Same archiving behavior triggered

#### **Test 5B: Archiving Process**
1. **Accept archiving offer**
2. **Check results**:
   - [ ] 02-SESSION-PLAN.md copied to SESSION-PLAN-ARCHIVE/ with timestamp
   - [ ] 03-CURRENT-STATE-SNAPSHOT.md updated with session progress
   - [ ] All timestamps validated and accurate
   - [ ] Clean 02-SESSION-PLAN.md prepared for next session (or current one updated)

### **Success Criteria:**
- [ ] Session end phrases trigger archiving
- [ ] Files properly archived with timestamps
- [ ] Progress captured in snapshot documents
- [ ] System ready for next session

---

## 📋 **Test Scenario 6: Cross-Session Continuity**

### **Setup:**
1. Complete Test Scenario 5 (session end)
2. Close Cursor completely
3. Reopen project in fresh session

### **Test Actions:**
1. **Start new session**
2. **Say**: "Ready to continue where we left off"
3. **Observe**: Does AI automatically load previous context?
4. **Check**: Does AI reference archived session and current snapshot?

### **Expected Behavior:**
- [ ] AI loads 03-CURRENT-STATE-SNAPSHOT.md for context
- [ ] AI references previous session's archived plan
- [ ] AI offers to continue or create new plan
- [ ] AI maintains awareness of project history

### **Success Criteria:**
- [ ] Context preserved across sessions
- [ ] No loss of progress or learning
- [ ] Smooth continuation of work
- [ ] Historical context accessible

---

## 📋 **Test Scenario 7: Computational Efficiency Validation**

### **Setup:**
1. Monitor AI response times and context usage
2. Compare with and without session lens

### **Test Actions:**
1. **Work with session lens** (4-6 items focus)
   - Time AI responses
   - Note context awareness scope
   
2. **Simulate full monitoring** (mention many items)
   - Compare response times
   - Note computational load differences

### **Expected Results:**
- [ ] Session lens responses faster than full monitoring
- [ ] AI focuses on relevant 4-6 items only
- [ ] No loss of important context
- [ ] 67% efficiency gain observable in practice

---

## 📋 **Test Scenario 8: Error Recovery & Edge Cases**

### **Test Actions:**

#### **Test 8A: Corrupted 02-SESSION-PLAN.md**
1. **Manually corrupt** 02-SESSION-PLAN.md (invalid markdown)
2. **Start session**
3. **Expected**: AI detects corruption and offers to recreate

#### **Test 8B: Missing Date Validation**
1. **Trigger deviation detection**
2. **Don't provide date when asked**
3. **Expected**: AI should persist in getting date validation

#### **Test 8C: Conflicting Completion Phrases**
1. **Say**: "That's complete, but actually let's change the approach"
2. **Expected**: AI handles both completion and deviation triggers

### **Success Criteria:**
- [ ] System recovers gracefully from errors
- [ ] Date validation is enforced
- [ ] Conflicting triggers handled appropriately

---

## 🎯 **Final System Validation**

### **Overall Success Criteria:**
- [ ] All 8 test scenarios pass
- [ ] System works without manual intervention
- [ ] Context preserved across sessions
- [ ] Computational efficiency achieved
- [ ] No systematic errors or failures
- [ ] User experience is smooth and helpful

### **Performance Benchmarks:**
- [ ] Session start: < 30 seconds to load context
- [ ] Auto-checkbox: < 5 seconds to update
- [ ] Deviation detection: < 10 seconds to document
- [ ] Session end: < 60 seconds to archive
- [ ] Cross-session: < 45 seconds to restore context

---

## 📝 **Test Results Documentation**

**Date Tested**: [USER TO FILL IN]  
**Tester**: [USER TO FILL IN]  
**Cursor Version**: [USER TO FILL IN]  
**Project Version**: [USER TO FILL IN]  

### **Results Summary:**
- **Scenarios Passed**: ___/8
- **Critical Issues Found**: ___
- **Performance Issues**: ___
- **Usability Issues**: ___

### **Detailed Results:**
*(Fill in after testing each scenario)*

**Scenario 1 - Brand New Project**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 2 - Existing Project**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 3 - Auto-Checkbox**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 4 - Deviation Detection**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 5 - Session End**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 6 - Cross-Session**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 7 - Efficiency**: ✅ PASS / ❌ FAIL  
**Notes**: 

**Scenario 8 - Error Recovery**: ✅ PASS / ❌ FAIL  
**Notes**: 

---

## 🔧 **Troubleshooting Guide**

### **Common Issues & Solutions:**

**Issue**: AI doesn't detect 02-SESSION-PLAN.md automatically  
**Solution**: Check cursor rules are active, try saying "Let's check our session plan"

**Issue**: Auto-checkbox not working  
**Solution**: Ensure completion phrases are in current session lens scope (4-6 items)

**Issue**: Deviation detection not triggering  
**Solution**: Use exact phrases: "Actually, let's..." or "Change of plan..."

**Issue**: Date validation not working  
**Solution**: AI should ask for date - if not, manually provide current date

**Issue**: Session end archiving not working  
**Solution**: Use exact phrases: "Let's wrap up" or "Session complete"

---

*This test plan ensures the session continuity system works reliably in real-world usage scenarios.* 