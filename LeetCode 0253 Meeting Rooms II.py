# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object): # 99.9%, 92%
    def minMeetingRooms(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        ans, endsIter = 0, 0
        for s in xrange(len(starts)): # 新开始一个meeting
            if starts[s] < ends[endsIter]: ans += 1 # 如果目前进行中最先结束的一个没有结束，那就+1room
            else: endsIter += 1 # 如果结束了则ends后移一位
        return ans