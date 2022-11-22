class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        
        matSum = [[0]*n for _ in range(m)]
       
        for i in range(m-1, -1, -1):
            rowCount = 0
            for j in range(n-1, -1, -1):
                rowCount += pizza[i][j] == "A"
                matSum[i][j] = matSum[i+1][j] + rowCount if i < m-1 else rowCount 
        
        M = 10**9 + 7
        
        @lru_cache(None)

        def dp(i, j, k):
            if matSum[i][j] < k: 
                return 0
            if k == 1 : 
                return 1
            ans = 0

            for r in range(i+1, m):
                if matSum[i][j] - matSum[r][j] > 0:
                    ans += dp(r, j, k-1)

            for c in range(j+1, n): 
                if matSum[i][j] - matSum[i][c] > 0:
                    ans += dp(i, c, k-1)
            return ans % M
        return dp(0, 0, k)
