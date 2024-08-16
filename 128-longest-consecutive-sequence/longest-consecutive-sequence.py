class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest = 0


        for num in nums_set:
            if num-1 not in nums_set: #start of a new sequence
                curr_num = num
                curr_cnt = 1


                while curr_num+1 in nums_set:
                    curr_num += 1
                    curr_cnt += 1

                longest = max(longest,curr_cnt)

        return longest


        