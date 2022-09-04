class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[-2], cost[-1]
        for i in range(len(cost)-3, -1, -1):
            temp = a
            a = cost[i] + min(a, b)
            b = temp     
        return min(a, b)

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
'''
