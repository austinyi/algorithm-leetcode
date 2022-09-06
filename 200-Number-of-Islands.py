class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                if i > 0: dfs(i-1, j)
                if i < m - 1: dfs(i+1, j)
                if j > 0: dfs(i, j-1)
                if j < n - 1: dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans
