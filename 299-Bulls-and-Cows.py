class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sCount = dict()
        a = b = 0
        
        for i, char in enumerate(secret):
            if char != guess[i]:
                sCount[char] = 1 + sCount.get(char, 0)
            
        for i, char in enumerate(guess):
            if char == secret[i]:
                a += 1
            elif sCount.get(char, 0) > 0:
                b += 1
                sCount[char] -= 1
                
        return str(a) + "A" + str(b) + "B"
                
