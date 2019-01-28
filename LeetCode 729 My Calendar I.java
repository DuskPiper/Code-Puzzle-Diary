class MyCalendar { // 78%
    TreeMap<Integer, Integer> books; //start和end的键值对

    public MyCalendar() {
        this.books = new TreeMap<Integer, Integer>();
    }
    
    public boolean book(int start, int end) {
        Integer floorKey = this.books.floorKey(start); 
        if (floorKey != null && this.books.get(floorKey) > start) { // Overlapped at left
            return false;
        }
        Integer ceilingKey = this.books.ceilingKey(start);
        if (ceilingKey != null && ceilingKey < end) { // Overlapped at right
            return false;
        }
        // Not overlapped
        this.books.put(start, end);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */