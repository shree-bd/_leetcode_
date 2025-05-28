"""
LeetCode Problem: 100 Same Tree
"""

from typing import Optional

"""
LeetCode Problem: 100 Same Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Both trees are None
            return True
        if not p or not q:  # One is None, the other is not
            return False
        if p.val != q.val:  # Values don’t match
            return False

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)