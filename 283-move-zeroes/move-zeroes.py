class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = [num for num in nums if num!= 0]
        # temp += [0] * (len(nums) - len(temp))        
        # nums[:] = temp

        # leave zero as where they are, just shift non zero to the left by traversing right pointer

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums


        