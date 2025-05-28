class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(left, right):
            pivot = nums[right]

            l, r = left, right

            while l<=r:
                if nums[l] < pivot:
                    l += 1
                elif nums[r] > pivot:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    l, r = l + 1, r - 1

            if k <= r:
                return quickselect(left, r)
            if k >= l:
                return quickselect(l, right)
            return nums[k]

        return quickselect(0, len(nums)-1)

            
             





        """
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
        """




        """
        k = len(nums) - k  # Find kth largest by finding (n-k)th smallest

        def quickselect(left, right):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p > k: return quickselect(l, p-1)
            elif p < k: return quickselect(p+1, r)
            else: return nums[p]

        return quickselect(0, len(nums) - 1)
        """
        


        