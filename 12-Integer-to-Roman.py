class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        f = num // 1000
        num %= 1000
        if f != 0:
            ans += "M" * f
        
        f = num // 100
        num %= 100
        if f != 0:
            if f == 9:
                ans += "CM"
            elif 5 <= f <= 8:
                ans += "D"
                ans += "C" * (f % 5)
            elif f == 4:
                ans += "CD"
            else:            
                ans += "C" * f
        
        f = num // 10
        num %= 10
        if f != 0:
            if f == 9:
                ans += "XC"
            elif 5 <= f <= 8:
                ans += "L"
                ans += "X" * (f % 5)
            elif f == 4:
                ans += "XL"
            else:            
                ans += "X" * f
        
        if num != 0:
            if num == 9:
                ans += "IX"
            elif 5 <= num <= 8:
                ans += "V"
                ans += "I" * (num % 5)
            elif num == 4:
                ans += "IV"
            else:            
                ans += "I" * num
        return ans
      
      
 '''
 class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        
        # Result Variable
        r = ''
        
        
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num-=n
        return r
        
'''
