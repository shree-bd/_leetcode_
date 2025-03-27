# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r
















        # if not root or root == p or root == q:
        #     return root

        # l = self.lowestCommonAncestor(root.left, p, q)
        # r = self.lowestCommonAncestor(root.right, p, q)

        # if l and r:
        #     return root  # If p and q are found in different subtrees, root is LCA
        # else:
        #     return l or r   # If both are in the same subtree, return the one that is non-null


# Time Complexity: O(N)
# Space Complexity: O(H)

        
        