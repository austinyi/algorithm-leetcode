class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        n = len(grid)
        q = deque()
        q.append((0,0))
        visited = {(0,0)}
        length = 1

        while q:
            l = len(q)
            for _ in range(l):
                r, c = q.popleft()
                
                if r == n-1 and c == n-1:
                    return length
                for dr, dc in [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,0),(1,1),(1,-1)]:
                    if r+dr < n and c+dc < n and r+dr >= 0 and c+dc >= 0 and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in visited:
                        q.append((r+dr, c+dc))
                        visited.add((r+dr,c+dc))
            length += 1
        
        return -1
