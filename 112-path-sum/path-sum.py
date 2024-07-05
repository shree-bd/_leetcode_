# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val

        ls = self.hasPathSum(root.left, targetSum - root.val)
        rs = self.hasPathSum(root.right, targetSum - root.val)

        return ls or rs


        