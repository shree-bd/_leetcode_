# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()  # Sort the array to make it easier to avoid duplicates and use two-pointer technique
#         result = []
        
#         for i in range(len(nums) - 2):
#             # Skip duplicates
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
            
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]
                
#                 if total < 0:
#                     left += 1
#                 elif total > 0:
#                     right -= 1
#                 else:
#                     result.append([nums[i], nums[left], nums[right]])
#                     # Skip duplicates
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
        
#         return result



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1] or num > 0: continue 

            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                value = nums[l] + nums[r]
                if value == target:
                    ans.add((num, nums[l], nums[r]))
                    l += 1
                elif value > target:
                    r -= 1
                else:
                    l += 1
        return list(ans)