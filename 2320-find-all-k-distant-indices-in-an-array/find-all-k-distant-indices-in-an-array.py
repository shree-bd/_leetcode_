class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        res = set()

        key_indices = [i for i, val in enumerate(nums) if val == key]

        for idx in key_indices:
            start = max(0, idx-k)
            end = min(n-1, idx+k)
            for i in range(start, end+1):
                res.add(i)
        return sorted(res)

