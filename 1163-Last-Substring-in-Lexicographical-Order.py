# Fastest solution with O(n) time and O(1) space
### https://leetcode.com/problems/last-substring-in-lexicographical-order/solutions/363662/short-python-code-o-n-time-and-o-1-space-with-proof-and-visualization/?orderBy=most_votes
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j = j + k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return s[i:]

# My Slow solution
class Solution:
    def lastSubstring(self, s: str) -> str:
        c = ""
        idx = []
        for i in range(len(s)):
            if s[i] > c:
                c = s[i]
                idx = [i]
            elif s[i] == c:
                idx.append(i)

        maxStr = ""
        for i in idx:
            if s[i:] > maxStr:
                maxStr = s[i:]
        return maxStr

# Very slow solution
class Solution:
    def lastSubstring(self, s: str) -> str:
        maxStr = ""
        for i in range(len(s)):
            if s[i:] > maxStr:
                maxStr = s[i:]
        return maxStr
