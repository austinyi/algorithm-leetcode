class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        store = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                store.append(i)
            elif i == ")" and store and store[-1] == "(":
                store.pop()
            elif i == "}" and store and store[-1] == "{":
                store.pop()
            elif i == "]" and store and store[-1] == "[":
                store.pop()
            else:
                return False
        return not store
            
                
                
