class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        array = []
        n = len(nums) + 1
        for i in range(1,n):
            if i not in set_nums:
                array.append(i)
        return array
                
        

                