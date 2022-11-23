class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        ans = []
        nums.sort()
        
        p = len(nums) - 1
        while p > 1: # nums[p] >= 0
            l, r = 0, p - 1
            while l < r:
                if nums[l] + nums[r] + nums[p] == 0:
                    ans.append([nums[l], nums[r], nums[p]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[p] > 0:
                    r -= 1
                else:
                    l += 1
            p -= 1
            while nums[p] == nums[p+1] and p > 1:
                p -= 1
        return ans
        
'''        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                n = nums[i] + nums[j]
                if -n in h and h[-n] > j:
                    ans.add((nums[i], nums[j], -n))
        return ans


'''
