# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the traversal result
        result = []
        
        # Helper function to perform the postorder traversal
        def traverse(node):
            if not node:
                return
            # Traverse the left subtree
            traverse(node.left)
            # Traverse the right subtree
            traverse(node.right)
            # Visit the root (current node)
            result.append(node.val)
        
        # Start the traversal from the root
        traverse(root)
        
        # Return the result of the postorder traversal
        return result