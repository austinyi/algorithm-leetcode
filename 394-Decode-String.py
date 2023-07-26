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


# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         for c in s:
#             if c == ']':
#                 cur = ''
#                 while stack[-1] != '[':
#                     cur = stack.pop() + cur
#                 stack.pop()

#                 num = ''
#                 while stack and stack[-1].isdigit():
#                     num = stack.pop() + num
#                 cur = int(num) * cur
#                 stack.append(cur)
#             else:
#                 stack.append(c)
#         return ''.join(stack)
