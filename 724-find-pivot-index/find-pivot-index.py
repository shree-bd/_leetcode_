class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (total - left_sum - num):
                return i
            left_sum += num
        return -1

#  TC: O(N) | SC.: O(1)

"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        n  = len(nums)

        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

#  TC: O(N^2) | SC.: O(1)

"""