"""
LeetCode Problem: 378 Kth Smallest Element In A Sorted Matrix
"""

from typing import List
"""
LeetCode Problem: 378 Kth Smallest Element In A Sorted Matrix
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = [num for row in matrix for num in row]
        flat.sort()
        return flat[k-1]

        
        