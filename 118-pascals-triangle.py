class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        
        for i in range(1, numRows):
            cur = [1]
            for j in range(i-1):
                cur.append(ans[-1][j] + ans[-1][j+1])
            cur.append(1)
            ans.append(cur)
        return ans
