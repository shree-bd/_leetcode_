# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildBST(left: int, right:int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left+right) //2
            node = TreeNode(nums[mid])

            node.left = buildBST(left, mid-1)
            node.right = buildBST(mid+1,right)

            return node

        return buildBST(0, len(nums) -1)

            

        