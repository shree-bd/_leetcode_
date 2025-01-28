class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            #  Update current_sum to include the current number
            # or start a new subarray at the current number
            curr_sum = max(nums[i], curr_sum + nums[i])

            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, curr_sum)

        return max_sum
        