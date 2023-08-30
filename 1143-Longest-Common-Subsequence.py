class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2d DP
        # m, n = len(text1), len(text2)
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i+1][j+1] = 1 + dp[i][j] if text1[i] == text2[j] else max(dp[i+1][j], dp[i][j+1])
        # return dp[-1][-1]

        # memory save
        m, n = len(text1), len(text2)
        dp = [0] * (n+1)
        for i in range(m):
            temp = 0
            for j in range(n):
                val = 1 + temp if text1[i] == text2[j] else max(dp[j], dp[j+1])
                temp = dp[j+1]
                dp[j+1] = val
        return dp[-1]

        
