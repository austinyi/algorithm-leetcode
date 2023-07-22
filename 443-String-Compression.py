class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 1
        l = 1 
        cur = chars[0]

        for i in range(1, len(chars)):
            if chars[i] != cur:
                if l == 1:
                    chars[j] = chars[i]
                    cur = chars[i]
                    j += 1
                else:
                    for c in str(l):
                        chars[j] = c
                        j += 1
                    chars[j] = chars[i]
                    cur = chars[i]
                    l = 1
                    j += 1
            else:
                l += 1
        
        if l > 1:
            for c in str(l):
                chars[j] = c
                j += 1
        chars = chars[:j]
        return j


                
