class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x):
            return a*x*x + b*x + c
        q = [quad(i) for i in nums]
        ans = [0] * len(nums)

        l, r = 0, len(nums) - 1
        
        if a > 0:
            i = len(nums) - 1
            while l <= r:
                if q[l] <= q[r]:
                    ans[i] = q[r]
                    r -= 1
                else:
                    ans[i] = q[l]
                    l += 1
                i -= 1
        else:
            i = 0
            while l <= r:
                if q[l] <= q[r]:
                    ans[i] = q[l]
                    l += 1
                else:
                    ans[i] = q[r]
                    r -= 1
                i += 1

        return ans
            
