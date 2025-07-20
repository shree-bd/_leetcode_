class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit