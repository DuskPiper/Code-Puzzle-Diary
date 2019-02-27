# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals): #99.69%
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        inte = sorted(intervals, key = lambda x: x.start) #按左边界排序，画个图就明白这样的好处
        rbound, ans= inte[0].end, [inte[0]] #最新的右边界，最终答案
        for pair in inte: #按顺序取出判断并插入答案
            if pair.start <= rbound: #overlap，执行merge，update答案最后一项
                if pair.end > rbound: rbound = pair.end #rbound = max(pair.end, rbound)
                ans[-1].end = rbound
            else: #not overlap，直接丢进答案里
                ans.append(pair)
                rbound = pair.end
        return ans