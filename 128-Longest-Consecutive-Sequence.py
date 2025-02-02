## 1. Sorting. Time: O(nlogn), Space: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         nums.sort()
#         ans, cur = 1, 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1] + 1:
#                 cur += 1
#                 ans = max(ans, cur)
#             elif nums[i] == nums[i-1]:
#                 continue
#             else:
#                 cur = 1
#         return ans
        
# Time: O(n), Space: O(n) - store set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

#         s = set(nums)
#         ans = 0
#         while s:
#             low = high = s.pop()
#             while low - 1 in s or high + 1 in s:
#                 if low - 1 in s:
#                     s.remove(low - 1)
#                     low -= 1
#                 else:
#                     s.remove(high + 1)
#                     high += 1
#             ans = max(ans, high - low + 1)
#         return ans

# # https://leetcode.com/problems/longest-consecutive-sequence/solutions/3332396/simplest-python-solution-with-o-n-time-complexity-and-o-n-space-complexity/
