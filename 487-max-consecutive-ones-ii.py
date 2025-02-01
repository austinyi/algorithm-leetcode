class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        last = 0
        used = 0 # did we already convert one zero to one
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                ans = max(ans, cur + last)
            else:
                if used == 0:
                    used = 1
                    last = cur + 1
                    cur = 0
                    ans = max(ans, cur + last)
                else:
                    last = cur + 1
                    cur = 0
        return ans
