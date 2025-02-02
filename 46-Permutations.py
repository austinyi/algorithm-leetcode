# Time: O(n⋅n!)
# For each of the n! permutations, we need O(n) work to copy curr into the answer. 
# Space: O(n)
# We don't count the answer as part of the space complexity. 
# The extra space we use here is for curr and the recursion call stack. 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for per in self.permute(nums[:i] + nums[i+1:]):
                ans.append(per + [nums[i]])
        return ans

