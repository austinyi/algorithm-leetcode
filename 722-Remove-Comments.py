class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        comment = False
        cur = ''

        for l in source:
            i = 0
            while i < len(l):
                if i == len(l) - 1:
                    if not comment:
                        cur += l[i]
                    break
                twoChars = l[i:i+2]
                if twoChars == '//':
                    if not comment:
                        break
                    else:
                        i += 2
                elif twoChars == '/*':
                    if not comment:
                        comment = True
                        i += 2
                    else:
                        i += 1
                elif twoChars == '*/':
                    if comment:
                        comment = False
                        i += 2
                    else:
                        cur += l[i]
                        i += 1
                else:
                    if not comment:
                        cur += l[i]
                    i += 1
            if cur and not comment:
                ans.append(cur)
                cur = ''
        return ans
