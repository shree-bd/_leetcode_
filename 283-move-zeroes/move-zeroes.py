class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # temp = [num for num in nums if num!= 0]
        # temp += [0] * (len(nums) - len(temp))        
        # nums[:] = temp

        # leave zero as where they are, just shift non zero to the left by traversing right pointer

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


# Time Complexity: O(N)
# Space Complexity: O(1)
        