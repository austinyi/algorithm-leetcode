class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {i:0 for i in range(3)}
        for n in nums:
            count[n] += 1

        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0], count[0] + count[1]):
            nums[i] = 1
        for i in range(count[0] + count[1], len(nums)):
            nums[i] = 2

        
        
        
        '''
        l, r = 0, len(nums) - 1
        i = 0
        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
        while i <= r:
            if nums[i] == 0:
                swap(l,i)
                l += 1
            elif nums[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
       '''     
