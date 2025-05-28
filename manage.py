#!/usr/bin/env python3
"""
LeetCode Repository Manager
Comprehensive management tool for organizing and tracking LeetCode solutions
"""

import argparse
import sys
from analytics import LeetCodeAnalytics
from organize import LeetCodeOrganizer
from progress_tracker import ProgressTracker

def main():
    parser = argparse.ArgumentParser(
        description="LeetCode Repository Manager - Organize and track your LeetCode solutions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python manage.py update          # Update README with latest analytics
  python manage.py organize        # Create category-based organization
  python manage.py progress        # Update progress tracking
  python manage.py all             # Run all operations
  python manage.py stats           # Show quick statistics
        """
    )
    
    parser.add_argument(
        'command',
        choices=['update', 'organize', 'progress', 'all', 'stats'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '--path',
        default='.',
        help='Path to the LeetCode repository (default: current directory)'
    )
    
    args = parser.parse_args()
    
    print("🚀 LeetCode Repository Manager")
    print("=" * 50)
    
    if args.command == 'update':
        update_analytics(args.path)
    elif args.command == 'organize':
        organize_repository(args.path)
    elif args.command == 'progress':
        track_progress(args.path)
    elif args.command == 'all':
        update_analytics(args.path)
        organize_repository(args.path)
        track_progress(args.path)
        print("\n🎉 All operations completed successfully!")
    elif args.command == 'stats':
        show_quick_stats(args.path)

def update_analytics(repo_path):
    """Update repository analytics and README"""
    print("\n📊 Updating Analytics...")
    print("-" * 30)
    
    analytics = LeetCodeAnalytics(repo_path)
    analytics.scan_repository()
    
    if not analytics.problems:
        print("❌ No LeetCode problems found in the repository!")
        return
    
    stats = analytics.generate_statistics()
    
    # Generate and save markdown report
    report = analytics.generate_markdown_report()
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Found {stats['total_problems']} problems")
    print(f"✅ Updated README.md with comprehensive analytics")

def organize_repository(repo_path):
    """Organize repository by categories"""
    print("\n🗂️  Organizing Repository...")
    print("-" * 30)
    
    organizer = LeetCodeOrganizer(repo_path)
    organizer.create_category_structure()

def track_progress(repo_path):
    """Update progress tracking"""
    print("\n📈 Tracking Progress...")
    print("-" * 30)
    
    tracker = ProgressTracker(repo_path)
    tracker.update_progress()
    
    # Generate and save progress report
    report = tracker.generate_progress_report()
    
    with open("PROGRESS.md", "w") as f:
        f.write(report)
    
    print("✅ Generated PROGRESS.md with detailed progress report")

def show_quick_stats(repo_path):
    """Show quick statistics"""
    print("\n📊 Quick Statistics")
    print("-" * 30)
    
    analytics = LeetCodeAnalytics(repo_path)
    analytics.scan_repository()
    
    if not analytics.problems:
        print("❌ No LeetCode problems found!")
        return
    
    stats = analytics.generate_statistics()
    
    print(f"📈 Total Problems: {stats['total_problems']}")
    print(f"🎯 Problem Range: #{stats['problem_range']['min']} - #{stats['problem_range']['max']}")
    
    print(f"\n💻 Languages:")
    for lang, count in sorted(stats['language_distribution'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['total_problems']) * 100
        print(f"   {lang}: {count} ({percentage:.1f}%)")
    
    print(f"\n🎯 Difficulty:")
    for difficulty, count in sorted(stats['difficulty_distribution'].items(), key=lambda x: x[1], reverse=True):
        percentage = (count / stats['total_problems']) * 100
        emoji = "🟢" if difficulty == "Easy" else "🟡" if difficulty == "Medium" else "🔴" if difficulty == "Hard" else "⚪"
        print(f"   {emoji} {difficulty}: {count} ({percentage:.1f}%)")
    
    print(f"\n📚 Top Categories:")
    for category, count in sorted(stats['category_distribution'].items(), key=lambda x: x[1], reverse=True)[:5]:
        percentage = (count / stats['total_problems']) * 100
        print(f"   {category}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    main() 