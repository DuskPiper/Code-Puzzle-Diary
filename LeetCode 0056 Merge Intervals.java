/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) { // 34, 82
        if (intervals == null || intervals.size() == 0)
            return intervals;
        List<Interval> ans = new LinkedList<Interval>();
        Collections.sort(intervals, (i1, i2) -> i1.start - i2.start);
        Interval cur = intervals.get(0);
        for (Interval i : intervals) {
            if (i.start > cur.end) { // not overlap
                ans.add(cur);
                cur = i;
            } else { // overlap
                cur.end = Math.max(i.end, cur.end);
            }
        }
        ans.add(cur);
        return ans;
    }
}