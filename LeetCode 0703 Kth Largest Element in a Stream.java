class KthLargest { // 85, 44
    PriorityQueue<Integer> pq;
    int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        pq = new PriorityQueue<Integer>();
        for (int num : nums) {
            pq.offer(num);
            if (pq.size() > k)
                pq.poll();
        }
    }
    
    public int add(int val) {
        pq.offer(val);
            if (pq.size() > k)
                pq.poll();
        return pq.peek();
    }
}