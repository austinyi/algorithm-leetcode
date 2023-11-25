class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        ans = 0
        for c in count:
            if count[c] > 1:
                ans += count[c]*(count[c]-1)/2
        return int(ans)
