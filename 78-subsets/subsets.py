# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []

#         def backtrack(start, subset):
#             result.append(subset[:])

#             for i in range(start, len(nums)):
#                 subset.append(nums[i])
#                 backtrack(i+1, subset)
#                 subset.pop()

#         backtrack(0,[])
#         return result

# Time Complexity: O(2^N)
# Space Complexity: O(N)   

# Iterative approach
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            result += [subset + [num] for subset in result]
        
        return result