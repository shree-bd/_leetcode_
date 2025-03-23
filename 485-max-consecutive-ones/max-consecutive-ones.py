class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_count = 0
        curr_ones = 0

        for n in nums:
            if n == 1:
                curr_ones += 1
                max_count = max(max_count, curr_ones)
            else:
                curr_ones = 0
        return max_count

        