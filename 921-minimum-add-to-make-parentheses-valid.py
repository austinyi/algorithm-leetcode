class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        cur = 0
        for p in s:
            if p == "(":
                cur += 1
            else:
                cur -= 1
                if cur < 0:
                    ans += 1
                    cur += 1
        return ans + cur
