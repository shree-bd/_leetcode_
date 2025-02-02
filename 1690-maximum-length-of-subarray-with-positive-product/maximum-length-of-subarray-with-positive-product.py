class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = 0
        result = 0 # Initialize result to track the maximum length

        for num in nums:
            if num > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0 # oNly update neg if it exists
            elif num < 0:
                pos, neg  = 1 + neg if neg > 0 else 0, 1 + pos  # swap pos & neg logic
            else:
                pos = neg = 0    # reset on encountering zero

            result = max(result, pos)   # update result

        return result

