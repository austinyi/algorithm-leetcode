from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {} # count = defaultdict(int)
        ans = 0
        l = 0

        for r, n in enumerate(nums):
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            while count[n] > k:
                count[nums[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
            
        return ans


