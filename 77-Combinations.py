# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         def backtrack(curr, first_num):
#             if len(curr) == k:
#                 ans.append(curr[:])
#                 return

#             need = k - len(curr)
#             remain = n - first_num + 1
#             available = remain - need

#             for num in range(first_num, first_num + available + 1):
#                 curr.append(num)
#                 backtrack(curr, num + 1)
#                 curr.pop()

#         ans = []
#         backtrack([], 1)
#         return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(start, k, cur):
            if k == 0:
                ans.append(cur)
            else:
                # i has to start at least at n-k+2 to select k more number
                for i in range(start, n-k+2):
                    dfs(i+1, k-1, cur + [i])
        dfs(1, k, [])
        return ans
