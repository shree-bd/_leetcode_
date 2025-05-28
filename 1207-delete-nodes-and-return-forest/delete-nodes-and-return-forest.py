# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []

        def dfs(node, parent_deleted):
            if not node:
                return None

            deleted = node.val in to_delete_set
            if parent_deleted and not deleted:
                res.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return res

# T.C: O(N) | SC.: O(N)
