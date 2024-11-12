# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/solutions/1823242/clean-solutions-for-meta-interview-with-potential-follow-ups

## 2: Not using dictionary
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [(i, n) for i, n in enumerate(nums) if n != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        cur1, cur2 = 0, 0
        while cur1 < len(self.nums) and cur2 < len(vec.nums):
            if self.nums[cur1][0] == vec.nums[cur2][0]:
                ans += self.nums[cur1][1] * vec.nums[cur2][1]
                cur1 += 1
                cur2 += 1
            elif self.nums[cur1][0] > vec.nums[cur2][0]:
                cur2 += 1
            else:
                cur1 += 1
        return ans

## 1. dictionary
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: nums[i] for i in range(len(nums)) if nums[i] != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for key in self.nums:
            ans += self.nums[key] * vec.nums.get(key, 0)
        return ans
        
#### Follow up question: 
#### What if only one vector is sparse and the other is not fully sparse?

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = [(i, n) for i, n in enumerate(nums) if n != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, n in self.nums:
            val = self.binary_search(vec.nums, i)
            ans += val * nums
        return ans

    def binary_search(self, vec_nums, idx):
        l, r = 0, len(vec_nums) - 1
        while l < r:
            mid = (start + end) // 2
            if vec_nums[mid][0] == idx:
                return vec_nums[mid][1]
            elif vec_nums[mid][0] > idx:
                r = mid - 1
            else:
                l = mid + 1
        if vec_nums[l][0] == idx:
            return vec_nums[l][1]
        elif vec_nums[r][0] == idx:
            return vec_nums[r][1]
        
        return 0

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
