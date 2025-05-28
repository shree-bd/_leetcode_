class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if abs(three_sum - target) < abs(closest - target):
                    closest = three_sum

                if three_sum < target:
                    l += 1
                elif three_sum > target:
                    r -= 1
                else:
                    return three_sum  # exact match

        return closest