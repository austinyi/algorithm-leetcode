class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if target exists, search returns the leftmost idx of target.
        # if not, returns the leftmost idx of some num > target.
        def search(x):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r) // 2
                if nums[m] >= x:
                    r = m
                else:
                    l = m + 1
            return l
        
        first = search(target)
        last = search(target + 1) - 1

        if first <= last:
            return [first, last]
        return [-1, -1]
