class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        store = set()
        
        for c in s:
            if c in store:
                ans += 2
                store.remove(c)
            else:
                store.add(c)
        if store:
            ans += 1
        return ans
