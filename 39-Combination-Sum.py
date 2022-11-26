class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, target, cur):
            ans = []
            if target == 0:
                return [cur]
            elif target < 0:
                return []

            for i in range(len(candidates)):
                ans += dfs(candidates[i:], target - candidates[i], cur + [candidates[i]])
            return ans
         
	#ans = []
        #for i in range(len(candidates)):
        #    ans += dfs(candidates[i:], target - candidates[i], [candidates[i]])

        ans = dfs(candidates, target, [])
        
        return ans

    
'''
## https://leetcode.com/problems/combination-sum/solutions/632799/Three-Python-easy-solutions-(DPBFSBacktrack)-with-explanation.-Time-beats-~88
# Dynmaic Programming
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
	cache = [[] for _ in range(target + 1)]
	cache[0] = [[]]
	for c in candidates:
		for i in range(target + 1):
			if i >= c:
				for temp_ans in cache[i - c]:
					cache[i].append(temp_ans + [c])
	return cache[-1]
'''
