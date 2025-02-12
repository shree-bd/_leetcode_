class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        sum_map = {}

        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10  # Extract last digit
                n //= 10  # Remove last digit
            return s

        for num in nums:
            d_sum = digit_sum(num)

            if d_sum in sum_map:
                max_sum = max(max_sum, sum_map[d_sum] + num)
                sum_map[d_sum] = max(sum_map[d_sum], num)  # Keep max num for this sum
            else:
                sum_map[d_sum] = num  # First occurrence of this sum

        return max_sum

        

