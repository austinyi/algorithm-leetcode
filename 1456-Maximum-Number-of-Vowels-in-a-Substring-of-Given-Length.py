class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = 0
        for i in range(k):
            if s[i] in 'aeiou':
                cur += 1 
        ans = cur
        for i in range(k, len(s)):
            if s[i-k] in 'aeiou':
                cur -= 1
            if s[i] in 'aeiou':
                cur += 1
                ans = max(ans, cur)
        return ans
            
