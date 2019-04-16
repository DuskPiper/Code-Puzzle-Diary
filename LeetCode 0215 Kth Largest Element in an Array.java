class Solution {
    public int findKthLargest(int[] nums, int k) { // 64, 94
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for (int num : nums) {
            pq.offer(num);
            if (pq.size() > k)
                pq.poll();
        }
        return pq.peek();
    }
}