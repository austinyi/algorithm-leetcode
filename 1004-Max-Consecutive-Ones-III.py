class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ### Very Optimized but hard to understand
        # cur0 = 0
        # l = 0
        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         cur0 += 1
        #     if cur0 > k:
        #         cur0 -= nums[l] == 0
        #         l += 1
        # return r - l + 1

        cur0 = cur1 = 0
        ans = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur1 += 1
                ans = max(ans, i - l + 1)
            else: # nums[i] == 0:
                if cur0 < k:
                    cur0 += 1
                    ans = max(ans, i - l + 1)
                else:
                    while nums[l] != 0:
                        cur1 -= 1
                        l += 1
                    l += 1

        return ans

