# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            b1, h1 = dfs(root.left)
            b2, h2 = dfs(root.right)
            return abs(h1 - h2) <= 1 and b1 and b2, max(h1, h2) + 1
        return dfs(root)[0]
        
