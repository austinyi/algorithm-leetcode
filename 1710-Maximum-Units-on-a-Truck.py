class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        n = len(boxTypes)
        ans = 0 

        s = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for i in range(n):
            if truckSize >= s[i][0]:
                ans += s[i][0] * s[i][1]
                truckSize -= s[i][0]
            elif truckSize < s[i][0] and truckSize != 0:
                ans += truckSize * s[i][1]
                truckSize = 0
            else:
                break

        return ans
