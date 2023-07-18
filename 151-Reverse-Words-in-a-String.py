class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        cur = ""
        for c in s:
            if c == " ":
                if cur == "":
                    continue
                else:
                    res.append(cur)
                    cur = ""
            else:
                cur += c
        if cur != "":
            res.append(cur)
        return ' '.join(res[::-1])
