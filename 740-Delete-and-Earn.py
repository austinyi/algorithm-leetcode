class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev, curr = 0, 0
        for n in range(1, max(count.keys())+1):
            prev, curr = curr, max(prev + n*count[n], curr)
        return curr
