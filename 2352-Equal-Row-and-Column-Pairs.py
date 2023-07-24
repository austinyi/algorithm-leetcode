class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        cnt = Counter([tuple(row) for row in grid])
        for col in zip(*grid):
            ans += cnt.get(tuple(col), 0)
        return ans


        
