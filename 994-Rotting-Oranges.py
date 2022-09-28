class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        fresh = 0
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        while q and fresh > 0:
            ans += 1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if 0 <=  r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        q.append((r + dr, c + dc))
            
        if fresh > 0:
            return -1
        else:
            return ans
        
                        
