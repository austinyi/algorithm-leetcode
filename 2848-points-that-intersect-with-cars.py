class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 1.
        covered_points = set()
        for start, end in nums:
            covered_points.update(range(start, end + 1))
        return len(covered_points)

        # 2.
        ans = 0
        nums.sort(key = lambda x: x[0])
        for i in range(len(nums)-1):
            if nums[i][1] < nums[i+1][0]:
                ans += nums[i][1] - nums[i][0] + 1
            else:
                nums[i+1] = [nums[i][0], max(nums[i][1], nums[i+1][1])]

        return ans + nums[-1][1] - nums[-1][0] + 1

# 3.
#https://leetcode.com/problems/points-that-intersect-with-cars/solutions/4233066/line-sweep-solution-o-n-runtime-o-1-space-easy-to-follow
# class Solution:
#     def numberOfPoints(self, nums: List[List[int]]) -> int:
        
#         line = [0] * 102
#         points_on_line = 0

#         for s,e in nums:
#             line[s] += 1
#             line[e + 1] -= 1

#         for i in range(1, 102):
#             line[i] += line[i - 1]
#             if line[i] != 0:
#                 points_on_line += 1

#         return points_on_line
