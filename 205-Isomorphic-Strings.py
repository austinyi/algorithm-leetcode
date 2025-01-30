class Solution(object):
    def isIsomorphic(self, s, t):
        st = {}
        for i in range(len(s)):
            if s[i] in st:
                if t[i] != st[s[i]]:
                    return False
            elif t[i] in st.values():
                return False
            else:
                st[s[i]] = t[i]

        return True
            
    # def isIsomorphic(self, s, t):
    #     if len(s) != len(t):
    #         return False

    #     mapping_s_t = {}
    #     mapping_t_s = {}

    #     for char_s, char_t in zip(s, t):
    #         if (char_s in mapping_s_t and mapping_s_t[char_s] != char_t) or \
    #         (char_t in mapping_t_s and mapping_t_s[char_t] != char_s):
    #             return False

    #         mapping_s_t[char_s] = char_t
    #         mapping_t_s[char_t] = char_s

    #     return True
                

