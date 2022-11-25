class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s: str) -> int:
        num = 0
        op = "+"
        stack = []

        def helper(num, op):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(num * stack.pop())
            elif op == "/":
                stack.append(int(stack.pop() / num))
            
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == "(":
                stack.append(op)
                op = "+"
                num = 0
            elif s[i] == ")":
                helper(num, op)
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                helper(num, stack.pop())
                num = 0
                op = s[i]
            elif s[i] in ["+", "-", "*", "/"]:
                helper(num, op)
                num = 0
                op = s[i]

        helper(num, op)
        
        return sum(stack)
            
