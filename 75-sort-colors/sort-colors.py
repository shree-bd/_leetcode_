class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0

        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i -= 1
            i += 1

        return nums

# Time Complexity: O(N)
# Space Complexity: O(1)




