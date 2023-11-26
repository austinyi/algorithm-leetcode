# https://www.youtube.com/watch?v=zsJ-J08Qgdk

class Solution:
    def calculate(self, s: str) -> int:
        cur = 0
        sign = 1
        ans = 0
        stack = []

        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in ['+','-']:
                ans += sign * cur
                sign = 1 if c == '+' else -1
                cur = 0
            elif c == '(':
                stack.append(ans)
                stack.append(sign)
                cur = 0
                ans = 0
                sign = 1
            elif c == ')':
                ans += sign * cur
                ans *= stack.pop()
                ans += stack.pop()
                cur = 0
        return ans + sign * cur

