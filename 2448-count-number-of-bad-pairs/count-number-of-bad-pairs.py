class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total_pairs = len(nums) * (len(nums) - 1) // 2  # Total number of pairs
        good_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            key = nums[i] - i  # Store the difference
            good_pairs += count[key]
            count[key] += 1

        return total_pairs - good_pairs

# Time Complexity: O(N)
# Space Complexity: O(N)
        