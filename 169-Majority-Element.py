class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        ans, maxCount = nums[0], 0
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > maxCount:
                maxCount = count[i]
                ans = i
        return ans
