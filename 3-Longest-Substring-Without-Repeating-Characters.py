class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # SLOW
        # ans = 0
        # for i in range(len(s)):
        #     char_set = set()
        #     char_set.add(s[i])
        #     j = i + 1
        #     while j < len(s) and s[j] not in char_set:
        #         char_set.add(s[j])
        #         j += 1
        #     ans = max(ans, j - i)
        # return ans


        # charset = set()
        # cur = 0
        # res = 0
        # length = len(s)
        # for i in range(length):
        #     while cur < length and s[cur] not in charset:
        #         charset.add(s[cur])
        #         cur += 1
        #     res = max(res, cur - i)
        #     charset.remove(s[i])
        # return res

        # Sliding Window
        seen = {}
        ans = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                ans = max(ans, r - l + 1)
            else:
                if seen[s[r]] < l:
                    ans = max(ans, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r 
        return ans
