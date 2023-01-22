class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        if intervals == []:
            return [newInterval]
        elif intervals[0][0] > newInterval[1]:
            ans.append(newInterval)
            ans += intervals
            return ans
        elif intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        l = min(intervals[i][0], newInterval[0])
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            i += 1

        r = max(intervals[i-1][1], newInterval[1])
        ans.append([l,r])
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1

        return ans
