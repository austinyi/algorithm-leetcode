class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        ans = 0
        for n in nums:
            if d.get(k-n, 0) == 0:
                d[n] = 1 + d.get(n, 0)
            else:
                d[k-n] = d.get(k-n) - 1
                ans += 1
        return ans

        # ans = 0
        # d = {}
        # for n in nums:
        #     d[n] = d.get(n,0) + 1
        
        # for i in d:
        #     ans += min(d[i], d.get(k-i,0))
        # return ans // 2
