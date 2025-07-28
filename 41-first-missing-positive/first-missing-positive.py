class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx] , nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
        





"""
        nums = set(nums)
        n = len(nums)

        for i in range(1, n+2):
            if i not in nums:
                return i        

# TC: O(N) | SC: O(N)
"""