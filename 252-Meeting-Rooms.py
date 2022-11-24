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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda i: i.start)
        if len(intervals) == 1:
            return True
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        
'''        

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        for i in range(len(intervals)):
            p1, q1 = intervals[i].start, intervals[i].end
            for j in range(i+1, len(intervals)):
                p2, q2 = intervals[j].start, intervals[j].end
                if p1 < p2 and q1 > p2:
                    return False
                elif p1 > p2 and q1 < q2:
                    return False
                elif p1 == p2:
                    return False

        return True

'''
