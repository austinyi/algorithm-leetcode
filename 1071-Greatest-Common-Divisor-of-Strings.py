class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        l1 = len(str1)
        l2 = len(str2)
        # l1 >= l2
        if str1[:l2] == str2:
            if l1 == l2:
                return str1
            str1 = str1[l2:]
            return self.gcdOfStrings(str1, str2)
        else:
            return ""
