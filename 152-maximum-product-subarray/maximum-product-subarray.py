class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        left_product, right_product = 0, 0
        max_product = nums[0]

        for i in range(n):
            left_product = (1 if left_product == 0 else left_product) * nums[i]
            right_product = (1 if right_product == 0 else right_product) * nums[n - i - 1]

            max_product = max(max_product, left_product, right_product)
        
        return max_product
        # if not nums:
        #     return 0

        # max_prod = nums[0]
        # curr_max, curr_min = 1, 1

        # for n in nums:
        #     if n == 0:
        #         curr_max, curr_min = 1, 1
        #         max_prod = max(max_prod, 0)
        #         continue

        #     tmp = curr_max * n
        #     curr_max = max(tmp, n * curr_min, n)
        #     curr_min = min(tmp, n * curr_min, n)
            
        #     max_prod = max(max_prod, curr_max)


        # return max_prod
        

# Time Complexity: O(n)
# Space Complexity: O(1)
