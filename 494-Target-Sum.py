class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If target is invalid, return 0
        if (total + target) % 2 == 1 or abs(target) > total:
            return 0 
        
        new_target = (total + target) // 2
        
        # Initialize DP array
        # dp[index][sum]: represents the number of ways to reach the sum using the first index numbers.
        dp = [0] * (new_target + 1)
        dp[0] = 1  # One way to achieve 0 (use no numbers)

        for i in range(len(nums)): 
            for j in range(new_target, nums[i] - 1, -1): 
                dp[j] += dp[j - nums[i]]

        # Return result from the last row
        return dp[new_target]


        # memo = {}

        # def dp(i, cur):
        #     if (i, cur) in memo:
        #         return memo[(i, cur)]
        #     if i == len(nums):
        #         if cur == target:
        #             return 1
        #         else:
        #             return 0

        #     memo[(i, cur)] = dp(i+1, cur+nums[i]) + dp(i+1, cur-nums[i])
        #     return memo[(i, cur)]
            
        # return dp(0, 0)
