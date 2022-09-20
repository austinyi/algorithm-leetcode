class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                cur = int(num1[i]) * int(num2[j])
                ans[i+j] += cur
                ans[i+j+1] += ans[i+j] // 10
                ans[i+j] = ans[i+j] % 10
        
        ans = ans[::-1]
        idx = 0
        while ans[idx] == 0:
            idx += 1
        
        return "".join(map(str, ans[idx:]))
