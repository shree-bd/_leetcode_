#!/usr/bin/env python3
"""
LeetCode Progress Tracker
Tracks progress over time and generates visual progress reports
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
from analytics import LeetCodeAnalytics

class ProgressTracker:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.progress_file = os.path.join(repo_path, "progress_history.json")
        self.analytics = LeetCodeAnalytics(repo_path)
        
    def load_progress_history(self):
        """Load existing progress history"""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"entries": [], "milestones": []}
    
    def save_progress_history(self, history):
        """Save progress history"""
        with open(self.progress_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def update_progress(self):
        """Update progress with current state"""
        print("📊 Updating progress tracking...")
        
        # Scan current repository
        self.analytics.scan_repository()
        stats = self.analytics.generate_statistics()
        
        # Load existing history
        history = self.load_progress_history()
        
        # Create new entry
        today = datetime.now().strftime('%Y-%m-%d')
        new_entry = {
            "date": today,
            "total_problems": stats['total_problems'],
            "difficulty_distribution": stats['difficulty_distribution'],
            "category_distribution": stats['category_distribution'],
            "language_distribution": stats['language_distribution']
        }
        
        # Check if we already have an entry for today
        existing_entry = None
        for i, entry in enumerate(history["entries"]):
            if entry["date"] == today:
                existing_entry = i
                break
        
        if existing_entry is not None:
            history["entries"][existing_entry] = new_entry
        else:
            history["entries"].append(new_entry)
        
        # Check for new milestones
        self._check_milestones(history, stats['total_problems'])
        
        # Save updated history
        self.save_progress_history(history)
        
        print(f"✅ Progress updated! Current total: {stats['total_problems']} problems")
        
    def _check_milestones(self, history, current_total):
        """Check and record milestones"""
        milestones = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 750, 1000]
        
        for milestone in milestones:
            if current_total >= milestone:
                # Check if this milestone is already recorded
                milestone_exists = any(m["count"] == milestone for m in history["milestones"])
                if not milestone_exists:
                    history["milestones"].append({
                        "count": milestone,
                        "date": datetime.now().strftime('%Y-%m-%d'),
                        "achieved": True
                    })
    
    def generate_progress_report(self):
        """Generate a comprehensive progress report"""
        history = self.load_progress_history()
        
        if not history["entries"]:
            return "No progress history available. Run update_progress() first."
        
        # Sort entries by date
        entries = sorted(history["entries"], key=lambda x: x["date"])
        
        # Calculate progress metrics
        latest = entries[-1]
        if len(entries) > 1:
            previous = entries[-2]
            daily_change = latest["total_problems"] - previous["total_problems"]
        else:
            daily_change = 0
        
        # Calculate weekly/monthly progress if we have enough data
        weekly_progress = self._calculate_period_progress(entries, 7)
        monthly_progress = self._calculate_period_progress(entries, 30)
        
        report = f"""# 📈 Progress Report

## Current Status
- **Total Problems Solved:** {latest['total_problems']} 🎯
- **Last Updated:** {latest['date']}
- **Daily Change:** {'+' if daily_change >= 0 else ''}{daily_change} problems

## Recent Progress
- **Weekly Progress:** {weekly_progress} problems
- **Monthly Progress:** {monthly_progress} problems

## Milestones Achieved 🏆
"""
        
        achieved_milestones = [m for m in history["milestones"] if m["achieved"]]
        achieved_milestones.sort(key=lambda x: x["count"])
        
        for milestone in achieved_milestones:
            report += f"- ✅ **{milestone['count']} problems** (achieved on {milestone['date']})\n"
        
        # Next milestone
        next_milestone = self._get_next_milestone(latest["total_problems"])
        if next_milestone:
            remaining = next_milestone - latest["total_problems"]
            report += f"\n## Next Milestone 🎯\n"
            report += f"- **Target:** {next_milestone} problems\n"
            report += f"- **Remaining:** {remaining} problems\n"
            report += f"- **Progress:** {latest['total_problems']}/{next_milestone} ({(latest['total_problems']/next_milestone*100):.1f}%)\n"
        
        # Progress over time
        if len(entries) >= 2:
            report += "\n## Progress Over Time\n\n"
            report += "| Date | Total Problems | Daily Change | Cumulative |\n"
            report += "|------|----------------|--------------|------------|\n"
            
            for i, entry in enumerate(entries[-10:]):  # Show last 10 entries
                if i == 0:
                    change = 0
                else:
                    prev_entry = entries[entries.index(entry) - 1]
                    change = entry["total_problems"] - prev_entry["total_problems"]
                
                change_str = f"+{change}" if change > 0 else str(change) if change < 0 else "0"
                report += f"| {entry['date']} | {entry['total_problems']} | {change_str} | {entry['total_problems']} |\n"
        
        # Category progress
        report += f"\n## Current Category Distribution\n\n"
        for category, count in sorted(latest['category_distribution'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / latest['total_problems']) * 100
            report += f"- **{category}:** {count} problems ({percentage:.1f}%)\n"
        
        return report
    
    def _calculate_period_progress(self, entries, days):
        """Calculate progress over a specific period"""
        if len(entries) < 2:
            return 0
        
        target_date = datetime.now() - timedelta(days=days)
        target_date_str = target_date.strftime('%Y-%m-%d')
        
        # Find entry closest to target date
        closest_entry = None
        for entry in entries:
            if entry["date"] <= target_date_str:
                closest_entry = entry
        
        if closest_entry:
            return entries[-1]["total_problems"] - closest_entry["total_problems"]
        else:
            # If no entry from that period, use the earliest entry
            return entries[-1]["total_problems"] - entries[0]["total_problems"]
    
    def _get_next_milestone(self, current_total):
        """Get the next milestone to achieve"""
        milestones = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1500, 2000]
        
        for milestone in milestones:
            if current_total < milestone:
                return milestone
        
        # If beyond all predefined milestones, calculate next 500 increment
        return ((current_total // 500) + 1) * 500

def main():
    """Main function"""
    print("📊 LeetCode Progress Tracker")
    print("=" * 40)
    
    tracker = ProgressTracker()
    
    # Update progress
    tracker.update_progress()
    
    # Generate and save progress report
    report = tracker.generate_progress_report()
    
    with open("PROGRESS.md", "w") as f:
        f.write(report)
    
    print("\n✅ Progress tracking complete!")
    print("📄 Check PROGRESS.md for detailed progress report")

if __name__ == "__main__":
    main() 