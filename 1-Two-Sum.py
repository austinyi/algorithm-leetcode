class Solution:
    '''
    # Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
    '''
  
    # One-pass            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = dict()
        for idx, num in enumerate(nums):
            t = target - num
            if t in rec:
                return [rec[t], idx]
            rec[num] = idx

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = dict()
        for i in range(len(nums)):
            t = target - nums[i]
            if t in rec:
                return [rec[t], i]
            rec[nums[i]] = i
    '''
