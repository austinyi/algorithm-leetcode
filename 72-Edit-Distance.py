# https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/?envType=study-plan-v2&envId=leetcode-75 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2d DP
        # m, n = len(word1), len(word2)
        # dp = [[0] * (n+1) for _ in range(m+1)]

        # for i in range(1, m+1):
        #     dp[i][0] = i
        # for j in range(1, n+1):
        #     dp[0][j] = j
        
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
        
        # return dp[-1][-1]

        # m, n = len(word1), len(word2)
        # dp = list(range(n+1))
        
        # for i in range(1, m+1):
        #     prev, cur = i-1, i
        #     dp[0] = i
        #     for j in range(1, n+1):
        #         temp = prev
        #         prev = dp[j]
        #         if word1[i-1] == word2[j-1]:
        #             dp[j] = temp
        #         else:
        #             dp[j] = 1 + min(cur, temp, prev)
        #         cur = dp[j]
                
        # return dp[-1]

        # MEMORY SAVE 1d DP
        m, n = len(word1), len(word2)
        dp = list(range(n+1))
        
        for i in range(1, m+1):
            prev = i-1
            dp[0] = i
            for j in range(1, n+1):
                temp, prev = prev, dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = temp
                else:
                    dp[j] = 1 + min(dp[j-1], temp, prev)

        return dp[-1]
