class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                count+=(right - left)
                left+=1
            else:
                right-=1

        return count








# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] < target:
#                     count = count + 1
#         return count

        