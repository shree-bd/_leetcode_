class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)

        for i in range(1, n+2):
            if i not in nums:
                return i        