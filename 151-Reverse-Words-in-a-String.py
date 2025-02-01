# Time: O(n)
# Space Complexity: O(n), Storing the list of words requires additional memory. (s.split())
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


## Implement s.split()
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         res = []
#         cur = ""
#         for c in s:
#             if c == " ":
#                 if cur == "":
#                     continue
#                 else:
#                     res.append(cur)
#                     cur = ""
#             else:
#                 cur += c
#         if cur != "":
#             res.append(cur)
#         return ' '.join(res[::-1])
