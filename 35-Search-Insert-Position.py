class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Find i such that a_{i-1} < target <= a_i
        l, r = 0, len(nums) 
        while l < r:
            m = (l+r) // 2
            if target <= nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
            else:
                return m 
        return l
        
