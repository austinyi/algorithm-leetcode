class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ## ITERATE RIGHT TO LEFT
        ans = [len(heights) - 1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > heights[ans[-1]]:
                ans.append(i)
        return ans[::-1]

        ## ITERATE LEFT TO RIGHT
        # ans = [0]
        # for i in range(1, len(heights)):
        #     while ans and heights[ans[-1]] <= heights[i]:
        #         ans.pop()
        #     ans.append(i)
        # return ans


