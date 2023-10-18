class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(nums, cur):
            if len(nums) == 0:
                ans.append(cur)
                return
            else:
                k = 0
                while k+1 < len(nums) and nums[k] == nums[k+1]:
                    k += 1
                dfs(nums[k+1:], cur)
                for i in range(k+1):
                    dfs(nums[k+1:], cur + [nums[0]]*(i+1))

        dfs(nums, [])
        return ans
