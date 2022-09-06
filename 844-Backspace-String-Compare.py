class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for c in s:
            if c == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(c)
                
        for c in t:
            if c == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(c)

        return stack_s == stack_t
      
 '''
 # O(1) memory solution
 The idea is that, read next letter from end to start.
 https://leetcode.com/problems/backspace-string-compare/discuss/585027/Python-O(N)-Time-O(1)-Space-Solution-or-Explained
 '''
