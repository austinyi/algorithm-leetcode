class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        count = [[bin(n).count("1"), n] for n in arr]
        s = sorted(count, key=lambda x: (x[0], x[1]))
        
        return [s[i][1] for i in range(len(arr))]
