class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        Sn = {0:1}

        for i in nums:
            cur += i
            ans += Sn.get(cur - k, 0)

            Sn[cur] = 1 + Sn.get(cur, 0)

        return ans
