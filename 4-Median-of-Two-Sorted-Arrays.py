'''
1. Using Python built-in function

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedNums = nums1
        mergedNums.extend(nums2)
        mergedNums.sort()
        
        if len(mergedNums) % 2 == 1: # odd
            return mergedNums[int(len(mergedNums) / 2)]
        else: # even
            return (mergedNums[int(len(mergedNums) / 2)] + mergedNums[int(len(mergedNums) / 2) - 1]) / 2
            
      
      
2. Merging two sorted arrays from the beginning

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #m, n = len(nums1), len(nums2)
        mid = (len(nums1)+len(nums2)+1) // 2 
        m = 0
        n = 0
        res = []
        for i in range(mid+1):
            n1 = nums1[m] if m < len(nums1) else float('inf')
            n2 = nums2[n] if n < len(nums2) else float('inf')
            if n1 > n2:
                res.append(n2)
                n += 1
            else:
                res.append(n1)
                m += 1

        return res[-2] if (len(nums1)+len(nums2)) % 2 == 1 else (res[-2] + res[-1])/2
 
''' 
 
# 3. Merging two sorted arrays from the beginning without using any additional memory

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m, n = len(nums1), len(nums2)
        mid = (len(nums1)+len(nums2)+1) // 2 
        m = 0
        n = 0
        for i in range(mid):
            n1 = nums1[m] if m < len(nums1) else float('inf')
            n2 = nums2[n] if n < len(nums2) else float('inf')
            if n1 > n2:
                n += 1
            else:
                m += 1
        
        a = nums1[m-1] if m > 0 else float('-inf')
        b = nums2[n-1] if n > 0 else float('-inf')
        
        if (len(nums1)+len(nums2)) % 2 == 1:
            return max(a,b)
        else:
            c = nums1[m] if m < len(nums1) else float('inf')
            d = nums2[n] if n < len(nums2) else float('inf')
            return (max(a,b) + min(c,d))/2


                
