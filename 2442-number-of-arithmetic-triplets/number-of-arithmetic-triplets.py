class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0

        for i in nums:
            if i+diff in nums and i+2*diff in nums:
                count+=1

        return count




# class Solution:
#     def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
#         count = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i,n):
#                 for k in range(j,n):
#                     if ((nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff)):
#                         count+=1

#         return count
                
        