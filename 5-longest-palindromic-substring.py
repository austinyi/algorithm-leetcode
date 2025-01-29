# 1: Check All Substrings
## Time: O(n^3), Space: O(1)

# 2: Expand from Centers
## Time: O(n^2), Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        
        start, end = 0, 0

        for i in range(len(s) - 1):
            l1, r1 = expand_from_center(i, i)
            l2, r2 = expand_from_center(i, i+1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end+1]

# # 3: Manacher's Algorithm
# Very Challenging
# ## Time: O(n), Space: O(1)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         # Step 1: Preprocess string with `#` to handle even-length cases
#         T = "#".join("^{}$".format(s))  # Add sentinels at start and end
#         n = len(T)
#         P = [0] * n  # Array to store palindrome radii
#         C, R = 0, 0  # Center and right boundary

#         # Step 2: Find palindromes
#         for i in range(1, n - 1):
#             mirror = 2 * C - i  # Mirror index of `i`

#             # Use previously computed palindrome if inside `R`
#             if i < R:
#                 P[i] = min(R - i, P[mirror])

#             # Expand around center `i`
#             while T[i + (1 + P[i])] == T[i - (1 + P[i])]:
#                 P[i] += 1

#             # Update center and right boundary if we expanded past `R`
#             if i + P[i] > R:
#                 C, R = i, i + P[i]

#         # Step 3: Extract the longest palindrome
#         max_length, center_index = max((P[i], i) for i in range(1, n - 1))
#         start = (center_index - max_length) // 2  # Convert back to original index
#         return s[start: start + max_length]

            
