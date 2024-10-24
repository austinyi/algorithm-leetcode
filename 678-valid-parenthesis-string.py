class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                open.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
        while star and open:
            if star[-1] < open[-1]:
                return False
            star.pop()
            open.pop()

        return not open
        
