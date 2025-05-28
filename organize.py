#!/usr/bin/env python3
"""
LeetCode Repository Organizer
Creates organized directory structure with category-based organization
"""

import os
import shutil
from pathlib import Path
from analytics import LeetCodeAnalytics

class LeetCodeOrganizer:
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.categories_dir = self.repo_path / "categories"
        self.analytics = LeetCodeAnalytics(repo_path)
        
    def create_category_structure(self):
        """Create organized directory structure by categories"""
        print("🗂️  Creating category-based organization...")
        
        # Scan repository first
        self.analytics.scan_repository()
        
        if not self.analytics.problems:
            print("❌ No problems found to organize!")
            return
        
        # Create categories directory
        self.categories_dir.mkdir(exist_ok=True)
        
        # Group problems by category
        stats = self.analytics.generate_statistics()
        problems_by_category = stats['problems_by_category']
        
        for category, problems in problems_by_category.items():
            category_path = self.categories_dir / self._sanitize_name(category)
            category_path.mkdir(exist_ok=True)
            
            # Create README for category
            self._create_category_readme(category_path, category, problems)
            
            # Create symlinks to original problem directories
            for problem in problems:
                original_dir = None
                for p in self.analytics.problems:
                    if p['number'] == problem['number']:
                        original_dir = self.repo_path / p['directory']
                        break
                
                if original_dir and original_dir.exists():
                    link_name = f"{problem['number']:04d}-{self._sanitize_name(problem['name'])}"
                    link_path = category_path / link_name
                    
                    # Remove existing symlink if it exists
                    if link_path.exists() or link_path.is_symlink():
                        link_path.unlink()
                    
                    # Create relative symlink
                    relative_path = os.path.relpath(original_dir, category_path)
                    try:
                        link_path.symlink_to(relative_path)
                    except OSError:
                        # If symlinks aren't supported, copy the directory
                        shutil.copytree(original_dir, link_path, dirs_exist_ok=True)
        
        print(f"✅ Created category structure in {self.categories_dir}")
        
    def _sanitize_name(self, name):
        """Sanitize name for directory/file usage"""
        return name.lower().replace(' ', '-').replace('/', '-').replace('\\', '-')
    
    def _create_category_readme(self, category_path, category_name, problems):
        """Create README for each category"""
        readme_path = category_path / "README.md"
        
        difficulty_counts = {'Easy': 0, 'Medium': 0, 'Hard': 0, 'Unknown': 0}
        for problem in problems:
            difficulty_counts[problem['difficulty']] += 1
        
        content = f"""# {category_name} Problems

**Total Problems:** {len(problems)}

## Difficulty Distribution
- 🟢 **Easy:** {difficulty_counts['Easy']} problems
- 🟡 **Medium:** {difficulty_counts['Medium']} problems  
- 🔴 **Hard:** {difficulty_counts['Hard']} problems
- ⚪ **Unknown:** {difficulty_counts['Unknown']} problems

## Problems List

| # | Problem | Difficulty | Languages |
|---|---------|------------|----------|
"""
        
        for problem in problems:
            difficulty_emoji = "🟢" if problem['difficulty'] == "Easy" else "🟡" if problem['difficulty'] == "Medium" else "🔴" if problem['difficulty'] == "Hard" else "⚪"
            languages_str = ", ".join(problem['languages']) if problem['languages'] else "N/A"
            content += f"| {problem['number']} | [{problem['name']}]({problem['number']:04d}-{self._sanitize_name(problem['name'])}) | {difficulty_emoji} {problem['difficulty']} | {languages_str} |\n"
        
        content += f"""
---
*This category contains {len(problems)} LeetCode problems focused on {category_name.lower()}.*
"""
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    """Main function"""
    print("🚀 LeetCode Repository Organizer")
    print("=" * 40)
    
    organizer = LeetCodeOrganizer()
    organizer.create_category_structure()
    
    print("\n✅ Repository organization complete!")
    print("📁 Check the 'categories' directory for organized problems")

if __name__ == "__main__":
    main() 