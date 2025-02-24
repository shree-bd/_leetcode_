# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # Helper function to perform preorder DFS traversal
        def dfs(node):
            if not node:
                return ["N"]
            return [str(node.val)] + dfs(node.left) + dfs(node.right)

        return ",".join(dfs(root))  # Join the list into a comma-separated string
                 

    def deserialize(self, data):
        values = data.split(",")  # Split the serialized string into a list
        # Helper function for deserialization using index
        def dfs(index):
            if values[index] == "N":
                return None, index + 1
            node = TreeNode(int(values[index]))
            node.left, index = dfs(index + 1)  # Deserialize left child
            node.right, index = dfs(index)     # Deserialize right child
            return node, index
        
        root, _ = dfs(0)  # Start from the first element and return the root
        return root


        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))