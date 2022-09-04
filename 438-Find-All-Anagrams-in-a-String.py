class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p) 
        if n1 < n2:
            return []
        
        ans = []
        pCount = dict()
        cur = dict()
        
        for idx, c in enumerate(p):
            pCount[c] = 1 + pCount.get(c, 0)
            cur[s[idx]] = 1 + cur.get(s[idx], 0)
        
        for i in range(n2, n1):
            if cur == pCount:
                ans.append(i-n2)
            cur[s[i]] = 1 + cur.get(s[i], 0)
        
            if cur[s[i-n2]] == 1:
                # cur.pop(s[i-n2])
                del cur[s[i-n2]]
            else:
                cur[s[i-n2]] -= 1        
        if cur == pCount:
            ans.append(n1-n2)
            
        return ans
