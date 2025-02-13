class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # convert nums into min-heap           
        res = 0
        
        # If there are fewer than 2 elements, no operation can be performed
        if len(nums) < 2:
            return 0
        
        while nums[0] < k:
            x = heapq.heappop(nums) # first min num
            y = heapq.heappop(nums) # second min num

            new_val = x * 2 + y
            heapq.heappush(nums, new_val) # push the new value back

            res += 1

        return res


# Time Complexity: O(N log N)
# Space Complexity: O(N)