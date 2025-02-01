class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize four state variables
        buy1, buy2 = float('-inf'), float('-inf')  # Negative infinity since we are "spending" money
        sell1, sell2 = 0, 0  # Profits initialized to zero

        # Iterate over each day's stock price
        for price in prices:
            buy1 = max(buy1, -price)        # Max profit after first buy
            sell1 = max(sell1, buy1 + price) # Max profit after first sell
            buy2 = max(buy2, sell1 - price)  # Max profit after second buy
            sell2 = max(sell2, buy2 + price) # Max profit after second sell

        return sell2  # Final maximum profit after at most two transactions

# 1. Time Exceed
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0]*len(prices) for _ in range(3)]
        # for i in range(1, 3):
        #     for j in range(1, len(prices)):
        #         dp[i][j] = dp[i][j-1]
        #         for k in range(j):
        #             if k == 0:
        #                 dp[i][j] = max(dp[i][j], prices[j] - prices[k])
        #             else:
        #                 dp[i][j] = max(dp[i][j], dp[i-1][k-1] + prices[j] - prices[k])
        # return dp[2][-1]

# 2. Better than 1. removing loop for k
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0]*len(prices) for _ in range(3)]
        # for i in range(1, 3):
        #     max_temp = -float('inf')
        #     for j in range(1, len(prices)):
        #         if j > 1:
        #             dp[i][j] = max(dp[i][j-1], max_temp + prices[j])
        #         dp[i][j] = max(dp[i][j], prices[j] - prices[0])
        #         max_temp = max(max_temp, dp[i-1][j-1] - prices[j])
        # return dp[2][-1]



