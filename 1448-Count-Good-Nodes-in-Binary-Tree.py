# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, m):
            if not node:
                return 0
            cur = int(node.val >= m)
            if not node.right and not node.left:
                return cur
            elif not node.right:
                return cur + dfs(node.left, max(m, node.left.val))
            elif not node.left:
                return cur + dfs(node.right, max(m, node.right.val))
            return cur + dfs(node.left, max(m, node.left.val)) + dfs(node.right, max(m, node.right.val))
            
        return dfs(root, root.val)
