# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False   
        elif x % 10 == 0 and x != 0:
            return False

        y = 0
        while x > y:
            y = 10 * y + x % 10
            x = x // 10
            print(x,y)
        
        return x == y or x == y // 10


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # if x % 10 == 0 and x != 0:
        #     return False
        
        # y = 0
        # temp = x
        # while temp > 0:
        #     a = temp % 10
        #     temp //= 10
        #     y = 10*y + a
        
        # return y == x

