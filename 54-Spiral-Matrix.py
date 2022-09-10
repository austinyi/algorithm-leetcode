class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        
        ans = []
        
        while l < r and t < b:
            ans.extend(matrix[t][l:r])
            t += 1

            for i in range(t, b):
                ans.append(matrix[i][r-1])
            r -= 1
            
            if l == r or t == b:
                break
                
            ans.extend(matrix[b-1][l:r][::-1])
            b -= 1
        
            for i in range(b-1, t-1, -1):
                ans.append(matrix[i][l])
            l += 1

        return ans
    
