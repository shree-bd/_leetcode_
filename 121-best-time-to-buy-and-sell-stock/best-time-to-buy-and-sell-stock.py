class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit




        # min_price = float("inf")
        # max_profit = 0

        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)

        # return max_profit






        # max_profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[i])

        # return max_profit

