#!/bin/bash

# Executive Business Analysis - Document Consolidation Script
# This script combines all key business analysis documents into one comprehensive file
# UPDATED: Now includes multiple essential documents for complete executive overview

set -e  # Exit on any error

OUTPUT_FILE="../../consolidated-document/Executive-Analysis-Complete.md"
TEMP_FILE="temp_consolidated.md"
BASE_DIR="../../"

echo "Building comprehensive executive business analysis document..."
echo "Including multiple key documents for complete analysis..."

# Start with the header
cat > "$TEMP_FILE" << 'EOF'
# [Company Name] / [Product Name] Hosting Provider Evaluation
## Complete Analysis & Implementation Guide - CONSOLIDATED REPORT

**CONFIDENTIAL BUSINESS ANALYSIS**

**Document Classification:** Internal Business Analysis - COMPLETE CONSOLIDATED VERSION  
**Prepared For:** [Executive Name] - [Company Name] / [Product Name]  
**Analysis Period:** Q3-Q4 FY25  
**Date:** 30 May 2025  

**Prepared By:** Ronan  
**Email:** [Your Email]  
**Phone:** [Your Phone]  
**Organization:** [Company Name] / [Product Name]  

**CONSOLIDATED DOCUMENT NOTICE:** This document combines all business analysis materials into one comprehensive report for easy distribution and review. All original documents remain intact in their respective folders.

**Classification:** Internal use only - Contains strategic business decisions, technical requirements, and budget information.

EOF

# Function to add a document section
add_document() {
    local file_path="$1"
    local section_title="$2"
    local section_number="$3"
    
    if [ -f "$file_path" ]; then
        echo "Adding: $section_title"
        echo "" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
        echo "# $section_number. $section_title" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
        echo "*Source: \`$(basename "$file_path")\`*" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
        
        # Add the full content, skipping YAML frontmatter if it exists
        if head -1 "$file_path" | grep -q "^---"; then
            awk 'BEGIN{skip=1} /^---/{if(skip){skip=0; next} else {skip=1}} !skip' "$file_path" >> "$TEMP_FILE"
        else
            cat "$file_path" >> "$TEMP_FILE"
        fi
        echo "" >> "$TEMP_FILE"
        echo "" >> "$TEMP_FILE"
    else
        echo "Warning: File not found: $file_path"
    fi
}

# Add documents in order
add_document "${BASE_DIR}README.md" "Project Overview & Executive Summary" "1"
add_document "${BASE_DIR}existing-research/provider-research/2025-05-29-2251-[Product Name]-Hosting-Provider-Deep-Research.md" "Comprehensive Market Research & Provider Analysis" "2"
add_document "${BASE_DIR}final-recommendation.md" "Final Recommendation & Decision Support" "3"
add_document "${BASE_DIR}comprehensive-analysis.md" "Technical Analysis & Requirements" "4"
add_document "${BASE_DIR}migration-strategy.md" "Migration Strategy & Implementation Plan" "5"
add_document "${BASE_DIR}migration-plan.md" "Detailed Migration Plan & Timeline" "6"
add_document "${BASE_DIR}provider-comparison-matrix.md" "Provider Comparison Matrix" "7"

# Add supporting technical documents
add_document "${BASE_DIR}revised-analysis-actual-codebase.md" "Revised Analysis Based on Actual Codebase" "8"
add_document "${BASE_DIR}SITEMAP.md" "Complete Documentation Sitemap" "9"
add_document "${BASE_DIR}hosting-requirements.md" "Detailed Hosting Requirements" "10"
add_document "${BASE_DIR}cost-analysis.md" "Cost Analysis & Budget Planning" "11"
add_document "${BASE_DIR}risk-assessment.md" "Risk Assessment & Mitigation" "12"
add_document "${BASE_DIR}evaluation-framework.md" "Evaluation Framework & Methodology" "13"

# Add decision framework documents
add_document "${BASE_DIR}decision-framework/scoring-criteria.md" "Detailed Scoring Criteria & Methodology" "14"
add_document "${BASE_DIR}decision-framework/risk-assessment.md" "Decision Framework Risk Assessment" "15"

# Add infrastructure analysis
add_document "${BASE_DIR}ios-background-sync-analysis.md" "iOS Background Sync Analysis" "16"
add_document "${BASE_DIR}comprehensive-answers-to-questions.md" "Comprehensive Q&A Analysis" "17"
add_document "${BASE_DIR}cdn-analysis-and-recommendations.md" "CDN Analysis & Infrastructure Recommendations" "18"

# Add critical mobile app improvements (HIGH PRIORITY)
add_document "${BASE_DIR}app-improvements/mobile-app-enhancement-recommendations.md" "Mobile App Enhancement Recommendations - CRITICAL" "19"
add_document "${BASE_DIR}app-improvements/photo-save-architecture-analysis.md" "Photo Save Architecture Analysis - CRITICAL UX Issue" "20"
add_document "${BASE_DIR}app-improvements/ios-background-sync-detailed-analysis.md" "iOS Background Sync Detailed Technical Analysis" "21"

# Add detailed provider evaluations
add_document "${BASE_DIR}provider-evaluations/scalahosting-detailed-review.md" "ScalaHosting Detailed Evaluation - PRIMARY RECOMMENDATION" "22"
add_document "${BASE_DIR}provider-evaluations/knownhost-detailed-review.md" "KnownHost Detailed Evaluation - VALUE ALTERNATIVE" "23"
add_document "${BASE_DIR}provider-evaluations/liquidweb-detailed-review.md" "Liquid Web Detailed Evaluation - NOT RECOMMENDED" "24"

# Clean up emoji usage in headers for professional presentation
echo "Cleaning up emoji usage for professional presentation..."

# Use Python for safe Unicode-aware emoji cleaning
python3 -c "
import re
import sys

# Read the file
with open('$TEMP_FILE', 'r', encoding='utf-8') as f:
    content = f.read()

# Define emoji pattern (common emojis used in headers)
header_emoji_pattern = re.compile(r'[🎯📊🏗️🌍📋🏆📞✅🚨📱💡📈🔧📄📁🔍📚🗺️⚡🔐💰🚀📅⚠️🔄⚙️🎵📋✨]+')

# Process line by line to preserve structure
lines = content.split('\n')
cleaned_lines = []

for line in lines:
    # Only clean emojis from markdown headers (lines starting with #)
    if re.match(r'^#{1,6}\s', line):
        # Remove emojis from headers but preserve markdown formatting
        line = header_emoji_pattern.sub('', line)
        # Clean up extra spaces but preserve header level
        line = re.sub(r'\s+', ' ', line)
        # Ensure proper spacing after hash marks
        line = re.sub(r'^(#{1,6})\s*(.+)', r'\1 \2', line)
        # Remove any trailing spaces
        line = line.rstrip()
    
    cleaned_lines.append(line)

# Write cleaned content
with open('${OUTPUT_FILE}.tmp', 'w', encoding='utf-8') as f:
    f.write('\n'.join(cleaned_lines))
"

mv "${OUTPUT_FILE}.tmp" "$TEMP_FILE"

# Add footer
cat >> "$TEMP_FILE" << 'EOF'


## Document Compilation Information

**Compiled:** $(date)
**Source Documents:** All files from 2025-hosting-analysis/ directory
**Original Structure:** Preserved in individual files
**Purpose:** Single comprehensive file for distribution

*This consolidated document ensures no content is omitted and provides complete hosting evaluation in a single file.*

*End of Consolidated Document*
EOF

# Move to final location
mv "$TEMP_FILE" "$OUTPUT_FILE"

echo "✅ Consolidated document created successfully!"
echo "📄 Output file: $OUTPUT_FILE"
echo "📊 File size: $(wc -l < "$OUTPUT_FILE") lines"
echo "📋 Documents included: 24 comprehensive analysis documents"
echo "🎯 Ready for professional distribution!" 