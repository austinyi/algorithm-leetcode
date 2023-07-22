class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        cur = 0
        for i in range(len(t)):
            if s[cur] == t[i]:
                cur += 1
            if cur == len(s):
                return True
            
        return False
        
        
        

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) == 0:
#             return True
#         idx = 0
#         for c in t:
#             if s[idx] == c:
#                 idx += 1
#                 if idx == len(s):
#                     return True
#         return False
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
    
