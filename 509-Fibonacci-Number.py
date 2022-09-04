'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        fn = [0, 1]
        for i in range(2, n+1):
            fn.append(fn[-1] + fn[-2])
            
        return fn[-1]
'''

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        for i in range(2, n+1):
            temp = b
            b += a
            a = temp
        return b

        
