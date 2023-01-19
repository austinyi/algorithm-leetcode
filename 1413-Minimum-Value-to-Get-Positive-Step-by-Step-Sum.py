class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 0
        min_sum = 0
        for n in nums:
            start += n
            min_sum = min(min_sum, start)

        if min_sum < 0:
            return -min_sum + 1
        else:
            return 1
        
        
