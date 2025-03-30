# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum = curr_sum * 10 + node.val

            # if its a leaf node, add to total
            if not node.left and not node.right:
                self.total += curr_sum
                return

            left = dfs(node.left, curr_sum)
            right = dfs(node.right, curr_sum)

        dfs(root, 0)
        return self.total

# Time Complexity: O(N)
# Space Complexity: O(H)
# Best case: H -> log N O(log N) | Worst case: H = N → So, space = O(N)
        