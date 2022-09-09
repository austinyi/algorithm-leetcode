class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        
        while n != 1  and n not in store:
            store.add(n)
            cur = 0
            while n:
                cur += (n % 10)**2
                n = n // 10
            n = cur
            
        return True if n == 1 else False
    
