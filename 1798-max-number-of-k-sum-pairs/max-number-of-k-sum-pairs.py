# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         n = len(nums)

#         first,last = 0, n-1
#         count = 0

#         while first < last:
#             if nums[first] + nums[last] == k:
#                 first += 1
#                 last -= 1
#                 count += 1
#             elif nums[first] + nums[last] < k:
#                 first += 1
#             else:
#                 last -= 1
#         return count
        
# Time Complexity: O(n long n)
# Space Complexity: O(n)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Optimal Solution using hashMap
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_count = defaultdict(int)

        for num in nums:
            complement = k - num

            if num_count[complement] > 0:
                count += 1
                num_count[complement] -= 1
            else:
                num_count[num] += 1
        return count
        
