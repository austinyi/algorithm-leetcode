class Solution:

    # # 1. Brute force
    # # Time: O(n^2), Space: O(1)
    # # For each element in the array, we find the maximum level of water it can trap after the rain, 
    # # which is equal to the minimum of maximum height of bars on both the sides minus its own height.
    # def trap(self, height):
    #     ans = 0
    #     for i in range(1, len(height) - 1):
    #         left_max = 0
    #         right_max = 0
    #         # Search the left part for max bar size
    #         for j in range(i, -1, -1):
    #             left_max = max(left_max, height[j])
    #         # Search the right part for max bar size
    #         for j in range(i, len(height)):
    #             right_max = max(right_max, height[j])
    #         ans += min(left_max, right_max) - height[i]
    #     return ans
            
    # # 2. Memoization, Prefix Sum
    # # Time: O(n), Space: O(n)
    # def trap(self, height: List[int]) -> int:
    #     if len(height) == 0:
    #         return 0
    #     ans = 0
    #     size = len(height)
    #     left_max, right_max = [0] * size, [0] * size

    #     left_max[0] = height[0]
    #     for i in range(1, size):
    #         left_max[i] = max(height[i], left_max[i - 1])

    #     right_max[-1] = height[-1]
    #     for i in range(size - 2, -1, -1):
    #         right_max[i] = max(height[i], right_max[i + 1])

    #     for i in range(1, size - 1):
    #         ans += min(left_max[i], right_max[i]) - height[i]
    #     return ans

    # 3. Two Pointer
    # Time: O(n), Space: O(1)
    def trap(self, height):
        l, r = 0, len(height) - 1
        ans = 0
        left_max, right_max = height[l], height[r]
        while l < r:
            if left_max <= right_max:
                ans += left_max - height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                ans += right_max - height[r]
                r -= 1
                right_max = max(right_max, height[r])
        return ans
