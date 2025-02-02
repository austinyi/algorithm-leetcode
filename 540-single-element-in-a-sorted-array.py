class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if m > 0 and nums[m] == nums[m-1]:
                if (r - m) % 2 == 0:
                    r = m 
                else:
                    l = m + 1
            elif m < len(nums) and nums[m] == nums[m+1]:
                if (r - m + 1) % 2 == 0:
                    r = m - 1
                else:
                    l = m
            else:
                return nums[m]
        return nums[l]
        
