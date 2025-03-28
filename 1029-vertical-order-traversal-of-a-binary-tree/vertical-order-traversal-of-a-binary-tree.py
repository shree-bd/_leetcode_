# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        dict_nodes = defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        res = [] 
        
        while queue:
            node, col, row = queue.popleft()
            dict_nodes[col].append((row, node.val))
            if node.left:
                queue.append((node.left, col-1, row+1))
            if node.right:
                queue.append((node.right, col+1, row+1))
        
        for col in sorted(dict_nodes.keys()):
            dict_nodes[col].sort(key = lambda x : (x[0], x[1])) # sort by row then by value
            res.append([val for _ , val in dict_nodes[col]])
        return res 
 
        