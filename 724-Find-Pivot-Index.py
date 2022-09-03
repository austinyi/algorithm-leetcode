class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_sum = 0
        for i in range(len(nums)):
            if cur_sum == total - nums[i] - cur_sum:
                return i
            cur_sum += nums[i]
        return -1
        
