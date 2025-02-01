# Iterative Binary Search
# If the middle element is greater than its right neighbor, 
# then a peak must exist on the left side (including the middle).
# Otherwise, a peak must exist on the right side.
# Time: O(logn), Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l
