class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n_w = 0
        n_c = 0
        cur = []
        for w in words:
            if n_c + n_w + len(w) <= maxWidth:
                n_c += len(w)
                n_w += 1
                cur.append(w)
            else:
                if n_w == 1:
                    res.append(cur[0]+" "*(maxWidth - n_c))
                else:
                    k = (maxWidth - n_c) // (n_w - 1)
                    r = (maxWidth - n_c) % (n_w - 1)
                    char = ""
                    for idx, cur_w in enumerate(cur):
                        char += cur_w
                        if idx < r:
                            char += " " * (k + 1)
                        elif idx < n_w - 1: 
                            char += " " * k
                    res.append(char)
                cur = [w]
                n_c = len(w)
                n_w = 1

        if cur:
            char = ""
            space = maxWidth - n_c - n_w + 1
            for idx, cur_c in enumerate(cur):
                char += cur_c
                if idx < n_w - 1:
                    char += " "
            char += " " * space
            res.append(char)
        return res
