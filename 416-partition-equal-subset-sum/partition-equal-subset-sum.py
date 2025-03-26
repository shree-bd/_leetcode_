# using Dyanmic programming
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, we can't split it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        # We need to find a subset with sum equal to total_sum / 2
        target = total_sum // 2
        
        # DP array where dp[i] means whether sum i can be achieved
        dp = [False] * (target + 1)
        dp[0] = True  # We can always make sum 0 with no elements
        
        for num in nums:
            # Traverse backwards to avoid overwriting dp values
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        # If we can achieve target sum, return True
        return dp[target]





# Using recursion - subset sum search

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 != 0:
            return False

        target = total_sum//2

        def canSubset(i, curr_sum):
            if curr_sum == target:
                return True
            if i >= len(nums) or curr_sum > target:
                return False

            #inclide curr_sum or exclude it
            return (canSubset(i+1, curr_sum + nums[i]) or canSubset(i+1, curr_sum))

        return canSubset(0,0)

# Time Complexity: O(2^N)
# Space Complexity: O(N)
        
"""
        