class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            
        cur, tar = 0, len(countT)
        res, minlen = [], len(s) + 1
        
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                cur += 1

            while cur == tar:
                if r-l+1 < minlen:
                    res = [l, r]
                    minlen = min(r-l+1, minlen)
                if s[l] in countT and countT[s[l]] == window[s[l]]:
                    cur -= 1
                window[s[l]] -= 1
                l += 1         

        return s[res[0]:res[1]+1] if minlen != len(s) + 1 else ""
    
