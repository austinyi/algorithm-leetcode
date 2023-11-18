class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0

        # s = sorted(nums)
        # cur, ans = 1, 1
        # prev = s[0]

        # for i in range(1, len(s)):
        #     if s[i] == prev + 1:
        #         cur += 1
        #         prev = s[i]
        #         ans = max(ans, cur)
        #     elif s[i] == prev:
        #         continue
        #     else:
        #         cur = 1
        #         prev = s[i]
        # return ans

        s = set(nums)
        ans = 0
        while s:
            low = high = s.pop()
            while low - 1 in s or high + 1 in s:
                if low - 1 in s:
                    s.remove(low - 1)
                    low -= 1
                else:
                    s.remove(high + 1)
                    high += 1
            ans = max(ans, high - low + 1)
        return ans

# https://leetcode.com/problems/longest-consecutive-sequence/solutions/3332396/simplest-python-solution-with-o-n-time-complexity-and-o-n-space-complexity/
