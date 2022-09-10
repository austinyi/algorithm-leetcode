class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        for i, c in enumerate(pivot):
            for d in range(1, len(strs)):
                if len(strs[d]) <= i or strs[d][i] != c:
                    return pivot[:i]
        return pivot
  
  
# Faster solution  
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = min(strs, key = len)
        for i, c in enumerate(pivot):
            for d in strs:
                if d[i] != c:
                    return pivot[:i]
        return pivot
