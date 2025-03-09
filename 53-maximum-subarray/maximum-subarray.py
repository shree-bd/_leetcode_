class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])

            max_sum = max(max_sum, curr_sum)
        
        return max_sum


        # curr_sum = 0
        # max_sum = nums[0]

        # for n in nums:
        #     if curr_sum < 0:
        #         curr_sum = 0
        #     curr_sum += n
        #     max_sum = max(max_sum, curr_sum)

        # return max_sum


# Time Complexity: O(n)
# Space Complexity: O(1)