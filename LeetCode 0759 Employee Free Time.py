"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution: # 41 78
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted([interval for personSchedule in schedule for interval in personSchedule], key=lambda i: i.start)
        
        ans = []
        curEnd = intervals[0].end
        for i in intervals:
            if i.start > curEnd:
                ans.append(Interval(curEnd, i.start))
            curEnd = max(curEnd, i.end)
            
        return ans