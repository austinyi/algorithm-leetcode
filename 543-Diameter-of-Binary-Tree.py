# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            l1, h1 = dfs(root.left)
            l2, h2 = dfs(root.right)
            return max(max(l1,l2), h1+h2), max(h1, h2) + 1
        return dfs(root)[0]

     
