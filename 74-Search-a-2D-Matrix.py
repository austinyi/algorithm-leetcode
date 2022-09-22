class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        
        while l <= r:
            mid = int((l+r)/2)
            if matrix[mid // n][mid % n] > target:
                r = mid - 1
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                return True
        return False
    
    
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i = 0
        while i < m and target >= matrix[i][0]:
            i += 1
                        
        for j in range(n):
            if matrix[i-1][j] == target:
                return True
        return False
   
'''
