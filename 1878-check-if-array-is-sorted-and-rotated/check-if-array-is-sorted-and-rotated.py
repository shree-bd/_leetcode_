class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count_breaks = 0

        for i in range(N):
            if nums[i] > nums[(i+1) % N]:
                count_breaks += 1

            if count_breaks > 1:
                return False

        return True

# Time Complexity: O(N)
# Space Complexity: O(1)