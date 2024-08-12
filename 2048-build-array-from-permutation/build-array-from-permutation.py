class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Encode both the original value and the new value into each element
        for i in range(n):
            # Encode the new value into nums[i]
            nums[i] = nums[i] + (nums[nums[i]] % n) * n
        
        # Step 2: Decode the result
        for i in range(n):
            # Extract the new value by dividing by n
            nums[i] = nums[i] // n
        
        return nums


        """
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
        """
        