#!/usr/bin/env python3
"""
LeetCode Repository Analytics
Analyzes the repository structure and generates comprehensive statistics
"""

import os
import re
import json
from collections import defaultdict, Counter
from datetime import datetime
import subprocess

class LeetCodeAnalytics:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        self.problems = []
        self.stats = defaultdict(int)
        self.difficulty_map = {}
        self.category_map = defaultdict(list)
        
    def scan_repository(self):
        """Scan the repository for LeetCode problems"""
        for item in os.listdir(self.repo_path):
            if os.path.isdir(os.path.join(self.repo_path, item)) and item != ".git":
                # Check if it's a LeetCode problem directory (starts with number)
                if re.match(r'^\d+', item):
                    problem_info = self.analyze_problem(item)
                    if problem_info:
                        self.problems.append(problem_info)
    
    def analyze_problem(self, problem_dir):
        """Analyze a single problem directory"""
        problem_path = os.path.join(self.repo_path, problem_dir)
        
        # Extract problem number and name
        match = re.match(r'^(\d+)-(.+)', problem_dir)
        if not match:
            return None
            
        problem_num = int(match.group(1))
        problem_name = match.group(2).replace('-', ' ').title()
        
        # Check for solution files
        solutions = []
        languages = set()
        
        for file in os.listdir(problem_path):
            if file.endswith('.py'):
                solutions.append(file)
                languages.add('Python')
            elif file.endswith('.java'):
                solutions.append(file)
                languages.add('Java')
            elif file.endswith('.cpp'):
                solutions.append(file)
                languages.add('C++')
            elif file.endswith('.js'):
                solutions.append(file)
                languages.add('JavaScript')
        
        # Try to extract difficulty from README if exists
        difficulty = self.extract_difficulty(problem_path)
        category = self.categorize_problem(problem_name, problem_num)
        
        return {
            'number': problem_num,
            'name': problem_name,
            'directory': problem_dir,
            'solutions': solutions,
            'languages': list(languages),
            'difficulty': difficulty,
            'category': category
        }
    
    def extract_difficulty(self, problem_path):
        """Extract difficulty from README file"""
        readme_path = os.path.join(problem_path, 'README.md')
        if os.path.exists(readme_path):
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    if 'easy' in content:
                        return 'Easy'
                    elif 'medium' in content:
                        return 'Medium'
                    elif 'hard' in content:
                        return 'Hard'
            except:
                pass
        return 'Unknown'
    
    def categorize_problem(self, problem_name, problem_num):
        """Categorize problems based on common patterns"""
        name_lower = problem_name.lower()
        
        # Tree problems
        if any(keyword in name_lower for keyword in ['tree', 'binary tree', 'bst', 'ancestor']):
            return 'Trees'
        
        # Array problems
        elif any(keyword in name_lower for keyword in ['array', 'matrix', 'subarray']):
            return 'Arrays'
        
        # String problems
        elif any(keyword in name_lower for keyword in ['string', 'substring', 'palindrome', 'word']):
            return 'Strings'
        
        # Linked List problems
        elif any(keyword in name_lower for keyword in ['linked list', 'list', 'node']):
            return 'Linked Lists'
        
        # Graph problems
        elif any(keyword in name_lower for keyword in ['graph', 'island', 'path']):
            return 'Graphs'
        
        # Dynamic Programming
        elif any(keyword in name_lower for keyword in ['climb', 'fibonacci', 'dp']):
            return 'Dynamic Programming'
        
        # Stack/Queue problems
        elif any(keyword in name_lower for keyword in ['stack', 'queue', 'parentheses']):
            return 'Stack/Queue'
        
        # Hash Table problems
        elif any(keyword in name_lower for keyword in ['hash', 'map', 'sum']):
            return 'Hash Table'
        
        # Binary Search
        elif any(keyword in name_lower for keyword in ['search', 'sorted', 'binary search']):
            return 'Binary Search'
        
        # Two Pointers
        elif any(keyword in name_lower for keyword in ['two pointer', 'palindrome']):
            return 'Two Pointers'
        
        # SQL problems (based on common problem numbers)
        elif problem_num in [175, 176, 177, 178, 180, 181, 182, 183, 184, 185, 196, 197, 262, 511, 512, 577, 584, 585, 586, 595, 596, 597, 601, 608, 627]:
            return 'Database/SQL'
        
        else:
            return 'Other'
    
    def generate_statistics(self):
        """Generate comprehensive statistics"""
        if not self.problems:
            return {}
        
        # Basic stats
        total_problems = len(self.problems)
        
        # Language distribution
        language_count = Counter()
        for problem in self.problems:
            for lang in problem['languages']:
                language_count[lang] += 1
        
        # Difficulty distribution
        difficulty_count = Counter(problem['difficulty'] for problem in self.problems)
        
        # Category distribution
        category_count = Counter(problem['category'] for problem in self.problems)
        
        # Problem number ranges
        problem_numbers = [p['number'] for p in self.problems]
        min_problem = min(problem_numbers)
        max_problem = max(problem_numbers)
        
        return {
            'total_problems': total_problems,
            'language_distribution': dict(language_count),
            'difficulty_distribution': dict(difficulty_count),
            'category_distribution': dict(category_count),
            'problem_range': {
                'min': min_problem,
                'max': max_problem
            },
            'problems_by_category': self.group_problems_by_category()
        }
    
    def group_problems_by_category(self):
        """Group problems by category"""
        categories = defaultdict(list)
        for problem in self.problems:
            categories[problem['category']].append({
                'number': problem['number'],
                'name': problem['name'],
                'difficulty': problem['difficulty'],
                'languages': problem['languages']
            })
        
        # Sort problems within each category by number
        for category in categories:
            categories[category].sort(key=lambda x: x['number'])
        
        return dict(categories)
    
    def generate_markdown_report(self):
        """Generate a comprehensive markdown report"""
        stats = self.generate_statistics()
        
        report = f"""# 🚀 LeetCode Solutions Repository

## 📊 Analytics Dashboard

**Total Problems Solved:** {stats['total_problems']} 🎯

### 📈 Progress Overview
- **Minimum Problem Number:** #{stats['problem_range']['min']}
- **Maximum Problem Number:** #{stats['problem_range']['max']}
- **Coverage Range:** {stats['problem_range']['max'] - stats['problem_range']['min'] + 1} problems span

### 💻 Language Distribution
"""
        
        for lang, count in sorted(stats['language_distribution'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / stats['total_problems']) * 100
            report += f"- **{lang}:** {count} solutions ({percentage:.1f}%)\n"
        
        report += "\n### 🎯 Difficulty Breakdown\n"
        for difficulty, count in sorted(stats['difficulty_distribution'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / stats['total_problems']) * 100
            emoji = "🟢" if difficulty == "Easy" else "🟡" if difficulty == "Medium" else "🔴" if difficulty == "Hard" else "⚪"
            report += f"- {emoji} **{difficulty}:** {count} problems ({percentage:.1f}%)\n"
        
        report += "\n### 📚 Category Distribution\n"
        for category, count in sorted(stats['category_distribution'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / stats['total_problems']) * 100
            report += f"- **{category}:** {count} problems ({percentage:.1f}%)\n"
        
        report += "\n## 📁 Problems by Category\n\n"
        
        for category, problems in sorted(stats['problems_by_category'].items()):
            report += f"### {category} ({len(problems)} problems)\n\n"
            report += "| # | Problem | Difficulty | Languages |\n"
            report += "|---|---------|------------|----------|\n"
            
            for problem in problems:
                difficulty_emoji = "🟢" if problem['difficulty'] == "Easy" else "🟡" if problem['difficulty'] == "Medium" else "🔴" if problem['difficulty'] == "Hard" else "⚪"
                languages_str = ", ".join(problem['languages'])
                report += f"| {problem['number']} | {problem['name']} | {difficulty_emoji} {problem['difficulty']} | {languages_str} |\n"
            
            report += "\n"
        
        report += f"""
## 🛠️ Repository Structure

Each problem is organized in its own directory with the following structure:
```
{stats['problem_range']['min']}-problem-name/
├── README.md          # Problem description and approach
├── solution.py        # Python solution
└── solution.java      # Java solution (if available)
```

## 📝 How to Use This Repository

1. **Browse by Category:** Use the category sections above to find problems by topic
2. **Search by Number:** Problems are organized numerically in directories
3. **Multiple Languages:** Most problems include solutions in Python, some in Java
4. **Detailed Explanations:** Each problem includes a README with approach and complexity analysis

## 🎯 Goals & Progress Tracking

- **Current Streak:** {stats['total_problems']} problems solved! 🔥
- **Next Milestone:** {((stats['total_problems'] // 50) + 1) * 50} problems
- **Progress to Next Milestone:** {stats['total_problems'] % 50}/50 ({((stats['total_problems'] % 50) / 50 * 100):.1f}%)

---

*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Generated automatically by analytics.py*
"""
        
        return report

def main():
    """Main function to run analytics"""
    print("🔍 Analyzing LeetCode repository...")
    
    analytics = LeetCodeAnalytics()
    analytics.scan_repository()
    
    if not analytics.problems:
        print("❌ No LeetCode problems found in the repository!")
        return
    
    print(f"✅ Found {len(analytics.problems)} LeetCode problems!")
    
    # Generate statistics
    stats = analytics.generate_statistics()
    
    # Print summary to console
    print(f"\n📊 Quick Stats:")
    print(f"   Total Problems: {stats['total_problems']}")
    print(f"   Languages: {', '.join(stats['language_distribution'].keys())}")
    print(f"   Categories: {len(stats['category_distribution'])}")
    
    # Generate and save markdown report
    report = analytics.generate_markdown_report()
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Updated README.md with comprehensive analytics!")
    print(f"🎯 Repository is now organized and ready!")

if __name__ == "__main__":
    main() 