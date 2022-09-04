'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        a, b = max(m,n) - 1, min(m,n) - 1
        for i in range(a+b, a, -1):
            ans *= i
        for j in range(1,b+1):
            ans /= j
        return int(ans)
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(m-1):
            for j in range(1, n):
                res[j] += res[j-1]
        return res[-1]
