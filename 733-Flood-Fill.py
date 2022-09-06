class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
                    
        m, n = len(image), len(image[0])
        col = image[sr][sc]

        if col == color:
            return image
        
        def dfs(r,c):
            if image[r][c] == col:
                image[r][c] = color
                if r > 0: dfs(r-1,c)
                if r < m-1: dfs(r+1,c)
                if c > 0: dfs(r,c-1)
                if c < n-1: dfs(r,c+1)

        dfs(sr, sc)
        return image
