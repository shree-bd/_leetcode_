class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # final_count = defaultdict(int)
        # result = 0

        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         product = nums[i] * nums[j]
        #         result += final_count[product] * 8
        #         final_count[product] += 1

        # return result


        final_count = {}  # Dictionary to store product frequencies
        result = 0

        # Generate all pairs and calculate their product
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                
                # If the product already exists, calculate the tuples
                if product in final_count:
                    result += 8 * final_count[product]  # 8 = 4 permutations * 2 pairs
                    final_count[product] += 1
                else:
                    final_count[product] = 1

        return result