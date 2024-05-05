class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            max_profit = max(max_profit, price - lowest)
        return max_profit