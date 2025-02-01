class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        cur_min = prices[0]
        for price in prices[1:]:
            ans = max(ans, price - cur_min)
            if price < cur_min:
                cur_min = price
        return ans
