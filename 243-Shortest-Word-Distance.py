class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        cur = -1
        find = 0
        ans = float("inf")
        for i, w in enumerate(wordsDict):
            if w == word1:
                if find == 2:
                    ans = min(ans, i - cur)
                find = 1
                cur = i
            elif w == word2:
                if find == 1:
                    ans = min(ans, i - cur)
                find = 2
                cur = i
        
        return ans
