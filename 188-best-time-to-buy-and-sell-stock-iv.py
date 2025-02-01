# Idea from 123-best-time-to-buy-and-sell-stock-iii
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float('-inf') for _ in range(k+1)]
        sell = [0 for _ in range(k+1)]

        for price in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)
        
        return sell[-1]
