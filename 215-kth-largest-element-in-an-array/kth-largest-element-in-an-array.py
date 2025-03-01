# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         min_heap = []

#         for num in nums:
#             heapq.heappush(min_heap, num)
#             if len(min_heap) > k:
#                 heapq.heappop(min_heap)

#         return min_heap[0]  # The top of the min-heap is the Kth largest

# Time Complexity: O(N log k)
# Space Complexity: O(k)


# >>>>>>>>>>>>>>> USING MAX-HEAP <<<<<<<<<<<<<<<<

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k):
            kth_largest = -heapq.heappop(max_heap)
        
        return kth_largest

# Time Complexity: O(N log k)
# Space Complexity: O(k)