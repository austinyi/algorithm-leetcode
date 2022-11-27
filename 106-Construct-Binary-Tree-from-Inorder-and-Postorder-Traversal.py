# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        
        ans = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        ans.left = self.buildTree(inorder[:idx], postorder[:idx])
        ans.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return ans
