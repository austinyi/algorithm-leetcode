class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])):
            cur = i
            j = 0
            while j < len(grid):
                if grid[j][cur] == 1:
                    cur += 1
                    if cur < len(grid[0]) and grid[j][cur] == 1:
                        j += 1
                        continue
                    else:
                        break
                else:
                    cur -= 1
                    if cur >= 0 and grid[j][cur] == -1:
                        j += 1
                        continue
                    else:
                        break         
                    
          
            #print(j)
            if j == len(grid):
                ans.append(cur)
            else:
                ans.append(-1)
                
        return ans
        
