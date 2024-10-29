class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            
            m = (l+r) // 2
 
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1
    

    
    '''
    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            l = 0
            r = len(nums) - 1
            while l < r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            if nums[l] == target:
                return l
            else:
                return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            while l < r:
                m = (l+r) // 2
                if nums[m] > nums[l]:
                    l = m 
                else:
                    r = m
            pivot = l+1

        if target >= nums[0]:
            l = 0
            r = pivot - 1
            while l < r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            if nums[l] == target:
                return l
            else:
                return -1
        else:
            l = pivot
            r = len(nums) - 1
            while l < r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            if nums[l] == target:
                return l
            else:
                return -1
        



    '''
