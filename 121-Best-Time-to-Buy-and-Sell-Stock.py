class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxPro = 0
        for r in prices:
            if r > l:
                maxPro = max(maxPro, r - l)
            else:
                l = r
        return maxPro
