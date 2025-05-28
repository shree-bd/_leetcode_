"""
LeetCode Problem: 1 Two Sum
"""

from typing import List
"""
LeetCode Problem: 1 Two Sum
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None

        hashMap = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i

        return []

        
        