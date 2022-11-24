"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals.sort(key = lambda i: i.start)
        ans = 1
        end = [intervals[0].end]

        for i in range(1, len(intervals)):
            act = 0
            for k in range(len(end)):
                if intervals[i].start >= end[k]:
                    end[k] = intervals[i].end
                    act = 1
                    break
            if act == 0:
                ans += 1
                end.append(intervals[i].end)

        return ans
