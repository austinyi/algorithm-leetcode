# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def right(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def left(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            elif root.right:
                root.val = self.right(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.left(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
