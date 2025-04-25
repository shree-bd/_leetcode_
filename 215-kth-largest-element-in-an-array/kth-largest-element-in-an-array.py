class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # Find kth largest by finding (n-k)th smallest

        def quickselect(left, right):
            pivot = nums[random.randint(left, right)]
            l, r = left, right

            while l <= r:
                if nums[l] < pivot:
                    l += 1
                elif nums[r] > pivot:
                    r -= 1
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            if k <= r:
                return quickselect(left, r)
            if k >= l:
                return quickselect(l, right)
            return nums[k]

        return quickselect(0, len(nums) - 1)
        


        