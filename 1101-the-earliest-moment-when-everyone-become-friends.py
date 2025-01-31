# Union
# M: number of logs: N: number of people
# Time: O(M*logM + N + MN)
# Space: O(M+N), M comes from sorting

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        group = {i: i for i in range(n)}

        def union(x, y, n_groups):
            x0, y0 = find(x), find(y)
            if x0 != y0:
                group[x0] = y0
                return n_groups - 1
            return n_groups

        def find(x):
            if group[x] != x:
                group[x] = find(group[x])
            return group[x]
        
        n_groups = n
        for t, x, y in sorted(logs):
            n_groups = union(x, y, n_groups)
            if n_groups == 1:
                return t

        return -1

