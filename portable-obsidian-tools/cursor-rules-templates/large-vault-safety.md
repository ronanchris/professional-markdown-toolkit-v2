# Large Vault Safety Protocol

**Rule Type**: ALWAYS  
**Purpose**: Prevent disasters in vaults with 1000+ pages

## Scope Confirmation Protocol
- Always ask "How many files should this affect?" before bulk operations
- Never assume vault-wide changes unless explicitly requested
- Confirm file count before proceeding with batch operations
- Offer to limit scope to specific folders when appropriate

## Testing Requirements
- ALWAYS offer `--dry-run` mode first for any bulk operation
- Suggest testing on 5-10 files before applying to entire vault
- Show example of what changes will look like before applying
- Require explicit confirmation for operations affecting 50+ files

## Batch Processing Guidelines
- Suggest processing in chunks of 50-100 files for large operations
- Offer to pause between batches for user review
- Provide progress updates during long operations
- Allow user to cancel and resume operations

## Backup Protocol
- Explain backup system before ANY destructive operation
- Specify backup location: `portable-obsidian-tools/backups/YYYYMMDD_HHMMSS/`
- Provide restore instructions after operations complete
- Never proceed with destructive operations without mentioning backups

## Risk Assessment
- **LOW RISK**: Single file edits, reading operations
- **MEDIUM RISK**: Template applications, format cleanup (5-50 files)
- **HIGH RISK**: YAML removal, bulk find/replace (50+ files)
- **CRITICAL RISK**: Vault-wide operations, link structure changes

## Error Recovery
- Provide clear rollback instructions if something goes wrong
- Maintain operation logs for troubleshooting
- Offer to help restore from backups if needed
- Document any issues for future prevention

## Enforcement
- Apply to ALL bulk operations (10+ files)
- Apply to ALL destructive operations (metadata removal, etc.)
- Apply to ALL cross-file operations (link updates, etc.)
- Cannot be overridden - safety is non-negotiable 