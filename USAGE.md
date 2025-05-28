# 📚 LeetCode Repository Usage Guide

This guide explains how to use the comprehensive management tools for your LeetCode solutions repository.

## 🚀 Quick Start

### Run All Operations
```bash
python3 manage.py all
```
This will update analytics, organize the repository, and track progress in one command.

## 📊 Available Commands

### 1. Update Analytics (`update`)
Updates the main README.md with comprehensive statistics and problem categorization.

```bash
python3 manage.py update
```

**What it does:**
- Scans all problem directories
- Categorizes problems by topic (Trees, Arrays, Strings, etc.)
- Generates difficulty distribution
- Creates language usage statistics
- Updates README.md with formatted tables and analytics

### 2. Organize Repository (`organize`)
Creates a category-based organization structure in the `categories/` directory.

```bash
python3 manage.py organize
```

**What it does:**
- Creates `categories/` directory
- Groups problems by category (Trees, Arrays, etc.)
- Creates symlinks to original problem directories
- Generates category-specific README files
- Maintains original directory structure

### 3. Track Progress (`progress`)
Updates progress tracking and generates detailed progress reports.

```bash
python3 manage.py progress
```

**What it does:**
- Records current progress in `progress_history.json`
- Tracks milestones (10, 25, 50, 100, 150, 200+ problems)
- Generates `PROGRESS.md` with detailed progress analytics
- Calculates daily, weekly, and monthly progress

### 4. Show Quick Stats (`stats`)
Displays quick statistics without generating files.

```bash
python3 manage.py stats
```

**What it shows:**
- Total problems solved
- Language distribution
- Difficulty breakdown
- Top categories

## 📁 Repository Structure

After running the management tools, your repository will have this structure:

```
leetcode-repository/
├── README.md                    # Main analytics dashboard
├── PROGRESS.md                  # Detailed progress tracking
├── USAGE.md                     # This usage guide
├── progress_history.json        # Progress tracking data
├── categories/                  # Organized by topic
│   ├── arrays/
│   │   ├── README.md
│   │   ├── 0001-two-sum/       # Symlink to original
│   │   └── 0015-3sum/          # Symlink to original
│   ├── trees/
│   │   ├── README.md
│   │   └── 0104-maximum-depth-of-binary-tree/
│   └── strings/
│       ├── README.md
│       └── 0125-valid-palindrome/
├── 1-two-sum/                   # Original problem directories
│   ├── README.md
│   └── two-sum.py
├── 15-3sum/
│   ├── README.md
│   └── 3sum.py
└── management scripts/
    ├── analytics.py             # Core analytics engine
    ├── organize.py              # Repository organizer
    ├── progress_tracker.py      # Progress tracking
    └── manage.py                # Main management interface
```

## 🔧 Management Scripts

### `analytics.py`
Core analytics engine that scans and categorizes problems.

**Features:**
- Automatic problem detection
- Smart categorization based on problem names and numbers
- Difficulty extraction from README files
- Language detection from solution files
- Comprehensive statistics generation

### `organize.py`
Creates category-based organization using symlinks.

**Features:**
- Category-based directory structure
- Symlinks preserve original organization
- Category-specific README files
- Cross-platform compatibility

### `progress_tracker.py`
Tracks progress over time with milestone detection.

**Features:**
- Historical progress tracking
- Milestone achievement detection
- Progress trend analysis
- Detailed progress reports

### `manage.py`
Unified command-line interface for all operations.

**Features:**
- Single entry point for all operations
- Command-line argument parsing
- Comprehensive help and examples
- Error handling and user feedback

## 📈 Analytics Features

### Problem Categorization
Problems are automatically categorized into:
- **Trees**: Binary trees, BST, tree traversal
- **Arrays**: Array manipulation, matrix problems
- **Strings**: String processing, palindromes
- **Linked Lists**: List operations, cycles
- **Hash Table**: Hash maps, frequency counting
- **Graphs**: Graph traversal, islands
- **Stack/Queue**: Stack operations, parentheses
- **Dynamic Programming**: DP problems
- **Binary Search**: Search algorithms
- **Database/SQL**: SQL query problems
- **Other**: Miscellaneous problems

### Difficulty Detection
Automatically detects difficulty from:
- README file content
- Problem descriptions
- Manual classification for known problems

### Language Support
Detects solutions in:
- Python (`.py`)
- Java (`.java`)
- C++ (`.cpp`)
- JavaScript (`.js`)

## 🎯 Progress Tracking

### Milestones
Automatic milestone tracking for:
- 10, 25, 50, 75, 100 problems
- 150, 200, 250, 300 problems
- 400, 500, 750, 1000+ problems

### Progress Metrics
- Daily problem solving rate
- Weekly and monthly progress
- Category-wise progress
- Language usage trends
- Difficulty progression

## 🔄 Automation

### Regular Updates
Run this command regularly to keep everything updated:
```bash
python3 manage.py all
```

### Git Integration
The repository includes a `.gitignore` file that excludes:
- Python cache files
- IDE configuration
- Temporary files
- OS-specific files

## 🛠️ Customization

### Adding New Categories
Edit the `categorize_problem()` method in `analytics.py` to add new categories:

```python
def categorize_problem(self, problem_name, problem_num):
    name_lower = problem_name.lower()
    
    # Add your custom category logic here
    if 'your_keyword' in name_lower:
        return 'Your Category'
    # ... existing logic
```

### Custom Milestones
Modify the milestones list in `progress_tracker.py`:

```python
milestones = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 750, 1000]
```

### Custom Difficulty Detection
Enhance difficulty detection in the `extract_difficulty()` method in `analytics.py`.

## 🐛 Troubleshooting

### Common Issues

1. **No problems found**: Ensure your problem directories follow the format `number-problem-name/`
2. **Symlinks not working**: On Windows, run as administrator or use the copy fallback
3. **Missing dependencies**: Ensure Python 3.6+ is installed
4. **Permission errors**: Check file permissions for the repository directory

### Getting Help

Run any command with `-h` for help:
```bash
python3 manage.py -h
```

## 🎉 Tips for Best Results

1. **Consistent Naming**: Use the format `number-problem-name/` for directories
2. **Include READMEs**: Add README.md files to problem directories with difficulty information
3. **Regular Updates**: Run `python3 manage.py all` after adding new problems
4. **Backup Progress**: The `progress_history.json` file contains your progress data - back it up!
5. **Explore Categories**: Use the `categories/` directory to study problems by topic

---

*Happy coding! 🚀* 