# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # Only append non-null children to the queue
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(level)
        return result

# Time Complexity: O(N)
# Space Complexity: O(N)
             
        