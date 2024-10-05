class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        first, last = 0, n-1
        result = 0

        # set a target sum
        skill_total = skill[first] + skill[last]

        while first < last:
            if skill[first] + skill[last] == skill_total:

                # Add their product to the result
                result += skill[first] * skill[last]
                first += 1
                last -= 1
            else:
                return -1

        return result


# Time Complexity: O(n logn n)
# Space Complexity: O(1)



            

            
        