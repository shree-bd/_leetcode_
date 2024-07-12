class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []
        n = len(nums)
        for i in range(n//2):
            minElement = nums[i]
            maxElement = nums[n-1-i]
            averages.append((minElement+maxElement)/2)

        return min(averages)

        