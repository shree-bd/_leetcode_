class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0] * count)
        """
        Do not return anything, modify nums in-place instead.
        """
        