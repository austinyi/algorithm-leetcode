class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        m = len(grid)
        n = len(grid[0])
        for i in range(n):
            cur = i
            j = 0
            while j < m:
                if grid[j][cur] == 1:
                    cur += 1
                    if cur < n and grid[j][cur] == 1:
                        j += 1
                    else:
                        break
                else:
                    cur -= 1
                    if cur >= 0 and grid[j][cur] == -1:
                        j += 1
                    else:
                        break         
                
            if j == m:
                ans.append(cur)
            else:
                ans.append(-1)
                
        return ans
    
    
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        def find(i):
            cur = i
            j = 0
            while j < m:
                if grid[j][cur] == 1:
                    cur += 1
                    if cur < n and grid[j][cur] == 1:
                        j += 1
                    else:
                        break
                else:
                    cur -= 1
                    if cur >= 0 and grid[j][cur] == -1:
                        j += 1
                    else:
                        break         
            if j == m:
                return(cur)
            else:
                return(-1)
                
        return [find(i) for i in range(n)]

 
