"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # path = set()
        # while p:
        #     path.add(p)
        #     p = p.parent
        # while q not in path:
        #     q = q.parent
        # return q

        def height(node):
            h = 1
            while node:
                node = node.parent
                h += 1
            return h
        
        p_h = height(p)
        q_h = height(q)
        
        if p_h < q_h:
            for _ in range(q_h - p_h):
                q = q.parent
        elif p_h > q_h:
            for _ in range(p_h - q_h):
                p = p.parent

        while p != q:
            p = p.parent
            q = q.parent
        return p
        

        #https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/solutions/4590067/python-beats-99-o-1-space-but-it-actually-makes-sense-interviewers-may-reject-other-answers
