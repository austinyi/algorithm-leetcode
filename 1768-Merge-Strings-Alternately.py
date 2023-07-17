class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i = 0 

        if len(word1) == len(word2):
            while i < len(word1):
                ans += (word1[i] + word2[i])
                i += 1
        elif len(word1) > len(word2):
            while i < len(word2):
                ans += (word1[i] + word2[i])
                i += 1
            ans += word1[i:]
        else:
            while i < len(word1):
                ans += (word1[i] + word2[i])
                i += 1
            ans += word2[i:]

        return ans
        
