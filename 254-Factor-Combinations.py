class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        def factor(n, i, cur):
            while i * i <= n:
                if n % i == 0:
                    ans.append(cur + [i, n//i])
                    factor(n//i, i, cur + [i])
                i += 1
        factor(n, 2, [])  
        return ans
