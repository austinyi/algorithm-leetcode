# if numRows = 3, add all characters with index 4k, 
# then add indices with 4k +- 1, then add indices with 4k + 2
# if numRos = 4, 6k, 6k+-1, 6k+-2, 6k+3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ""
        m = (numRows - 1) * 2

        i = 0
        while m*i < len(s):
            ans += s[m*i]
            i += 1
        
        for k in range(1, numRows - 1):
            i = 0
            while m*i + k < len(s):
                ans += s[m*i + k]
                if m*(i+1) - k < len(s):
                    ans += s[m*(i+1) - k]
                i += 1

        k = numRows - 1
        i = 0
        while m*i + k < len(s):
            ans += s[m*i + k]
            i += 1

        return ans

    
