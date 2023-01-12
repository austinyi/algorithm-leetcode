class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def factor(n, i, cur, res):
            while i * i <= n:
                if n % i == 0:
                    res.append(cur + [i, n//i])
                    factor(n//i, i, cur + [i], res)
                i += 1
            return res
        return factor(n, 2, [], [])
