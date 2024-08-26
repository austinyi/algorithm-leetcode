class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        a, b = 1, 1
        while a < len(nums):
            if nums[a] != nums[a-1]:
                nums[b] = nums[a]
                a += 1
                b += 1
            else:
                a += 1

        return b
