class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cur = curmax = prices[0]
        # ans = 0
        # for i in range(1, len(prices)):
        #     if prices[i] < curmax:
        #         ans += curmax - cur
        #         cur = curmax = prices[i]
        #     else:
        #         curmax = prices[i]
        # return ans + curmax - cur

        ans = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                ans += prices[i+1] - prices[i]
        return ans
