# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    # >>>>>>>>>>> USING BFS (LEVEL ORDER TRAVERSAL) <<<<<<<<<<<<<<<<<<<
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1  # Increase depth after processing a level

        return depth


# Time Complexity: O(N) (visiting each node once)
# Space Complexity: O(H) (H = tree height, worst case O(N) for skewed trees)