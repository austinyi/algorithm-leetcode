class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        cur0 = 0
        ans = 0
        for i, n in enumerate(nums):
            if n == 1:
                ans = max(ans, i-l+1-cur0)
            else:
                if cur0 == 0:
                    cur0 += 1
                    ans = max(ans, i-l)
                else:
                    while nums[l] != 0:
                        l += 1
                    l += 1
        return ans - int(len(nums) == ans)
      
        # l = 0
        # cur0 = 0
        # cur = 0
        # ans = 0
        # for i, n in enumerate(nums):
        #     if n == 1:
        #         cur += 1
        #     else:
        #         if cur0 == 0:
        #             cur0 = 1
        #         else:
        #             while nums[l] != 0:
        #                 l += 1
        #             l += 1
        #             ans = max(cur, ans)
        #             cur = i - l 
        # return max(cur, ans) - int(cur == len(nums))
