class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # d = {}
        # for e in arr:
        #     d[e] = d.get(e, 0) + 1
        
        # return len(set(d.values())) == len(d.values())

        d = Counter(arr)
        return len(set(d.values())) == len(d.values())


