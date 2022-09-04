# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = collections.deque()
        if not root:
            return []
        else:
            q.append([root])
        
        while q:
            level = []
            res = []
            pop = q.popleft()
            for i in pop:
                res.append(i.val)
                if i.left:
                    level.append(i.left)
                if i.right: 
                    level.append(i.right)
            ans.append(res)
            if len(level) > 0:
                q.append(level)
        return ans
