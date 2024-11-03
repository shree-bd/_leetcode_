class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half_len - i

            # Check boundary conditions
            max_left_1 = nums1[i - 1] if i > 0 else float('-infinity')
            min_right_1 = nums1[i] if i < m else float('infinity')
            max_left_2 = nums2[j - 1] if j > 0 else float('-infinity')
            min_right_2 = nums2[j] if j < n else float('infinity')

            # Check if valid partition
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(max_left_1, max_left_2)
                else:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
            elif max_left_1 > min_right_2:
                right = i - 1
            else:
                left = i + 1

        # In case input arrays are not sorted or some error occurs
        return -1


        

        