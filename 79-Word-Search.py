class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()

        def dfs(r, c, cur):
            if cur == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            if board[r][c] != word[cur] or (r, c) in path:
                return False
            path.add((r, c))
            res = dfs(r+1, c, cur+1) or dfs(r, c+1, cur+1) or dfs(r-1, c, cur+1) or dfs(r, c-1, cur+1)
            path.remove((r, c))
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
