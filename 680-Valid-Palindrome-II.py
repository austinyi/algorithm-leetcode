class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            l, r = i, j
            while l <= r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check_palindrome(s, i+1, j) or check_palindrome(s, i, j-1)
        return True
