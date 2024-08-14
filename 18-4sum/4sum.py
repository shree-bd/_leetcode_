class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = set()  # Use a set to avoid duplicate quadruplets
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for j
                    continue
                
                l, r = j + 1, len(nums) - 1
                while l < r:
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                        # Skip duplicates for l and r
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sum_ < target:
                        l += 1
                    else:
                        r -= 1
        
        return list(result)




        