class Solution:
    def mySqrt(self, x: int) -> int:
        # n = 0
        # while n*n <= x:
        #     n += 1
        # return n-1

        if x == 0 or x == 1:
            return x

        l = 1
        r = x
        while l < r:
            m = (r+l) // 2
            
            if m*m < x:
                l = m + 1
            elif m*m > x:
                r = m 
            else:
                return m
        return l - 1
            
