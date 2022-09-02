'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedNums = nums1
        mergedNums.extend(nums2)
        mergedNums.sort()
        
        if len(mergedNums) % 2 == 1: # odd
            return mergedNums[int(len(mergedNums) / 2)]
        else: # even
            return (mergedNums[int(len(mergedNums) / 2)] + mergedNums[int(len(mergedNums) / 2) - 1]) / 2

'''

class Solution:
  
    # Method to find median
    def findMedianSortedArrays(self, A, B):
        
          # Assumption both A and B cannot be empty
        n = len(A)
        m = len(B)
        if (n > m):
            return self.findMedianSortedArrays(B, A)  # Swapping to make A smaller
  
        start = 0
        end = n
        realmidinmergedarray = (n + m + 1) // 2
  
        while (start <= end):
            mid = (start + end) // 2
            leftAsize = mid
            leftBsize = realmidinmergedarray - mid
              
            # checking overflow of indices
            leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
            leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
            rightA = A[leftAsize] if (leftAsize < n) else float('inf')
            rightB = B[leftBsize] if (leftBsize < m) else float('inf')
  
            # if correct partition is done
            if leftA <= rightB and leftB <= rightA:
                if ((m + n) % 2 == 0):
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                return max(leftA, leftB)
  
            elif (leftA > rightB):
                end = mid - 1
            else:
                start = mid + 1
                
