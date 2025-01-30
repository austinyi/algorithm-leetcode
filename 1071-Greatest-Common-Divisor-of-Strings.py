# Time: O(n), Space: O(n/m) = O(n)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        l1, l2 = len(str1), len(str2)
        if str1[:l2] == str2:
            if l1 == l2:
                return str1
                
            return self.gcdOfStrings(str1[l2:], str2)
        else:
            return ""

# Time: O(m+n), Space: O(1)
# from math import gcd

# def gcd_of_strings(str1: str, str2: str) -> str:
#     # Check if str1 and str2 can be formed by some substring x
#     if str1 + str2 != str2 + str1:
#         return ""
    
#     # Find the greatest common divisor of lengths
#     gcd_length = gcd(len(str1), len(str2))
    
#     # The greatest common divisor string
#     return str1[:gcd_length]
