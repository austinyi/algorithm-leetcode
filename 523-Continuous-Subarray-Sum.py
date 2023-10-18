class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        cur = 0
        if len(nums) == 1:
            return False
        
        for i, n in enumerate(nums):
            cur += n
            cur %= k
            if cur in prefix:
                if i - prefix[cur] > 1:
                    return True
            else:
                prefix[cur] = i
        return False
