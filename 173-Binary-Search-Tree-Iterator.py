# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack  = []
        self.pushLeftTree(root)
    
    def pushLeftTree(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        cur = self.stack.pop()
        if cur.right:
            self.pushLeftTree(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
