"""
LeetCode Problem: 907 Koko Eating Bananas
"""

from typing import List
"""
LeetCode Problem: 907 Koko Eating Bananas
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        min_k, max_k = 1, max(piles)

        while min_k < max_k:
            mid_k = min_k + ((max_k-min_k)//2)

            total_hours = sum(math.ceil(pile/mid_k) for pile in piles)

            if total_hours > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k 
        
        return min_k                



        