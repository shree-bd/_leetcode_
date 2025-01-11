class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob, rob2, n, n+1, ....]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2




        # if nums is None:
        #     return 0

        # return recurse(nums, 0, 0)

        # def recurse(nums, index, earnings):
        #     # Base Case
        #     if (index >= len(nums)):
        #         return earnings

        #     # Do not rob
        #     case 1 = recurse(nums, index + 1, earnings)

        #     # Rob 
        #     case 2 = recurse(nums, index + 2, earnings + nums[index])

        #     return max(case 1, case 2)
    
        