class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        # g = gcd(oneGroup, zeroGroup)
        # if g != 1:
        #     return self.goodBinaryStrings(math.ceil(minLength / g), maxLength // g, oneGroup // g, zeroGroup // g)
        # dp = [0] * (maxLength + 1)
        # dp[0] = 1
        
        # for i in range(min(oneGroup,zeroGroup), max(oneGroup,zeroGroup)):
        #     if dp[i-min(oneGroup,zeroGroup)] > 0:
        #         dp[i] += dp[i-min(oneGroup,zeroGroup)]
        
        # for i in range(max(oneGroup,zeroGroup), maxLength + 1):
        #     dp[i] += dp[i-oneGroup] + dp[i-zeroGroup]

        # return sum(dp[minLength:]) % 1000000007

        # dp = [0] * (maxLength + 1)
        # dp[0] = 1
        # MOD = 1_000_000_007
        # for i in range(maxLength + 1):
        #     if dp[i]:
        #         if i + oneGroup <= maxLength:
        #             dp[i + oneGroup] = (dp[i] + dp[i + oneGroup]) % MOD
        #         if i + zeroGroup <= maxLength:
        #             dp[i + zeroGroup] = (dp[i] + dp[i + zeroGroup]) % MOD
        # return sum(dp[minLength:]) % MOD

        g = gcd(oneGroup, zeroGroup)
        if g != 1:
            return self.goodBinaryStrings(math.ceil(minLength / g), maxLength // g, oneGroup // g, zeroGroup // g)
        m1 = max(oneGroup, zeroGroup)
        m2 = min(oneGroup, zeroGroup)
        dp = [0] * m1
        dp[0] = 1
        ans = 0
        for i in range(m2, m1):
            dp[i] = dp[i-m2]
            if i >= minLength:
                ans += dp[i % m1]
        
        for i in range(m1, maxLength + 1):
            dp[i % m1] = dp[(i-oneGroup) % m1] + dp[(i-zeroGroup) % m1]
            if i >= minLength:
                ans += dp[i % m1]

        return ans % 1000000007
