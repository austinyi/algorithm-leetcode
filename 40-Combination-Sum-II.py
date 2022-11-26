class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(candidates, target, cur):
            res = []
            if target == 0:
                return [cur]
            elif target < 0:
                return []

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                res += dfs(candidates[i+1:], target - candidates[i], cur + [candidates[i]])
            return res

        return dfs(candidates, target, [])
        
