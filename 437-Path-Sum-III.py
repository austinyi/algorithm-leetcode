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
            
