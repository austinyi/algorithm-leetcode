class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCount, mCount = dict(), dict()
        for i in ransomNote:
            rCount[i] = 1 + rCount.get(i, 0)
        for i in magazine:
            mCount[i] = 1 + mCount.get(i, 0)

        for c in rCount:
            if rCount[c] > mCount.get(c, 0):
                return False
        return True
