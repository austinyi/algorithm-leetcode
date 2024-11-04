# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        # count = {i:0 for i in range(3)}
        # for n in nums:
        #     count[n] += 1

        # for i in range(count[0]):
        #     nums[i] = 0
        # for i in range(count[0], count[0] + count[1]):
        #     nums[i] = 1
        # for i in range(count[0] + count[1], len(nums)):
        #     nums[i] = 2


     
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # For all idx < p0 : nums[idx < p0] = 0
        # curr is an index of elements under consideration
        p0 = curr = 0

        # For all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
        
