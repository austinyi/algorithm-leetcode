class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            l1, r1 = firstList[i]
            l2, r2 = secondList[j]
            if l1 <= r2 and l2 <= r1:
                ans.append([max(l1, l2), min(r1, r2)])
            if r1 < r2:
                i += 1
            else:
                j += 1
        return ans
        
        # i, j = 0, 0
        # ans = []
        # while i < len(firstList) and j < len(secondList):
        #     if firstList[i][0] < secondList[j][0]:
        #         while i < len(firstList) and firstList[i][1] < secondList[j][0]:
        #             i += 1
        #         if i == len(firstList):
        #             return ans 
        #         if firstList[i][0] <= secondList[j][1]:
        #             m = max(secondList[j][0], firstList[i][0])
        #             if firstList[i][1] < secondList[j][1]:
        #                 ans.append([m, firstList[i][1]])
        #                 i += 1
        #             else:
        #                 ans.append([m, secondList[j][1]])
        #                 j += 1
        #     else:
        #         while j < len(secondList) and secondList[j][1] < firstList[i][0]:
        #             j += 1
        #         if j == len(secondList):
        #             return ans
        #         if secondList[j][0] <= firstList[i][1]:
        #             m = max(secondList[j][0], firstList[i][0])
        #             if firstList[i][1] < secondList[j][1]:
        #                 ans.append([m, firstList[i][1]])
        #                 i += 1
        #             else:
        #                 ans.append([m, secondList[j][1]])
        #                 j += 1
        # return ans
