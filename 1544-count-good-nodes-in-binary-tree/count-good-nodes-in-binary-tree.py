# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if not node:
                return 0

            res = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)
            res += dfs(node.left, max_value)
            res += dfs(node.right, max_value)
            return res

        return dfs(root, root.val)

        