class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for i, (x, y) in enumerate(points):
            heapq.heappush(heap, (-x**2 - y**2, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points[t[1]] for t in heap]

        # ans = []
        # heap = []
        
        # for x, y in points:
        #     heap.append([x**2+y**2, x, y])
        
        # heapq.heapify(heap)
        
        # for i in range(k,0,-1):
        #     _, x, y = heapq.heappop(heap)
        #     ans.append([x,y])
      
        # return ans
