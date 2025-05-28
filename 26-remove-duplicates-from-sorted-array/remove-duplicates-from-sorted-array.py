class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0 

        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                left += 1
                nums[left] = nums[right]

        return left + 1

# T.C: O(N) | S.C - O(1)

        