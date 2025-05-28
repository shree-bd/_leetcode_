class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            if start == len(nums):
                return result.append(nums[:])

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  #swap
                backtrack(start+1)  #reursion for next index
                nums[start], nums[i] = nums[i], nums[start] #undo swap

        backtrack(0)
        return result

# Time Complexity: O(n!)
# Space Complexity: O(n * n!)
        
        