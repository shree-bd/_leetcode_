class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        sl = SortedList()
        result = []

        for i in range(len(nums)):
            sl.add(nums[i])

            # Remove the element sliding out of window
            if i >= k:
                sl.remove(nums[i - k])

            # Compute median once window is full
            if i >= k - 1:
                mid = k // 2
                if k % 2 == 1:
                    result.append(float(sl[mid]))
                else:
                    result.append((sl[mid - 1] + sl[mid]) / 2)

        return result
        
# Time Complexity: O(N log K) | Space Complexity: O(K)
# N= no of elemtns in nums | K = window size


"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:




# Time Complexity: O(N * K log K) | Space Complexity: O(K)
# N= no of elemtns in nums | K = window size
"""