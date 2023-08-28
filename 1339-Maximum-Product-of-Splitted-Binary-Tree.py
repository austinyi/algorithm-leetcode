# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        store = []
        def tree_sum(r):
            if r is None:
                return 0
            s = r.val + tree_sum(r.left) + tree_sum(r.right)
            store.append(s)
            return s
        total_sum = tree_sum(root)
        
        # ans = 0
        # for e in store:
        #     if ans < (total_sum - e)*e:
        #         ans = (total_sum - e)*e
        # return ans % (10**9 + 7)
        return max([(total_sum - e)*e for e in store]) % (10**9 + 7)

