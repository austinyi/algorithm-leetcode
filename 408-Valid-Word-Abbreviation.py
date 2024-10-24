class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, k = 0, 0
        while i < len(word) and k < len(abbr):
            if not abbr[k].isdigit():
                if word[i] != abbr[k]:
                    return False
                k += 1
                i += 1
            else:
                if abbr[k] == '0':
                    return False
                cur = 0
                while k < len(abbr) and abbr[k].isdigit():
                    cur = 10*cur + int(abbr[k])
                    k += 1
                i += cur
        #return True if i == len(word) and k == len(abbr) else False
        return i == len(word) and k == len(abbr)
                


