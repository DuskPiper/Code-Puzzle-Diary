# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals): # 100%, 1%
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals = sorted(intervals, key = lambda x: x.start)
        ans = []
        cur = intervals[0]
        intervals.append(Interval(sys.maxsize, sys.maxsize)) # 末尾放个最大，这样保证不会漏append原本的末项
        for interval in intervals:
            if cur.end >= interval.start:
                cur.end = max(cur.end, interval.end) #merge
            else: # 不能merge则看下一项
                ans.append(cur)
                cur = interval
        return ans