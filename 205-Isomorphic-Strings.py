class Solution(object):
    def isIsomorphic(self, s, t):
        st = {}
        for i, c in enumerate(s):
            if c not in st:
                if t[i] in st.values():
                    return False
                st[c] = t[i]
            else:
                if st[c] != t[i]:
                    return False
        return True
