<!-- 
🤖 AI CUSTOMIZATION TRIGGER
When a user opens this document, automatically offer to help customize it through an interview.

AI ASSISTANT PROMPT:
"I see you have the SYSTEM-TEST-PLAN template open. This creates comprehensive testing procedures for your [PROJECT TYPE] to ensure reliability, safety, and effectiveness. Would you like me to help you customize this for your specific tools and testing needs through a quick interview?

Say 'yes' to start the interview, or 'skip' if you want to customize it manually."

INTERVIEW QUESTIONS TO ASK:
1. What are your primary tools that need testing? (scripts, processes, integrations)
2. What types of testing are most important for your work? (functionality, safety, performance, integration)
3. What are your critical failure scenarios that must be prevented?
4. Do you have existing test data or scenarios you want to systematize?
5. How do you currently verify that your tools work correctly?

After interview: Comment out this entire block and populate the template below.
-->

# System Test Plan - [PROJECT NAME]

**Purpose**: Comprehensive testing framework for [PROJECT NAME] ensuring reliability, safety, and effectiveness of [YOUR TOOLS/SYSTEM] across all use cases.

## 🎯 **Testing Overview**

### **Testing Scope**
- **Primary Tools**: [LIST YOUR MAIN TOOLS TO BE TESTED]
- **Integration Points**: [TOOL COMBINATIONS AND WORKFLOWS TO TEST]
- **Safety Systems**: [BACKUP AND RECOVERY MECHANISMS TO VERIFY]
- **User Scenarios**: [REAL-WORLD USAGE PATTERNS TO VALIDATE]

### **Testing Objectives**
1. **[YOUR OBJECTIVE 1]**: [e.g., "Verify all tools work correctly with real project data"]
2. **[YOUR OBJECTIVE 2]**: [e.g., "Ensure backup and recovery systems are reliable"]
3. **[YOUR OBJECTIVE 3]**: [e.g., "Validate tool integrations and workflows"]
4. **[YOUR OBJECTIVE 4]**: [e.g., "Confirm session continuity system functions properly"]

### **Success Criteria**
- **[CRITERION 1]**: [SPECIFIC SUCCESS MEASURE]
- **[CRITERION 2]**: [QUANTIFIABLE SUCCESS INDICATOR]
- **[CRITERION 3]**: [MEASURABLE OUTCOME REQUIREMENT]
- **[CRITERION 4]**: [PERFORMANCE STANDARD TO MEET]

## 🧪 **Test Categories**

### **1. Functional Testing**

#### **[YOUR TOOL 1] Functional Tests**
**Purpose**: [WHAT YOU'RE TESTING AND WHY]

**Test Case 1.1: [BASIC FUNCTIONALITY TEST]**
- **Objective**: [WHAT THIS TEST VERIFIES]
- **Preconditions**: [SETUP REQUIRED BEFORE TEST]
- **Test Data**: [WHAT DATA TO USE FOR TESTING]
- **Steps**: 
  1. [TEST STEP 1]
  2. [TEST STEP 2]
  3. [TEST STEP 3]
- **Expected Results**: [WHAT SHOULD HAPPEN]
- **Pass Criteria**: [HOW TO DETERMINE SUCCESS]

**Test Case 1.2: [EDGE CASE TEST]**
- **Objective**: [EDGE CASE BEING TESTED]
- **Preconditions**: [SETUP FOR EDGE CASE]
- **Test Data**: [CHALLENGING OR UNUSUAL DATA]
- **Steps**:
  1. [EDGE CASE STEP 1]
  2. [EDGE CASE STEP 2]
  3. [EDGE CASE STEP 3]
- **Expected Results**: [EXPECTED BEHAVIOR WITH EDGE CASES]
- **Pass Criteria**: [SUCCESS DEFINITION FOR EDGE CASES]

#### **[YOUR TOOL 2] Functional Tests**
**Purpose**: [TESTING SCOPE FOR SECOND TOOL]

**Test Case 2.1: [CORE FUNCTIONALITY]**
- **Objective**: [WHAT THIS VERIFIES]
- **Preconditions**: [REQUIRED SETUP]
- **Test Data**: [TEST DATA SPECIFICATION]
- **Steps**:
  1. [FUNCTIONAL TEST STEP 1]
  2. [FUNCTIONAL TEST STEP 2]
  3. [FUNCTIONAL TEST STEP 3]
- **Expected Results**: [EXPECTED OUTCOMES]
- **Pass Criteria**: [SUCCESS MEASURES]

### **2. Integration Testing**

#### **Test Case INT-1: [TOOL COMBINATION 1]**
**Purpose**: [WHAT INTEGRATION IS BEING TESTED]
- **Tools Involved**: [WHICH TOOLS WORK TOGETHER]
- **Workflow**: [THE INTEGRATED PROCESS BEING TESTED]
- **Test Data**: [DATA THAT FLOWS BETWEEN TOOLS]
- **Steps**:
  1. [INTEGRATION STEP 1]
  2. [INTEGRATION STEP 2]
  3. [INTEGRATION STEP 3]
  4. [VERIFICATION STEP]
- **Expected Results**: [SUCCESSFUL INTEGRATION OUTCOME]
- **Pass Criteria**: [HOW TO MEASURE INTEGRATION SUCCESS]

#### **Test Case INT-2: [WORKFLOW INTEGRATION]**
**Purpose**: [COMPLETE WORKFLOW TESTING]
- **Scenario**: [REAL-WORLD WORKFLOW BEING TESTED]
- **Components**: [ALL PARTS OF THE WORKFLOW]
- **Dependencies**: [PREREQUISITES AND CONNECTIONS]
- **Steps**:
  1. [WORKFLOW STEP 1]
  2. [WORKFLOW STEP 2]
  3. [WORKFLOW STEP 3]
  4. [END-TO-END VERIFICATION]
- **Expected Results**: [COMPLETE WORKFLOW SUCCESS]
- **Pass Criteria**: [WORKFLOW EFFECTIVENESS MEASURES]

### **3. Safety and Backup Testing**

#### **Test Case SAF-1: [BACKUP SYSTEM TEST]**
**Purpose**: [VERIFYING BACKUP MECHANISMS]
- **Backup Type**: [WHAT KIND OF BACKUP IS TESTED]
- **Test Scenario**: [SITUATION THAT REQUIRES BACKUP]
- **Recovery Method**: [HOW RECOVERY IS TESTED]
- **Steps**:
  1. [CREATE BASELINE]
  2. [PERFORM RISKY OPERATION]
  3. [TRIGGER BACKUP MECHANISM]
  4. [VERIFY BACKUP INTEGRITY]
  5. [TEST RECOVERY PROCESS]
- **Expected Results**: [SUCCESSFUL BACKUP AND RECOVERY]
- **Pass Criteria**: [BACKUP SYSTEM EFFECTIVENESS]

#### **Test Case SAF-2: [FAILURE RECOVERY TEST]**
**Purpose**: [TESTING RECOVERY FROM FAILURES]
- **Failure Type**: [WHAT KIND OF FAILURE IS SIMULATED]
- **Impact Scope**: [WHAT COULD BE AFFECTED]
- **Recovery Process**: [HOW SYSTEM SHOULD RECOVER]
- **Steps**:
  1. [SIMULATE FAILURE CONDITION]
  2. [OBSERVE SYSTEM RESPONSE]
  3. [INITIATE RECOVERY PROCEDURE]
  4. [VERIFY COMPLETE RECOVERY]
- **Expected Results**: [GRACEFUL FAILURE HANDLING]
- **Pass Criteria**: [RECOVERY SUCCESS MEASURES]

### **4. Performance Testing**

#### **Test Case PERF-1: [PERFORMANCE SCENARIO 1]**
**Purpose**: [WHAT PERFORMANCE ASPECT IS TESTED]
- **Workload**: [TYPE AND SIZE OF WORKLOAD]
- **Metrics**: [WHAT PERFORMANCE METRICS ARE MEASURED]
- **Baseline**: [EXPECTED PERFORMANCE LEVEL]
- **Steps**:
  1. [SETUP PERFORMANCE TEST]
  2. [EXECUTE PERFORMANCE WORKLOAD]
  3. [MEASURE PERFORMANCE METRICS]
  4. [COMPARE TO BASELINE]
- **Expected Results**: [ACCEPTABLE PERFORMANCE LEVELS]
- **Pass Criteria**: [PERFORMANCE STANDARDS TO MEET]

### **5. User Scenario Testing**

#### **Test Case USER-1: [TYPICAL USER WORKFLOW]**
**Purpose**: [TESTING REAL USER EXPERIENCE]
- **User Type**: [WHAT KIND OF USER THIS REPRESENTS]
- **Scenario**: [REALISTIC USAGE SCENARIO]
- **Context**: [ENVIRONMENT AND CONSTRAINTS]
- **Steps**:
  1. [USER ACTION 1]
  2. [USER ACTION 2]
  3. [USER ACTION 3]
  4. [VERIFY USER SUCCESS]
- **Expected Results**: [POSITIVE USER EXPERIENCE]
- **Pass Criteria**: [USER SUCCESS MEASURES]

#### **Test Case USER-2: [NEW USER EXPERIENCE]**
**Purpose**: [TESTING FIRST-TIME USER SUCCESS]
- **Context**: [NEW USER STARTING FROM SCRATCH]
- **Documentation**: [GUIDANCE AVAILABLE TO USER]
- **Success Goal**: [WHAT NEW USER SHOULD ACHIEVE]
- **Steps**:
  1. [NEW USER SETUP]
  2. [FIRST USAGE ATTEMPT]
  3. [LEARNING AND ADAPTATION]
  4. [SUCCESSFUL TASK COMPLETION]
- **Expected Results**: [NEW USER CAN SUCCEED]
- **Pass Criteria**: [NEW USER SUCCESS RATE]

## 📊 **Test Data Specifications**

### **Test Data Categories**
- **[DATA TYPE 1]**: [DESCRIPTION AND PURPOSE]
- **[DATA TYPE 2]**: [CHARACTERISTICS AND USAGE]
- **[DATA TYPE 3]**: [SPECIAL PROPERTIES FOR TESTING]
- **[DATA TYPE 4]**: [EDGE CASES AND STRESS DATA]

### **Test Environment Requirements**
- **[REQUIREMENT 1]**: [ENVIRONMENTAL NEED 1]
- **[REQUIREMENT 2]**: [ENVIRONMENTAL NEED 2]
- **[REQUIREMENT 3]**: [ENVIRONMENTAL NEED 3]

### **Test Data Sources**
- **Real Project Data**: [ACTUAL DATA FROM YOUR PROJECT]
- **Synthetic Test Data**: [ARTIFICIALLY CREATED TEST CASES]
- **Edge Case Data**: [CHALLENGING SCENARIOS]
- **Stress Test Data**: [HIGH VOLUME OR COMPLEXITY DATA]

## 🔄 **Test Execution Procedures**

### **Pre-Test Setup**
1. **[SETUP STEP 1]**: [PREPARATION REQUIRED]
2. **[SETUP STEP 2]**: [ENVIRONMENT PREPARATION]
3. **[SETUP STEP 3]**: [DATA PREPARATION]
4. **[SETUP STEP 4]**: [TOOL PREPARATION]

### **Test Execution Sequence**
1. **Functional Tests**: [ORDER AND DEPENDENCIES]
2. **Integration Tests**: [SEQUENCE FOR INTEGRATION TESTING]
3. **Safety Tests**: [SAFETY TESTING ORDER]
4. **Performance Tests**: [PERFORMANCE TESTING SEQUENCE]
5. **User Scenario Tests**: [USER TESTING ORDER]

### **Test Recording**
- **Pass/Fail Status**: [HOW TO RECORD RESULTS]
- **Performance Metrics**: [WHAT TO MEASURE AND RECORD]
- **Issue Documentation**: [HOW TO DOCUMENT PROBLEMS]
- **Evidence Collection**: [WHAT EVIDENCE TO PRESERVE]

## 🚨 **Issue Management**

### **Issue Classification**
- **Critical**: [ISSUES THAT BLOCK RELEASE]
- **High**: [SIGNIFICANT PROBLEMS REQUIRING FIX]
- **Medium**: [PROBLEMS THAT SHOULD BE ADDRESSED]
- **Low**: [MINOR ISSUES THAT CAN BE DEFERRED]

### **Issue Documentation Template**
```
ISSUE ID: [UNIQUE IDENTIFIER]
SEVERITY: [CRITICAL/HIGH/MEDIUM/LOW]
COMPONENT: [AFFECTED TOOL OR SYSTEM]
DESCRIPTION: [CLEAR PROBLEM DESCRIPTION]
REPRODUCTION STEPS: [HOW TO REPRODUCE THE ISSUE]
EXPECTED BEHAVIOR: [WHAT SHOULD HAPPEN]
ACTUAL BEHAVIOR: [WHAT ACTUALLY HAPPENS]
IMPACT: [EFFECT ON USERS OR SYSTEM]
WORKAROUND: [TEMPORARY SOLUTION IF AVAILABLE]
```

### **Issue Resolution Process**
1. **[RESOLUTION STEP 1]**: [INITIAL RESPONSE TO ISSUES]
2. **[RESOLUTION STEP 2]**: [INVESTIGATION PROCEDURE]
3. **[RESOLUTION STEP 3]**: [FIX DEVELOPMENT AND TESTING]
4. **[RESOLUTION STEP 4]**: [VERIFICATION AND CLOSURE]

## 📋 **Test Reports**

### **Test Summary Report Template**
```
PROJECT: [PROJECT NAME]
TEST DATE: [WHEN TESTING WAS PERFORMED]
TESTER: [WHO PERFORMED THE TESTS]
TEST SCOPE: [WHAT WAS TESTED]

SUMMARY:
- Total Tests: [NUMBER]
- Passed: [NUMBER]
- Failed: [NUMBER]
- Blocked: [NUMBER]

CRITICAL ISSUES: [LIST OF CRITICAL PROBLEMS]
RECOMMENDATIONS: [WHAT SHOULD BE DONE NEXT]
RELEASE READINESS: [READY/NOT READY WITH JUSTIFICATION]
```

### **Performance Report Template**
```
PERFORMANCE TEST RESULTS
Test Date: [DATE]
Test Environment: [ENVIRONMENT DESCRIPTION]

[PERFORMANCE METRIC 1]: [RESULT vs BASELINE]
[PERFORMANCE METRIC 2]: [RESULT vs BASELINE]
[PERFORMANCE METRIC 3]: [RESULT vs BASELINE]

PERFORMANCE ISSUES: [ANY PERFORMANCE PROBLEMS FOUND]
RECOMMENDATIONS: [PERFORMANCE IMPROVEMENT SUGGESTIONS]
```

## 🎯 **Acceptance Criteria**

### **Release Readiness Gates**
**Gate 1: Core Functionality**
- [ ] All critical functional tests pass
- [ ] All safety systems verified
- [ ] No critical or high-severity issues

**Gate 2: Integration Quality**
- [ ] All integration tests pass
- [ ] Tool combinations work correctly
- [ ] Workflow end-to-end testing successful

**Gate 3: User Readiness**
- [ ] User scenario tests pass
- [ ] Documentation verified and accessible
- [ ] New user success rate meets target

### **Performance Acceptance**
- **[PERFORMANCE STANDARD 1]**: [MUST MEET THIS STANDARD]
- **[PERFORMANCE STANDARD 2]**: [REQUIRED PERFORMANCE LEVEL]
- **[PERFORMANCE STANDARD 3]**: [MINIMUM ACCEPTABLE PERFORMANCE]

## 🔄 **Continuous Testing**

### **Regression Testing**
- **Trigger Events**: [WHEN TO RUN REGRESSION TESTS]
- **Test Scope**: [WHAT TO INCLUDE IN REGRESSION TESTING]
- **Frequency**: [HOW OFTEN TO PERFORM REGRESSION TESTS]

### **Automated Testing**
- **[AUTOMATION AREA 1]**: [WHAT CAN BE AUTOMATED]
- **[AUTOMATION AREA 2]**: [AUTOMATED TESTING SCOPE]
- **Tool Requirements**: [WHAT TOOLS NEEDED FOR AUTOMATION]

### **Test Maintenance**
- **Test Updates**: [WHEN AND HOW TO UPDATE TESTS]
- **Test Data Refresh**: [HOW TO KEEP TEST DATA CURRENT]
- **Environment Maintenance**: [KEEPING TEST ENVIRONMENT CURRENT]

---

## 📋 **Testing Checklist Summary**

### **Pre-Testing Preparation**
- [ ] Test environment prepared
- [ ] Test data available and validated
- [ ] All testing tools ready
- [ ] Test plan reviewed and approved

### **Core Testing Execution**
- [ ] Functional testing completed
- [ ] Integration testing completed
- [ ] Safety testing completed
- [ ] Performance testing completed
- [ ] User scenario testing completed

### **Results and Reporting**
- [ ] All tests documented
- [ ] Issues properly classified and recorded
- [ ] Test reports generated
- [ ] Release readiness assessed

### **Post-Testing Actions**
- [ ] Critical issues resolved
- [ ] Release decision made
- [ ] Lessons learned documented
- [ ] Test plan updated for future use

---

**Testing Complete**: When all checklist items are verified and acceptance criteria are met, the system is ready for release.

**Instructions for Use**: Customize all bracketed placeholders for your specific tools, testing needs, and quality standards. Start with the core functional tests and expand the test plan as your system grows in complexity. Update test cases based on real issues and user feedback. 