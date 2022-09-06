class Solution:
    def decodeString(self, s: str) -> str:
        stack = [s[0]]
        
        for i in range(1, len(s)):
            if s[i] == "]":
                cur = ""
                while True:
                    c = stack.pop()
                    if c == "[":
                        break
                    cur = c + cur
                
                integer = ""
                while stack:
                    if stack[-1].isdigit():
                        integer = stack.pop() + integer
                    else:
                        break  
                        
                stack.append(cur * int(integer))
            else:
                stack.append(s[i])

        return "".join(stack)
