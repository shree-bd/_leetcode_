class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        final_count = defaultdict(int)
        result = 0

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                result += final_count[product] * 8
                final_count[product] += 1

        return result