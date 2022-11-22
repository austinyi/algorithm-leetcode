class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()

        ans = 0
        prev = -1

        for num in nums:
            if prev < num:
                prev = num
            else:
                ans += prev - num + 1
                prev += 1
        return ans
        
'''

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()

        if nums[0] != nums[1]:
            return self.minIncrementForUnique(nums[1:])
        nums[1] += 1
        return 1 + self.minIncrementForUnique(nums)
'''
