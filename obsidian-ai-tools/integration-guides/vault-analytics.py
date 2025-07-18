#!/usr/bin/env python3
"""
Obsidian Vault Analytics Script
Analyzes vault structure, metadata, and provides optimization insights.
"""

import os
import re
import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

def check_dependencies():
    """Check if required dependencies are available."""
    missing = []
    try:
        import yaml
    except ImportError:
        missing.append("PyYAML (install with: pip install pyyaml)")
    
    if missing:
        print("Error: Missing required dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        print("\nTo install all dependencies:")
        print("  pip install -r requirements.txt")
        sys.exit(1)

# Check dependencies before importing
check_dependencies()
import yaml

class VaultAnalyzer:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)
        self.notes = []
        self.metadata = {}
        self.links = defaultdict(list)
        self.tags = Counter()
        self.stats = {}
        
    def analyze(self):
        """Run complete vault analysis."""
        print(f"Analyzing vault: {self.vault_path}")
        self._scan_notes()
        self._analyze_metadata()
        self._analyze_links()
        self._analyze_tags()
        self._generate_stats()
        return self.get_report()
    
    def _scan_notes(self):
        """Scan vault for markdown files."""
        markdown_files = list(self.vault_path.glob("**/*.md"))
        self.notes = [f for f in markdown_files if not f.name.startswith('.')]
        print(f"Found {len(self.notes)} markdown files")
    
    def _analyze_metadata(self):
        """Analyze YAML frontmatter in notes."""
        frontmatter_count = 0
        metadata_fields = Counter()
        
        for note_path in self.notes:
            try:
                with open(note_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        try:
                            frontmatter = yaml.safe_load(parts[1])
                            if frontmatter:
                                frontmatter_count += 1
                                self.metadata[str(note_path)] = frontmatter
                                for field in frontmatter.keys():
                                    metadata_fields[field] += 1
                        except yaml.YAMLError:
                            pass
            except Exception as e:
                print(f"Error reading {note_path}: {e}")
        
        self.stats['notes_with_frontmatter'] = frontmatter_count
        self.stats['metadata_fields'] = dict(metadata_fields)
    
    def _analyze_links(self):
        """Analyze WikiLinks and backlinks."""
        link_pattern = re.compile(r'\[\[([^\]]+)\]\]')
        
        for note_path in self.notes:
            try:
                with open(note_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find all WikiLinks
                links = link_pattern.findall(content)
                for link in links:
                    # Handle aliases and block references
                    clean_link = link.split('|')[0].split('#')[0].split('^')[0]
                    self.links[str(note_path)].append(clean_link)
            except Exception as e:
                print(f"Error analyzing links in {note_path}: {e}")
    
    def _analyze_tags(self):
        """Analyze tag usage."""
        tag_pattern = re.compile(r'#([a-zA-Z0-9_/-]+)')
        
        for note_path in self.notes:
            try:
                with open(note_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find inline tags
                tags = tag_pattern.findall(content)
                for tag in tags:
                    self.tags[tag] += 1
                
                # Find frontmatter tags
                if str(note_path) in self.metadata:
                    meta = self.metadata[str(note_path)]
                    if 'tags' in meta:
                        if isinstance(meta['tags'], list):
                            for tag in meta['tags']:
                                self.tags[str(tag)] += 1
                        elif isinstance(meta['tags'], str):
                            self.tags[meta['tags']] += 1
            except Exception as e:
                print(f"Error analyzing tags in {note_path}: {e}")
    
    def _generate_stats(self):
        """Generate overall statistics."""
        total_notes = len(self.notes)
        notes_with_links = len([n for n in self.links.keys() if self.links[n]])
        total_links = sum(len(links) for links in self.links.values())
        
        # Calculate file sizes
        sizes = []
        for note_path in self.notes:
            try:
                size = note_path.stat().st_size
                sizes.append(size)
            except:
                pass
        
        self.stats.update({
            'total_notes': total_notes,
            'notes_with_links': notes_with_links,
            'total_links': total_links,
            'unique_tags': len(self.tags),
            'avg_links_per_note': total_links / max(total_notes, 1),
            'avg_file_size': sum(sizes) / max(len(sizes), 1) if sizes else 0,
            'largest_file': max(sizes) if sizes else 0,
            'frontmatter_coverage': (self.stats.get('notes_with_frontmatter', 0) / max(total_notes, 1)) * 100
        })
    
    def get_report(self):
        """Generate comprehensive report."""
        report = {
            'vault_path': str(self.vault_path),
            'analysis_date': datetime.now().isoformat(),
            'summary': self.stats,
            'top_tags': dict(self.tags.most_common(20)),
            'metadata_analysis': self._analyze_metadata_quality(),
            'link_analysis': self._analyze_link_quality(),
            'recommendations': self._generate_recommendations()
        }
        return report
    
    def _analyze_metadata_quality(self):
        """Analyze metadata quality and consistency."""
        if not self.metadata:
            return {'status': 'No metadata found'}
        
        date_formats = Counter()
        missing_fields = Counter()
        standard_fields = ['title', 'created', 'modified', 'tags']
        
        for note_path, meta in self.metadata.items():
            # Analyze date formats
            for field in ['created', 'modified', 'date']:
                if field in meta:
                    date_val = str(meta[field])
                    if re.match(r'\d{4}-\d{2}-\d{2}', date_val):
                        date_formats['YYYY-MM-DD'] += 1
                    elif re.match(r'\d{2}/\d{2}/\d{4}', date_val):
                        date_formats['MM/DD/YYYY'] += 1
                    else:
                        date_formats['other'] += 1
            
            # Check for missing standard fields
            for field in standard_fields:
                if field not in meta:
                    missing_fields[field] += 1
        
        return {
            'total_notes_with_metadata': len(self.metadata),
            'date_formats': dict(date_formats),
            'missing_standard_fields': dict(missing_fields),
            'metadata_consistency_score': self._calculate_consistency_score()
        }
    
    def _analyze_link_quality(self):
        """Analyze link quality and find potential issues."""
        broken_links = []
        orphaned_notes = []
        highly_connected = []
        
        # Find notes referenced by others
        referenced_notes = set()
        for links in self.links.values():
            referenced_notes.update(links)
        
        # Check for broken links and orphaned notes
        note_names = {note.stem for note in self.notes}
        
        for note_path, links in self.links.items():
            for link in links:
                if link not in note_names:
                    broken_links.append({'note': note_path, 'broken_link': link})
        
        # Find orphaned notes (no incoming links)
        for note in self.notes:
            if note.stem not in referenced_notes and not self.links.get(str(note), []):
                orphaned_notes.append(str(note))
        
        # Find highly connected notes
        backlink_count = Counter()
        for links in self.links.values():
            for link in links:
                backlink_count[link] += 1
        
        highly_connected = [
            {'note': note, 'backlinks': count}
            for note, count in backlink_count.most_common(10)
        ]
        
        return {
            'broken_links': broken_links[:20],  # Limit output
            'orphaned_notes': orphaned_notes[:20],
            'highly_connected_notes': highly_connected,
            'link_health_score': self._calculate_link_health_score(broken_links, orphaned_notes)
        }
    
    def _calculate_consistency_score(self):
        """Calculate metadata consistency score (0-100)."""
        if not self.metadata:
            return 0
        
        score = 100
        total_notes = len(self.metadata)
        
        # Penalize inconsistent date formats
        date_formats = Counter()
        for meta in self.metadata.values():
            for field in ['created', 'modified', 'date']:
                if field in meta:
                    date_val = str(meta[field])
                    if re.match(r'\d{4}-\d{2}-\d{2}', date_val):
                        date_formats['YYYY-MM-DD'] += 1
                    else:
                        date_formats['other'] += 1
        
        if date_formats and date_formats['other'] > 0:
            score -= (date_formats['other'] / sum(date_formats.values())) * 30
        
        return max(0, round(score))
    
    def _calculate_link_health_score(self, broken_links, orphaned_notes):
        """Calculate link health score (0-100)."""
        total_notes = len(self.notes)
        if total_notes == 0:
            return 100
        
        score = 100
        
        # Penalize broken links
        if broken_links:
            score -= min(30, len(broken_links) / total_notes * 100)
        
        # Penalize orphaned notes
        if orphaned_notes:
            score -= min(40, len(orphaned_notes) / total_notes * 100)
        
        return max(0, round(score))
    
    def _generate_recommendations(self):
        """Generate actionable recommendations."""
        recommendations = []
        
        # Metadata recommendations
        if self.stats.get('frontmatter_coverage', 0) < 70:
            recommendations.append({
                'type': 'metadata',
                'priority': 'high',
                'title': 'Add frontmatter to more notes',
                'description': f"Only {self.stats.get('frontmatter_coverage', 0):.1f}% of notes have frontmatter. Consider adding metadata to improve organization.",
                'action': 'Use Cursor to bulk-add frontmatter templates'
            })
        
        # Tag recommendations
        if len(self.tags) > 100:
            recommendations.append({
                'type': 'organization',
                'priority': 'medium',
                'title': 'Consolidate tag structure',
                'description': f"You have {len(self.tags)} unique tags. Consider creating a tag hierarchy to improve organization.",
                'action': 'Review and consolidate similar tags using Cursor find/replace'
            })
        
        # Link recommendations
        if self.stats.get('avg_links_per_note', 0) < 2:
            recommendations.append({
                'type': 'connectivity',
                'priority': 'medium',
                'title': 'Increase note connectivity',
                'description': f"Average of {self.stats.get('avg_links_per_note', 0):.1f} links per note. More connections improve knowledge discovery.",
                'action': 'Review notes and add relevant internal links'
            })
        
        return recommendations

def main():
    parser = argparse.ArgumentParser(description='Analyze Obsidian vault structure and quality')
    parser.add_argument('vault_path', help='Path to Obsidian vault')
    parser.add_argument('--output', '-o', help='Output file for report (JSON format)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.vault_path):
        print(f"Error: Vault path '{args.vault_path}' does not exist")
        return 1
    
    analyzer = VaultAnalyzer(args.vault_path)
    report = analyzer.analyze()
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\nReport saved to: {args.output}")
    
    # Print summary
    print("\n" + "="*50)
    print("VAULT ANALYSIS SUMMARY")
    print("="*50)
    
    summary = report['summary']
    print(f"Total Notes: {summary['total_notes']}")
    print(f"Notes with Frontmatter: {summary['notes_with_frontmatter']} ({summary['frontmatter_coverage']:.1f}%)")
    print(f"Total Links: {summary['total_links']}")
    print(f"Average Links per Note: {summary['avg_links_per_note']:.1f}")
    print(f"Unique Tags: {summary['unique_tags']}")
    print(f"Average File Size: {summary['avg_file_size']/1024:.1f} KB")
    
    print("\nTOP TAGS:")
    for tag, count in list(report['top_tags'].items())[:10]:
        print(f"  #{tag}: {count}")
    
    print("\nRECOMMENDations:")
    for rec in report['recommendations']:
        print(f"  [{rec['priority'].upper()}] {rec['title']}")
        print(f"    {rec['description']}")
        print(f"    Action: {rec['action']}\n")
    
    return 0

if __name__ == '__main__':
    exit(main()) 