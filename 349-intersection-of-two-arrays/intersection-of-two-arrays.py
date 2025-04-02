class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return list(nums1_set & nums2_set)
        
# Time Complexity: O(M+N)
# Space Complexity: O(M+N)