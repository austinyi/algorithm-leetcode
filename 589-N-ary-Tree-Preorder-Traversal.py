"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        
        def dfs(root, out):
            if not root:
                return
            out.append(root.val)
            for child in root.children:
                dfs(child, out)
        
        dfs(root, output)        
        return output
