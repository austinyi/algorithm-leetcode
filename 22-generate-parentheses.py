class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def dfs(l, r, s):
            if len(s) == 2*n:
                output.append(s)
            if l < n:
                dfs(l+1, r, s + '(')
            if r < l:
                dfs(l, r+1, s + ')')
        
        dfs(0, 0, '')
        return output
