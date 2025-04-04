class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        cnt = 0
        hash_map = {0:1}

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            cnt += hash_map.get(diff, 0)
            hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
        return cnt



        # result = 0
        # curr_sum = 0

        # # Dictionary to store prefix sums and their counts
        # # Starts with {0: 1} to handle the case where a subarray starting from the beginning equals k
        # prefix_sums = {0:1}

        # # Iterate over each number in the array
        # for n in nums:
        #     curr_sum += n
        #     diff = curr_sum - k
            
            
        #     # If the difference exists in prefix_sums, add its count to the result
        #     # This means there are 'prefix_sums[diff]' subarrays that end at the current index and sum to k
        #     result += prefix_sums.get(diff, 0)
        #     prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)


        # return result
