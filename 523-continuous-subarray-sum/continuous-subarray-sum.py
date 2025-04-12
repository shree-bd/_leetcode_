class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0 : -1}     # maps remainder -> end index
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            mod  = prefix_sum if k==0 else prefix_sum % k

            if mod not in mod_map:
                mod_map[mod] = i
            elif i - mod_map[mod] > 1:
                    return True

        return False

# Time Complexity: O(N) | Space Complexity: O(N)