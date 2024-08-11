class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        
        # Step 2: Use a heap to find the top k frequent elements
        # We use a min-heap to keep track of the top k elements
        # heapq.nlargest returns the k largest elements based on the frequency count
        return [item for item, freq in heapq.nlargest(k, countMap.items(), key=lambda x: x[1])]

