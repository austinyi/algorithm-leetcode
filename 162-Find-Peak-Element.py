class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # Find the first index that nums[i] > nums[i+1]. Then naturally nums[i-1] > nums[i]
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
        
