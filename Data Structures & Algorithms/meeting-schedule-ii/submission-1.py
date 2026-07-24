"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        emp=[[0, 0] for _ in range(len(intervals))]
        for i in range(len(intervals)):
            emp[i][0]=intervals[i].start
            emp[i][1]=intervals[i].end
        starts = sorted(emp[i][0] for i in range(len(emp)))
        ends = sorted(emp[i][1] for i in range(len(emp)))
        count = res = s = e = 0
        while s < len(emp):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res