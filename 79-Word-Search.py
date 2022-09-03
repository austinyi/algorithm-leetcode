class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        cur = set()
    
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            if board[r][c] != word[i] or (r,c) in cur:
                return False
            
            cur.add((r,c))
            ans = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            cur.remove((r,c))
            
            return ans
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
