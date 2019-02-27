class MyCalendarTwo { // 80%
    List<int[]>books; // 所有成功的book，int[start, end]
    MyCalendarOne overlaps; // 用MyCalendarOne的思路存储overlap：虽book可重叠，但重叠部分不可重叠，即overlap的性质同前一题的book
    List<int[]>currentOverlaps; // 当前book检测时碰到的overlap暂存收集器，收集好overlap，一旦成功则全存进MyCalendarOne.overlaps

    public MyCalendarTwo() {
        this.books = new ArrayList<int[]>();
        this.overlaps = new MyCalendarOne();
        this.currentOverlaps = new ArrayList<int[]>();
    }
    
    public boolean book(int start, int end) {
        this.currentOverlaps.clear(); // 清空上一轮收集的暂存overlap
        for (int[] book : this.books) { // 挨个检测是否存在overlap
            int overlapStart = Math.max(start, book[0]);
            int overlapEnd = Math.min(end, book[1]);
            if (overlapStart < overlapEnd) { // Overlap happens, overlap = [overlapStart, overlapEnd]
                if (!this.overlaps.bookOverlap(overlapStart, overlapEnd)) { // Tripple-overlap happens
                    return false;
                } else { // 当前检测存在overlap但是不存在Tripple-overlap，是合法的 // 合法 = 不产生tripple-overlap
                    this.currentOverlaps.add(new int[]{overlapStart, overlapEnd}); // 收集该合法的overlap，如overlap均合法则该函数返true
                }
            }
        }
        // 只有所有overlap均合法的时候，他们才是有效的，一旦for循环内有一个不合法，该轮所有overlap均无效
        // 所有overlap均合法（均不产生tripple-overlap），接下来完成book
        this.books.add(new int[]{start, end}); 
        for (int[] currentOverlap : this.currentOverlaps) { // 统一存储收集来的合法overlap（已保证不会再产生overlap）
            this.overlaps.addOverlap(currentOverlap[0], currentOverlap[1]);
        }
        return true;
    }
    
    private class MyCalendarOne { //上一题的解题思路复制改编来的
        TreeMap<Integer, Integer> overlaps; // 合法overlap，不允许再产生进一步overlap
        
        public MyCalendarOne() {
            this.overlaps = new TreeMap<Integer, Integer>();
        }
        
        public boolean bookOverlap(int start, int end) {
            Integer floorKey = this.overlaps.floorKey(start);
            if (floorKey != null && this.overlaps.get(floorKey) > start) { // New overlap overlaps existing overlaps at left
                return false;
            }
            Integer ceilingKey = this.overlaps.ceilingKey(start);
            if (ceilingKey != null && ceilingKey < end) { // New overlap overlaps existing overlaps at left
                return false;
            }
            // New overlap not overlapped with old overlaps
            // this.overlaps.put(start, end); // 不在这里添加，否则有bug添加到合法的overlap whose sibling是非法的（也就是无效的合法overlap）
            return true;
        }
        
        public void addOverlap(int start, int end) { // 从这里统一添加合法有效overlap
            this.overlaps.put(start, end);
        }
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */