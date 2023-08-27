class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = [0, 0]
        for i, n in enumerate(nums):
            ans[i % 2] = max(ans[i % 2] + n, ans[(i-1) % 2])
        
        return ans[(len(nums)-1) % 2]
