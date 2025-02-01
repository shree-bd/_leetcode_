class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_array = []
        dq = collections.deque() # indices
        left = right = 0 

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)


            if left > dq[0]:
                dq.popleft()

            if (right + 1) >= k:
                max_array.append(nums[dq[0]])
                left += 1

            right += 1

        return max_array


            




        