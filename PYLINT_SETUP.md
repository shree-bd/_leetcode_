# 🔧 PyLint Setup & Issue Resolution

This document explains how to resolve PyLint issues in your LeetCode repository.

## 🚀 Quick Fix

Run this command to automatically fix common PyLint issues:

```bash
python3 fix_pylint.py
```

## 📋 Current PyLint Configuration

The repository includes a `.pylintrc` file with relaxed settings suitable for LeetCode solutions:

### Disabled Checks
- `missing-module-docstring` - Not required for solution files
- `missing-class-docstring` - Not required for simple classes
- `missing-function-docstring` - Not required for solution functions
- `line-too-long` - Allows longer lines for readability
- `invalid-name` - Allows short variable names (common in algorithms)
- `broad-except` - Allows general exception handling

### Enabled Checks (Critical Only)
- `syntax-error` - Python syntax errors
- `undefined-variable` - Using undefined variables
- `unused-import` - Importing unused modules
- `import-error` - Import issues

## 🔄 GitHub Workflow

The PyLint workflow (`.github/workflows/pylint.yml`) is configured to:

1. **Run on Python 3.10 only** (faster CI)
2. **Check only 3 files** per run (prevents overwhelming CI)
3. **Focus on critical errors** only (not style issues)
4. **Non-blocking** - warnings don't fail the build

## 🛠️ Manual PyLint Fixes

### Common Issues & Solutions

#### 1. Missing Module Docstring
**Issue:** `C0114: Missing module docstring`

**Fix:** Add a docstring at the top of your Python file:
```python
"""
LeetCode Problem: Two Sum
"""

# Your solution code here...
```

#### 2. Missing Import
**Issue:** `E0602: Undefined variable 'List'`

**Fix:** Add the missing import:
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Your code here
```

#### 3. Unused Import
**Issue:** `W0611: Unused import`

**Fix:** Remove the unused import or use it in your code.

#### 4. Line Too Long
**Issue:** `C0301: Line too long`

**Fix:** Break long lines:
```python
# Instead of:
result = some_very_long_function_name(parameter1, parameter2, parameter3, parameter4)

# Use:
result = some_very_long_function_name(
    parameter1, parameter2, 
    parameter3, parameter4
)
```

## 🎯 Best Practices for LeetCode Solutions

### 1. File Structure
```python
"""
LeetCode Problem: [Problem Name]
"""
from typing import List, Optional  # Add imports as needed

class Solution:
    def problemMethod(self, param1: List[int]) -> int:
        """Solve the problem."""
        # Your solution here
        pass

# Test cases (optional)
if __name__ == "__main__":
    solution = Solution()
    # Test your solution
```

### 2. Variable Naming
- Use descriptive names when possible: `left`, `right`, `result`
- Short names are OK for loops: `i`, `j`, `k`
- Use snake_case for variables and functions

### 3. Type Hints
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    """Find two numbers that add up to target."""
    pass
```

## 🔧 Running PyLint Locally

### Check a specific file:
```bash
pylint --rcfile=.pylintrc your_file.py
```

### Check only critical errors:
```bash
pylint --rcfile=.pylintrc --disable=all --enable=syntax-error,undefined-variable your_file.py
```

### Check all Python files in problem directories:
```bash
find . -name "*.py" -path "./[0-9]*" | head -5 | xargs pylint --rcfile=.pylintrc
```

## 🚫 Excluding Files from PyLint

Files listed in `.gitignore` under "Management scripts" are excluded:
- `analytics.py`
- `organize.py` 
- `progress_tracker.py`
- `manage.py`
- `fix_pylint.py`

## 📊 Understanding PyLint Scores

PyLint gives scores from -10 to 10:
- **10.0** - Perfect code
- **8.0+** - Very good
- **6.0+** - Good enough for LeetCode solutions
- **Below 6.0** - Needs improvement

## 🔄 Automated Fixes

The `fix_pylint.py` script automatically:
1. Adds missing module docstrings
2. Adds missing `typing` imports
3. Fixes basic formatting issues

## 🎯 CI/CD Integration

The GitHub workflow will:
- ✅ **Pass** if no critical errors found
- ⚠️ **Warn** about style issues (non-blocking)
- ❌ **Fail** only on syntax errors or undefined variables

## 🆘 Troubleshooting

### If PyLint is still failing:

1. **Check the specific error message** in the GitHub Actions log
2. **Run PyLint locally** to see the exact issues
3. **Use the fix script**: `python3 fix_pylint.py`
4. **Manually fix remaining issues** using this guide

### Common Commands:
```bash
# Fix common issues automatically
python3 fix_pylint.py

# Check what PyLint would report
pylint --rcfile=.pylintrc $(find . -name "*.py" -path "./[0-9]*" | head -3)

# Update repository analytics
python3 manage.py all
```

---

*This setup ensures your LeetCode repository maintains code quality while keeping the CI/CD pipeline fast and reliable! 🚀* 