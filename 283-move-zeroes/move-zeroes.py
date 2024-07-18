class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
        return nums















# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         count = nums.count(0)
#         nums[:] = [num for num in nums if num != 0]
#         nums.extend([0] * count)
