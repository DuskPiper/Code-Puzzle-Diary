class Solution { // 40%, 73%
    public boolean canAttendMeetings(Interval[] intervals) {
        if (intervals == null || intervals.length <= 1) return true;
        Arrays.sort(intervals, (i1, i2) -> i1.start - i2.start);
        /* //wastes memory
        int endTime = -1;
        for (Interval interval : intervals) {
            if (endTime > interval.start) return false;
            endTime = interval.end;
        }
        */
        for (int i = 1; i < intervals.length; i ++) {
            if (intervals[i].start < intervals[i - 1].end) return false;
        }
        return true;
    }
}