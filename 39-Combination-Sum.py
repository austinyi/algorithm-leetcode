class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(candidates, target, cur):
            if candidates == []:
                return
            elif target == candidates[0]:
                ans.append(cur + [candidates[0]])
                return
            elif target < candidates[0]:
                return
            else:
                for i in range(len(candidates)):
                    dfs(candidates[i:], target - candidates[0], cur + [candidates[0]])

        for i in range(len(candidates)):
            dfs(candidates[i:], target, [])

        return ans
