class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h = {i: [] for i in range(numCourses)}
        for q, p in prerequisites:
            h[q].append(p)
        
        visited = [0 for _ in range(numCourses)]
        cur = set()
        ans = []

        def dfs(c):
            if visited[c] == 1:
                return True
            if c in cur:
                return False
                
            cur.add(c)
            for pre in h[c]:
                if not dfs(pre):
                    return False
            
            cur.remove(c)
            ans.append(c)
            visited[c] = 1
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return ans
        
