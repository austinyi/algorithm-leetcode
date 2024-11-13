"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
## https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/solutions/415648/python-easy-inorder-traversal

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head, prev = None, None
        
        def inorder(node):
            nonlocal head, prev
            if node.left:
                inorder(node.left)
            if not head:
                head = node
            if prev:
                prev.right = node
                node.left = prev
            prev = node
            if node.right:
                inorder(node.right)

        inorder(root)
        prev.right = head
        head.left = prev
        return head
        
