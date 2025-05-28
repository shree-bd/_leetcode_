class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2

        #step 1: find first decreaaing from end
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            #step 2: find nunnber just larger than nums[i]
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            #step 3: swap
            nums[i] , nums[j] = nums[j], nums[i]

        # step 4: reverse from i+1 to end
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

# TC: O(N) | SC: O(1)

        

        