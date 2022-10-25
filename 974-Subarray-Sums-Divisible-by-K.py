class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        d = {0:1}
        
        for i, n in enumerate(nums):
            cur += n
            cur %= k

            temp = cur % k
            ans += d.get(temp, 0)

            d[cur] = d.get(cur, 0) + 1

        return ans


