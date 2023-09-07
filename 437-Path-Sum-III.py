# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, curSum, prevSum):
            if not node:
                return 0
            curSum += node.val
            ans = prevSum.get(curSum - targetSum, 0)
            prevSum[curSum] = 1 + prevSum.get(curSum, 0)
            ans += dfs(node.left, curSum, prevSum)
            ans += dfs(node.right, curSum, prevSum)
            
            prevSum[curSum] -= 1

            return ans 
            
        return dfs(root, 0, {0:1})


######## Brute Force
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0 
        
        def dfs(root, targetSum):
            if not root:
                return 0
            return dfs(root.left, targetSum - root.val) + dfs(root.right, targetSum - root.val) + (root.val == targetSum)
            
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
            
######## Memorization of path sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.d = {0:1}
        self.ans = 0
        
        self.dfs(root, 0, targetSum)
        return self.ans
    
    def dfs(self, root, prevSum, targetSum):
        if not root:
            return 
        
        curSum = prevSum + root.val
        self.ans += self.d.get(curSum - targetSum, 0)
        self.d[curSum] = 1 + self.d.get(curSum, 0)

        self.dfs(root.left, curSum, targetSum)
        self.dfs(root.right, curSum, targetSum)        
        self.d[curSum] -= 1
