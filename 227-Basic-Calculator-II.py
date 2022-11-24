class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        ans = 0
        num = 0
        prev = 0
        op = "+"

        while i < len(s):
            cur = s[i]
            if cur.isdigit():
                cur = int(cur)
                num = cur
                while i < len(s) - 1 and s[i+1].isdigit():
                    num = 10*num + int(s[i+1])
                    i += 1
                
                if op == "+":
                    ans += num
                    prev = num
                elif op == "-":
                    ans -= num
                    prev = -num
                elif op == "*":
                    ans -= prev
                    prev *= num
                    ans += prev
                else:
                    ans -= prev
                    prev = int(prev/num) 
                    ans += prev
                num = 0
            elif cur != " ":
                op = cur
            i += 1
        return ans
