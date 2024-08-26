class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        twice = False
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if not twice:
                    nums[cur] = nums[i]
                    cur += 1
                    twice = True
            else:
                nums[cur] = nums[i]
                cur += 1
                twice = False
        return cur
