class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(d[i][0])

        return ans
        
        # d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        # return list(d.keys())[:k]
