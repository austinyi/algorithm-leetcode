# # 1. Using Python built-in function
# ## Time: O((n + m) * log(n + m)), Space: O(n+m)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = nums1 + nums2
#         merged.sort()
        
#         l = len(merged)
#         if l % 2 == 1:
#             return merged[l // 2]
#         else:
#             return (merged[l // 2] + merged[l // 2 - 1]) / 2


# # 2. Two-Pointer method
# ## Time: O(n + m), Space: O(1)
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         i, j = 0, 0
#         m1, m2 = 0, 0
#         # Find median.
#         for count in range((n + m) // 2 + 1):
#             m2 = m1
#             if i < m and j < n:
#                 if nums1[i] <= nums2[j]:
#                     m1 = nums1[i]
#                     i += 1
#                 else:
#                     m1 = nums2[j]
#                     j += 1
#             elif i < m:
#                 m1 = nums1[i]
#                 i += 1
#             else:
#                 m1 = nums2[j]
#                 j += 1

#         if (n + m) % 2 == 1:
#             return m1
#         else:
#             return (m1 + m2) / 2
 
# 3. Binary Search
## Time: O(log(min(m,n))), Space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


                
