class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)<2:
            return 0


        # in itliaze the 
        buy1 = float("inf")
        sell1 = 0
        buy2 = float("inf")
        sell2 =0

        for price in prices:
            buy1 = min(buy1, price)

            sell1 = max(sell1, price - buy1)

            buy2 = min(buy2, price-sell1)
            sell2 = max(sell2, price-buy2)

        return sell2


        



"""
sell firts bu later

"""



