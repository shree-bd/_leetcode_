class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

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



# By using map:

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
        
#         nums_map = {}
#         max_len = 0

#         for num in nums:

#             if num not in nums_map:
#                 nums_map[num] = [num, num]
#                 left = num
#                 right = num
            
#                 # look to extend the sequence [a,b] left or right
#                 if num - 1 in nums_map:
#                     left = nums_map[num-1][0]
                
#                 if num + 1 in nums_map:
#                     right = nums_map[num+1][1]
                
#                 nums_map[left] = [left, right]
#                 nums_map[right] = [left, right]

#                 max_len = max(max_len, right - left + 1)
#         print(nums_map)
#         return max_len
        
        