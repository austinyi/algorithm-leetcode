class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, pair2):
        if self.count == pair2.count:
            return self.word < pair2.word
        return self.count < pair2.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        
        q = []
        heapq.heapify(q)
        for word, count in counts.items():
            heapq.heappush(q, Pair(word, -count))
            
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(q).word)
            
        return ans
