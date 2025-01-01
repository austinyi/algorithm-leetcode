class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        
        y = 0
        temp = x
        while temp > 0:
            a = temp % 10
            temp //= 10
            y = 10*y + a
        
        return y == x

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0 or (x != 0 and x % 10 == 0):
    #         return False

    #     reversed_num = 0
    #     original = x

    #     while x > reversed_num:
    #         reversed_num = reversed_num * 10 + x % 10
    #         x //= 10

    #     return x == reversed_num or x == reversed_num // 10
