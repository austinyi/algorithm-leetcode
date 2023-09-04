# Good reference for binary search: https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/?envType=study-plan-v2&envId=leetcode-75  
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r) // 2
            if sum([-(-pile // m) for pile in piles]) <= h:
                r = m
            else:
                l = m + 1
        return l
