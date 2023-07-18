class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        i = 0 
        j = len(l)-1
        while i < j:
            while l[i] not in ['a','e','i','o','u','A','E','I','O','U'] and i < j:
                i += 1
            while l[j] not in ['a','e','i','o','u','A','E','I','O','U'] and j > i:
                j -= 1
            if i != j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return "".join(l)
