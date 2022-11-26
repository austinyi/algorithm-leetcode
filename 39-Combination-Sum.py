class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(candidates, target, cur):
            ans = []
            if target == 0:
                return [cur]
            elif target < 0:
                return []

            for i in range(len(candidates)):
                ans += dfs(candidates[i:], target - candidates[i], cur + [candidates[i]])
            return ans
            
        #for i in range(len(candidates)):
        #    ans += dfs(candidates[i:], target - candidates[i], [candidates[i]])

        ans = dfs(candidates, target, [])
        
        return ans
