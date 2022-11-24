class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        for q, p in prerequisites:
            pre[q].append(p)

        check = [0 for _ in range(numCourses)] 

        def dfs(n, cur):
            if n in cur:
                return False
            if check[n]:
                return True

            for p in pre[n]:
                if p in cur or not dfs(p, cur + [n]):
                    return False
                check[p] = 1
            check[n] = 1
            return True
        
        for i in range(numCourses):
            if check[i] == 0 and not dfs(i, []):
                return False

        return True
