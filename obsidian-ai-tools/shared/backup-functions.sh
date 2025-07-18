#!/bin/bash
# Shared Backup Functions for Professional Markdown Toolkit
# Source this file in other scripts: source "$(dirname "$0")/../shared/backup-functions.sh"

# Global backup configuration
BACKUP_ENABLED=true
BACKUP_BASE_DIR=""

# Initialize backup system
init_backup_system() {
    local script_dir="$1"
    BACKUP_BASE_DIR="$(dirname "$script_dir")/backups/$(date +%Y%m%d_%H%M%S)"
    
    if [ "$BACKUP_ENABLED" = true ]; then
        mkdir -p "$BACKUP_BASE_DIR"
        echo "📁 Backup directory created: $BACKUP_BASE_DIR"
    fi
}

# Create backup of a single file
create_backup() {
    local file="$1"
    local backup_subdir="${2:-general}"
    
    if [ "$BACKUP_ENABLED" != true ]; then
        return 0
    fi
    
    if [ ! -f "$file" ]; then
        echo "⚠️  Warning: Cannot backup non-existent file: $file"
        return 1
    fi
    
    local backup_dir="$BACKUP_BASE_DIR/$backup_subdir"
    mkdir -p "$backup_dir"
    
    local filename=$(basename "$file")
    local backup_path="$backup_dir/$filename"
    
    # If backup already exists, append a number
    local counter=1
    while [ -f "$backup_path" ]; do
        local name_without_ext="${filename%.*}"
        local ext="${filename##*.}"
        if [ "$name_without_ext" = "$ext" ]; then
            # No extension
            backup_path="$backup_dir/${filename}_${counter}"
        else
            backup_path="$backup_dir/${name_without_ext}_${counter}.${ext}"
        fi
        counter=$((counter + 1))
    done
    
    cp "$file" "$backup_path"
    echo "💾 Backup created: $backup_path"
    return 0
}

# Create backup of all files in a directory matching a pattern
create_directory_backup() {
    local source_dir="$1"
    local pattern="${2:-*.md}"
    local backup_subdir="${3:-batch_operation}"
    
    if [ "$BACKUP_ENABLED" != true ]; then
        return 0
    fi
    
    local backup_dir="$BACKUP_BASE_DIR/$backup_subdir"
    mkdir -p "$backup_dir"
    
    local file_count=0
    for file in "$source_dir"/$pattern; do
        if [ -f "$file" ]; then
            local filename=$(basename "$file")
            cp "$file" "$backup_dir/$filename"
            file_count=$((file_count + 1))
        fi
    done
    
    echo "💾 Batch backup created: $file_count files in $backup_dir"
    return 0
}

# Disable backups (for advanced users or testing)
disable_backups() {
    BACKUP_ENABLED=false
    echo "⚠️  Backups disabled - proceeding without backup creation"
}

# Enable backups (default state)
enable_backups() {
    BACKUP_ENABLED=true
    echo "✅ Backups enabled"
}

# Get backup information
get_backup_info() {
    if [ "$BACKUP_ENABLED" = true ]; then
        echo "Backup directory: $BACKUP_BASE_DIR"
        if [ -d "$BACKUP_BASE_DIR" ]; then
            echo "Backup size: $(du -sh "$BACKUP_BASE_DIR" 2>/dev/null | cut -f1 || echo 'Unknown')"
            echo "Files backed up: $(find "$BACKUP_BASE_DIR" -type f 2>/dev/null | wc -l || echo 'Unknown')"
        fi
    else
        echo "Backups are currently disabled"
    fi
}

# Clean up old backups (keep last N days)
cleanup_old_backups() {
    local days_to_keep="${1:-7}"
    local script_dir="$2"
    
    # Validate inputs
    if [ -z "$script_dir" ]; then
        echo "❌ Error: Script directory not provided"
        return 1
    fi
    
    if ! [[ "$days_to_keep" =~ ^[0-9]+$ ]] || [ "$days_to_keep" -lt 1 ]; then
        echo "❌ Error: Days to keep must be a positive number (got: $days_to_keep)"
        return 1
    fi
    
    local backup_root="$(dirname "$script_dir")/backups"
    
    # Validate backup root path
    if [ -z "$backup_root" ] || [ "$backup_root" = "/" ] || [ "$backup_root" = "/backups" ]; then
        echo "❌ Error: Invalid backup root path: $backup_root"
        return 1
    fi
    
    if [ ! -d "$backup_root" ]; then
        echo "No backup directory found at $backup_root"
        return 0
    fi
    
    echo "🧹 Cleaning up backups older than $days_to_keep days from: $backup_root"
    
    # Find directories to remove (safer approach)
    local dirs_to_remove
    dirs_to_remove=$(find "$backup_root" -maxdepth 1 -type d -name "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]" -mtime +$days_to_keep 2>/dev/null)
    
    if [ -z "$dirs_to_remove" ]; then
        echo "📊 No old backup directories found to clean up"
        return 0
    fi
    
    local count=0
    while IFS= read -r dir; do
        if [ -n "$dir" ] && [ -d "$dir" ]; then
            echo "🗑️  Removing old backup: $(basename "$dir")"
            rm -rf "$dir"
            count=$((count + 1))
        fi
    done <<< "$dirs_to_remove"
    
    local remaining=$(find "$backup_root" -maxdepth 1 -type d -name "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9][0-9][0-9]" 2>/dev/null | wc -l)
    echo "📊 Cleaned up $count old backup sets, $remaining remaining"
}

# Restore from backup (interactive)
restore_from_backup() {
    local script_dir="$1"
    local backup_root="$(dirname "$script_dir")/backups"
    
    if [ ! -d "$backup_root" ]; then
        echo "❌ No backup directory found at $backup_root"
        return 1
    fi
    
    echo "Available backup sets:"
    local backup_dirs=($(find "$backup_root" -type d -name "*_*" | sort -r))
    
    if [ ${#backup_dirs[@]} -eq 0 ]; then
        echo "❌ No backup sets found"
        return 1
    fi
    
    for i in "${!backup_dirs[@]}"; do
        local dir="${backup_dirs[$i]}"
        local timestamp=$(basename "$dir")
        local file_count=$(find "$dir" -type f 2>/dev/null | wc -l)
        echo "  $((i+1)): $timestamp ($file_count files)"
    done
    
    echo "Enter the number of the backup set to restore from (or 0 to cancel):"
    read -r choice
    
    if [ "$choice" -eq 0 ] 2>/dev/null; then
        echo "❌ Restore cancelled"
        return 0
    fi
    
    if [ "$choice" -lt 1 ] || [ "$choice" -gt ${#backup_dirs[@]} ] 2>/dev/null; then
        echo "❌ Invalid selection"
        return 1
    fi
    
    local selected_backup="${backup_dirs[$((choice-1))]}"
    echo "⚠️  This will restore files from: $selected_backup"
    echo "⚠️  This may overwrite current files. Continue? (y/N)"
    read -r confirm
    
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "❌ Restore cancelled"
        return 0
    fi
    
    # Perform restore
    local restored_count=0
    find "$selected_backup" -type f -name "*.md" | while read -r backup_file; do
        local filename=$(basename "$backup_file")
        local restore_path="$PWD/$filename"
        cp "$backup_file" "$restore_path"
        restored_count=$((restored_count + 1))
        echo "✅ Restored: $filename"
    done
    
    echo "🎉 Restore complete!"
}

# Show this help
show_backup_help() {
    cat << 'EOF'
Backup Functions Help
=====================

Available Functions:
  init_backup_system <script_dir>     - Initialize backup system
  create_backup <file> [subdir]       - Backup single file
  create_directory_backup <dir> [pattern] [subdir] - Backup multiple files
  disable_backups                     - Disable backup creation
  enable_backups                      - Enable backup creation (default)
  get_backup_info                     - Show backup status
  cleanup_old_backups [days] <script_dir> - Remove old backups
  restore_from_backup <script_dir>    - Interactive restore

Usage in scripts:
  source "$(dirname "$0")/../shared/backup-functions.sh"
  init_backup_system "$SCRIPT_DIR"
  create_backup "somefile.md" "metadata_operations"

Command line options to add to your scripts:
  --no-backup     - Disable backups for this run
  --backup-only   - Create backups but don't modify files

EOF
} 