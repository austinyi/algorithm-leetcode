class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = dict()
        for c in tasks:
            d[c] = 1 + d.get(c, 0)
        
        maxHeap = [-cnt for cnt in d.values()]
        heapq.heapify(maxHeap)
        
        ans = 0
        q = deque()
        while maxHeap or q:
            ans += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt < 0:
                    q.append([cnt, ans + n])
            if q and q[0][1] == ans:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return ans
