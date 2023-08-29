class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(b, a) + cost[i]
        return min(a,b)


        # a, b = cost[-2], cost[-1]
        # for i in range(len(cost)-3, -1, -1):
        #     temp = a
        #     a = cost[i] + min(a, b)
        #     b = temp     
        # return min(a, b)
