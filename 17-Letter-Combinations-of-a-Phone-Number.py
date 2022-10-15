class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        ans = []
        def dfs(digits, cur):
            if digits == "":
                ans.append(cur)
            else:
                for char in digitToChar[digits[0]]:
                    dfs(digits[1:], cur + char)
      
        dfs(digits, "")
        return ans
