class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = dict()
        ans = 0
        
        for w in words:
            if w in d and d[w] > 0:
                d[w] -= 1
                ans += 4
            else:
                d[w[::-1]] = d.get(w[::-1], 0) + 1
                
        for w in d:
            if w == w[::-1] and d[w] > 0:
                ans += 2
                break
                
        return ans
                
        
        '''
        counter, ans = [ [0]*26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if counter[b][a]:
                ans += 4
                counter[b][a] -= 1
            else:
                counter[a][b] += 1
        
        i = 0
        while i < 26:
            if counter[i][i] > 0:
                ans += 2
                break
            i += 1
        return ans
        
        '''
