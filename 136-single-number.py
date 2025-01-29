# Bit Manipulation
## Time: O(n), Space: O(1)
class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

    # Time: O(n), Space: O(n)
    # def singleNumber(self, nums: List[int]) -> int:
    #     return 2 * sum(set(nums)) - sum(nums)
