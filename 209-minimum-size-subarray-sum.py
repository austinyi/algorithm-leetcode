class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        cur = 0
        l = 0
        for r in range(len(nums)):
            cur += nums[r]
            if cur >= target:
                while l <= r and cur >= target:
                    ans = min(ans, r - l + 1)
                    cur -= nums[l]
                    l += 1
            elif cur < target:
                continue

        return ans if ans != float('inf') else 0

## 
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         ans = float('inf')
#         cur = 0
#         l = 0
#         for r in range(len(nums)):
#             cur += nums[r]
#             while l <= r and cur >= target:
#                 ans = min(ans, r - l + 1)
#                 cur -= nums[l]
#                 l += 1
#         return ans if ans != float('inf') else 0
                                  

