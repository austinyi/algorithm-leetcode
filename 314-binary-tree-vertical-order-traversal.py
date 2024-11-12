# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

## 1. BFS with sorting
# Time: O(n logn), Space: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]

## 2. BFS without sorting
# Time: O(n), Space: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        min_col, max_col = 0, 0

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_col = min(min_col, column)
                max_col = max(max_col, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                
                        
        return [columnTable[x] for x in range(min_col, max_col + 1)]
