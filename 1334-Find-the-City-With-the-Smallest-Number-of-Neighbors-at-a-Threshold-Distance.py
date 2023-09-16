class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for i, j, w in edges:
            d[i][j] = d[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(i, n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                    d[j][i] = d[i][j]

        ans = 0
        cur = float('inf')
        for i in range(n):
            count = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold:
                    count += 1 
            if count <= cur:
                cur = count
                ans = i
        return ans
        
