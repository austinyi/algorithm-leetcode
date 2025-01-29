## Time: O(n), Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        maxCount = 0
        for i in nums:
            count[i] = 1 + count.get(i, 0)
            if count[i] > maxCount:
                maxCount = count[i]
                ans = i
        return ans

# Boyer-Moore Voting Algorithm
## Time: O(n), Space: O(1)
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
