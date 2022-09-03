class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = dict()
        for i, c in enumerate(s):
            if c in s_to_t:
                if s_to_t[c] != t[i]:
                    return False
            else:
                if t[i] in s_to_t.values():
                    return False
                else:
                    s_to_t[c] = t[i]

        return True
      
