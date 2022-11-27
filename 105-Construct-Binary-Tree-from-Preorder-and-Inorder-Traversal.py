# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        top = preorder[0]
        ans = TreeNode(top)
        idx = inorder.index(top)

        ans.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        ans.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return ans
