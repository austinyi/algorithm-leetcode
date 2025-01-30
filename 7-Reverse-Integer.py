class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        while x > 0:
            ans = 10*ans + x % 10
            x //= 10
            if ans > 2**31 -1:
                return 0
        
        return ans*sign
        
