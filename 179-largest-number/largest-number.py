class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        # 3 30 : 330 > 303
        nums.sort(key=lambda x:x*10, reverse=True)

        large_num = ''.join(nums)

        return '0' if large_num[0] == '0' else large_num


        