class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = {}
        for i, w in enumerate(wordsDict):
            self.dict[w] = self.dict.get(w, []) + [i]

    def shortest(self, word1: str, word2: str) -> int:
        ans = float('inf')
        idx1, idx2 = self.dict[word1], self.dict[word2]
        i, j = 0, 0
        while i < len(idx1) and j < len(idx2):
            ans = min(ans, abs(idx1[i] - idx2[j]))
            if idx1[i] < idx2[j]:
                i += 1
            else:
                j += 1
        return ans



        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
