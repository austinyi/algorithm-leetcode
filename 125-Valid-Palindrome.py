class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l-i-1]:
                return False
        return True
