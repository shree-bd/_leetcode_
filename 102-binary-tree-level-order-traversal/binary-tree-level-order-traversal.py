# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         result = []

#         q= collections.deque()
#         q.append(root)

#         while q:
#             qLen = len(q)
#             level = []
#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     level.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if level:
#                 result.append(level)

#         return result

        
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# By using DFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d=defaultdict(list)
        def rec(x,depth):
            self.d[depth].append(x.val)
            if x.left: rec(x.left,depth+1)
            if x.right: rec(x.right,depth+1)
        if root: rec(root,0)
        return [self.d[i] for i in sorted(self.d.keys())]
