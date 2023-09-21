class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ans = [1] * len(nums)
        m = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        ans[i] = ans[j]
                    elif dp[j] + 1 == dp[i]:
                        ans[i] += ans[j]
            m = max(m, dp[i])
        cnt = 0
        for i in range(len(nums)):
            if dp[i] == m: cnt += ans[i] 
        return cnt


        

        
