class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # {index, curr_sum} -> num of ways

        def backtrack(i, curr_sum):
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            if i == len(nums):
                return 1 if curr_sum == target else 0

            dp[(i, curr_sum)] = (
                backtrack(i + 1, curr_sum + nums[i]) + 
                backtrack(i+1, curr_sum - nums[i])
            )
            return dp[(i, curr_sum)]
        return backtrack(0, 0)
        