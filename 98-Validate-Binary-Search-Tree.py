# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = root.left
        right = root.right
        if left:
            while left.right is not None: # while left.right:
                left = left.right
            if left.val >= root.val:
                return False
        if right:
            while right.left is not None:
                right = right.left
            if right.val <= root.val:
                return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left, right = root.left, root.right
        while left:
            if left.val >= root.val: 
                return False
            left = left.right
        while right:
            if right.val <= root.val: 
                return False
            right = right.left
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
'''
