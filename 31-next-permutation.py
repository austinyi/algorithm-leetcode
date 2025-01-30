class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode.com/problems/next-permutation/editorial
        # Scan numbers from the right, 
        # and find pair a[i] and a[i−1] where, a[i] > a[i−1].
        # swap a[i-1] and a[j] 
        # (scan from right and find first j such that a[j] > a[i-1])
        # reverse the numbers following a[i-1]
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums

        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i == -1:
            return reverse(nums, 0)
        else:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            return reverse(nums, i+1)

