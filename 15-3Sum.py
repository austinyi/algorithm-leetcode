class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums) - 1

        while n >= 2 and nums[n] >= 0:
            l, r = 0, n-1
            while l < r:
                threesum = nums[l] + nums[r] + nums[n]
                if threesum == 0:
                    ans.append([nums[l], nums[r], nums[n]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
            
            n -= 1
            while n >= 2 and nums[n] == nums[n+1]:
                n -= 1
        
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
