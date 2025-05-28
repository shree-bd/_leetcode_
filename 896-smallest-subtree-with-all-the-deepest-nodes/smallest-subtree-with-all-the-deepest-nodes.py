# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_deepest_nodes(root):
            queue = collections.deque([root])
            level = []

            while queue:
                level = list(queue) # alst full level will be the deepest
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return level


        def lca(root, nodes_set):
            if not root or root in nodes_set:
                return root

            left = lca(root.left, nodes_set )
            right = lca(root.right, nodes_set)

            if left and right:
                return root
            else:
                return left or right

        deepest_nodes = find_deepest_nodes(root)
        return lca(root, set(deepest_nodes))

        