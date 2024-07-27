class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize variables
        res = nums[k]
        cur_min = nums[k]
        left = right = k
        
        # Expand both to the left and right
        while left >= 0 and right < len(nums):
            # Update the minimum value in the current subarray
            cur_min = min(cur_min, nums[left], nums[right])
            
            # Calculate the score
            score = cur_min * (right - left + 1)
            
            # Update the result
            res = max(res, score)
            
            # Determine where to expand
            if left == 0 and right == len(nums) - 1:
                break
            if left > 0 and (right == len(nums) - 1 or nums[left - 1] >= nums[right + 1]):
                left -= 1
            else:
                right += 1
        
        return res