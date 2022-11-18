"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        def post(node):
            for child in node.children:
                post(child)
            ans.append(node.val)
        post(root)
        return ans
        
        '''
   def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            ans += self.postorder(child)
        ans.append(root.val)
        return ans        
        
        

    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
        return ans[::-1]
        '''
