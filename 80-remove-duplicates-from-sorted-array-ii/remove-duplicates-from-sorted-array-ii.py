class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 0

        for r in nums:
            if l < 2 or r != nums[l-2]:
                nums[l] = r
                l += 1
        return l
        