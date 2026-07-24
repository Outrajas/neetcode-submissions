"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        emp=[[0, 0] for _ in range(len(intervals))]
        for i in range(len(intervals)):
            emp[i][0]=intervals[i].start
            emp[i][1]=intervals[i].end
        emp=sorted(emp)        
        for i in range(len(intervals)-1):
            if emp[i][1]>emp[i+1][0]:
                return False
        return True             
