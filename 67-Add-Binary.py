class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)
        a = list(a[::-1])
        b = list(b[::-1])

        ans = ['0'] * len(a)
        carry = 0

        for i in range(len(b)):
            a[i] = int(a[i])
            b[i] = int(b[i])
            if a[i] + b[i] + carry >= 2:
                ans[i] = str(a[i] + b[i] + carry - 2)
                carry = 1
            else:
                ans[i] = str(a[i] + b[i] + carry)
                carry = 0
        for i in range(len(b), len(a)):
            a[i] = int(a[i])
            if a[i] + carry == 2:
                carry = 1
            else:
                ans[i] = str(a[i] + carry)
                carry = 0

        ans = ''.join(ans)
        if carry == 1:
            return '1' + ans[::-1]
        else:
            return ans[::-1]
