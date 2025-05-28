class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(first_num):
            left, right = 0, len(nums)-1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if first_num:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]








        """
        first = last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
        """
        