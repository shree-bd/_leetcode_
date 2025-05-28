"""
LeetCode Problem: 2581 Divide Players Into Teams Of Equal Skill
"""

from typing import List
"""
LeetCode Problem: 2581 Divide Players Into Teams Of Equal Skill
"""

# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         skill.sort()
#         n = len(skill)
#         first, last = 0, n-1
#         result = 0

#         # set a target sum
#         skill_total = skill[first] + skill[last]

#         while first < last:
#             if skill[first] + skill[last] == skill_total:

#                 # Add their product to the result
#                 result += skill[first] * skill[last]
#                 first += 1
#                 last -= 1
#             else:
#                 return -1

#         return result


# Time Complexity: O(n logn n)
# Space Complexity: O(1)


# ***********************************************************************
            
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Create a frequency count of the skill levels
        skill_count = Counter(skill)
        result = 0
        
        # Step 2: Calculate the target sum of each pair
        target_sum = max(skill) + min(skill)
        
        # Step 3: Iterate over each unique skill level
        for skill_value, count in skill_count.items():
            # Find the complementary skill level for the pair
            complement = target_sum - skill_value
            
            # Handle edge case when both players have the same skill level
            if complement == skill_value and count % 2 != 0:
                return -1  # Odd count of players with the same skill
            
            # If the complement doesn't exist or if counts don't match, return -1
            if complement not in skill_count or skill_count[complement] != count:
                return -1
            
            # Add the product of skill_value and complement to the result
            result += count * skill_value * complement
        
        # Since we counted each pair twice, divide the result by 2
        return result // 2
            
        