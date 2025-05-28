"""
LeetCode Problem: 110 Balanced Binary Tree
"""

from typing import Optional

"""
LeetCode Problem: 110 Balanced Binary Tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # def dfs(root):
        #     if not root: return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        #     return [balanced, 1 + max(left[1], right[1])]

        # return dfs(root)[0]

        def dfs(node):
            if not node:
                return 0  # Height of an empty tree is 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # If any subtree is unbalanced, propagate -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1  
            
            return 1 + max(left, right)  # Height of current node
        
        return dfs(root) != -1

                
        