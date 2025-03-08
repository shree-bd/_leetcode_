class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = [num for num in nums if num!= 0]
        temp += [0] * (len(nums) - len(temp))
        
        nums[:] = temp
        