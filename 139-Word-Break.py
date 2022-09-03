'''
# Recursive, very slow, time limit exceeded
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        for word in wordDict:
            if len(s) >= len(word) and word == s[:len(word)]:
                if self.wordBreak(s[len(word):], wordDict):
                    return True
        return False
'''

# Dynamic Programming
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w) <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
