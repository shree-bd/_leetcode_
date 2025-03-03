# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        right_side = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):                
                node = queue.popleft()

                if i == level_size - 1:
                    right_side.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side





# Time Complexity: O(N)
# Space Coplexity: O(N)