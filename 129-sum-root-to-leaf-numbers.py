# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Recursive Preorder Traversal.
# Time: O(N), Space: O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, num):
            if not node:
                return 0
            if not node.left and not node.right:
                return 10*num + node.val
            return dfs(node.left, 10*num + node.val) + dfs(node.right, 10*num + node.val)

        return dfs(root, 0)

# 2. Iterative Preorder Traversal.
# Time: O(N), Space: O(H)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 0)]

        while stack:
            root, cur = stack.pop()
            if root:
                cur = 10*cur + root.val
                if not root.left and not root.right:
                    ans += cur
                else:
                    stack.append([root.left, cur])
                    stack.append([root.right, cur])
        return ans
