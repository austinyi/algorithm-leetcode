class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        cur = {}
        curMax = 0   
            
        for r in range(len(s)):
            cur[s[r]] = 1 + cur.get(s[r], 0)
            curMax = max(curMax, cur[s[r]])
            while r-l+1 - curMax > k:
                cur[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
        
        return ans
