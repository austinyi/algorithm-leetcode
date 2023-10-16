class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        elif len(nums) == 1:
            return [[], [nums[0]]]
        ans = []

        for i in self.subsets(nums[1:]):
            ans.append(i)
            ans.append([nums[0]] + i)
        return ans
    
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = []

    #     def dfs(nums, cur):
    #         if nums == []:
    #             ans.append(cur)
    #         else:
    #             dfs(nums[1:], cur)
    #             dfs(nums[1:], cur + [nums[0]])
        
    #     dfs(nums, [])
    #     return ans
