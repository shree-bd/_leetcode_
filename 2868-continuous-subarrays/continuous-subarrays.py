class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = Counter()
        l = 0
        res = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while max(count) - min(count) > 2:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            res += r - l + 1

        return res


        