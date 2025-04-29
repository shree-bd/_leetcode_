class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)

        max_heap = [(-freq,num) for num, freq in hash_map.items()]
        heapq.heapify(max_heap)

        res = []

        for _ in range(k):
            freq, num = heapq.heappop(max_heap)
            res.append(num)

        return res

        