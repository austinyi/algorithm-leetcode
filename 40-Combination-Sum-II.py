class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(candidates, target, cur):
            if target < 0:
                return
            elif target == 0:
                ans.append(cur)
            else:
                for i in range(len(candidates)):
                    if i > 0 and candidates[i] == candidates[i-1]:
                        continue
                    dfs(candidates[i+1:], target - candidates[i], cur + [candidates[i]])

        dfs(candidates, target, [])
        return ans
