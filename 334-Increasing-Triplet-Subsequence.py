class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        i = 0
        while nums[i] >= nums[i+1] and i+2 < len(nums):
            i += 1
        j = i+1
        k = i+2

        while k < len(nums):
            if nums[k] > nums[j]:
                return True
            elif nums[k] > nums[i]:
                j = k
                k += 1
            elif nums[k] <= nums[i]:
                i = k
                k += 1
        return False



