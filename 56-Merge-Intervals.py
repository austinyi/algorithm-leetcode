class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i+1][0]:
                ans.append(intervals[i])
            else:
                intervals[i+1] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
        
        ans.append(intervals[-1])

        return ans

