# Time: 4^n / n^(1/2)
# The number of valid sequences follows Catalan numbers
# C(n) = (2n)!/(n!(n+1)!) = 2n C n - 2n C (n+1) -> 4^n / {n^(3/2) sqrt(pi)}
# time complexity = n*C(n) = 4^n / n^(1/2)

# Space: recursion depth is at most 2n => O(n) space for the call stack.
# The output list stores O(4ⁿ/√n) sequences, each of length O(n), 
# requiring O(n * 4ⁿ / √n) space.
# Ignoring output storage, auxiliary space is O(n) (for recursion stack).
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

# Iterative Implementation:
#
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []
#         left = right = 0
#         q = [(left, right, '')]
#         while q:
#             left, right, s = q.pop()
#             if len(s) == 2 * n:
#                 result.append(s)
#             if left < n:
#                 q.append((left + 1, right, s + '('))
#             if right < left:
#                 q.append((left, right + 1, s + ')'))
#         return result
