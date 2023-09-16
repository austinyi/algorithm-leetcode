class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        num = self.countAndSay(n-1)

        cur = num[0]
        l = 1
        i = 1
        ans = ""
        while i < len(num):
            if num[i] == cur:
                l += 1
                i += 1
            else:
                ans += str(l) + str(cur)
                cur = num[i]
                i += 1
                l = 1
        ans += str(l) + str(cur)
        return ans
