class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for per in self.permute(nums[:i] + nums[i+1:]):
                ans.append(per + [nums[i]])
        return ans

    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(nums, cur):
            if len(nums) == 1:
                ans.append(cur + [nums[0]])
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i+1:], cur + [nums[i]])

        dfs(nums, [])
        return ans

    

