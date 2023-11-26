class Solution:
    def calculate(self, s: str) -> int:
        cur, ans = 0, 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                cur = 10*cur + int(c)
            elif c in ['+','-']:
                if stack:
                    stack.append(cur)
                    cur = stack.pop(0)
                    while stack:
                        op = stack.pop(0)
                        if op == '*':
                            cur *= stack.pop(0)
                        else:
                            cur //= stack.pop(0) 
                    ans += sign * cur
                else:
                    ans += sign * cur
                cur = 0
                sign = 1 if c == '+' else -1    

            elif c in ['*','/']:
                stack.append(cur)
                stack.append(c)
                cur = 0

        if stack:
            stack.append(cur)
            cur = stack.pop(0)
            while stack:
                op = stack.pop(0)
                if op == '*':
                    cur *= stack.pop(0)
                else:
                    cur //= stack.pop(0) 
            ans += sign * cur
        else:
            ans += sign * cur

        return ans







        # i = 0
        # ans = 0
        # num = 0
        # prev = 0
        # op = "+"

        # while i < len(s):
        #     cur = s[i]
        #     if cur.isdigit():
        #         cur = int(cur)
        #         num = cur
        #         while i < len(s) - 1 and s[i+1].isdigit():
        #             num = 10*num + int(s[i+1])
        #             i += 1

        #         if op == "+":
        #             ans += num
        #             prev = num
        #         elif op == "-":
        #             ans -= num
        #             prev = -num
        #         elif op == "*":
        #             ans -= prev
        #             prev *= num
        #             ans += prev
        #         else:
        #             ans -= prev
        #             prev = int(prev/num) 
        #             ans += prev
        #         num = 0
        #     elif cur != " ":
        #         op = cur
        #     i += 1
        # return ans
