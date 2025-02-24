# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if current node is "good"
            count = 1 if node.val >= max_val else 0
            
            # Update max value seen so far
            max_val = max(max_val, node.val)
            
            # Recur for left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            
            return count
        
        return dfs(root, root.val)  # Start DFS with root's value as max_val
        