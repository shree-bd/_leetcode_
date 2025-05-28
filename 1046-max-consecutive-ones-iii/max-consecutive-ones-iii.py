class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
            max_len = max(max_len, r - l +1)

        return max_len

# Time Complexity: O(N)
# Space Complexity: O(1)




        