class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for i in d:
            if d[i] % 2 != 0:
                return False
        return True
