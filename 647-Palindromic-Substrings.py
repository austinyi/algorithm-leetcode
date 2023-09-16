class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                ans += 1
                k = 1
                while i+k+1 < len(s) and i-k >= 0 and s[i+k+1] == s[i-k]:
                    ans += 1
                    k += 1
        for i in range(1, len(s)-1):
            if s[i-1] == s[i+1]:
                ans += 1
                k = 1
                while i+k+1 < len(s) and i-k-1 >= 0 and s[i+k+1] == s[i-k-1]:
                    ans += 1
                    k += 1
        return ans
