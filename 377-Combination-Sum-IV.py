# Dynamic Programming
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num: 
                    dp[i] += dp[i - num]
        
        return dp[-1]

'''
# Backtracking (Time Limit Exceeded)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(nums, target):
            ans = 0
            if target == 0:
                return 1
            elif target < 0:
                return 0
            for i in range(len(nums)):
                ans += dfs(nums, target - nums[i])
            return ans

        return dfs(nums, target)
 '''

