class Solution { // 90, 68
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<Map.Entry<Integer, Integer>>(new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> entry1, Map.Entry<Integer, Integer> entry2) {
                return entry1.getValue() - entry2.getValue();
            }
        });
        
        for (Map.Entry entry : counter.entrySet()) {
            pq.offer(entry);
            if (pq.size() > k) pq.poll();
        }
        
        List<Integer> ans = new LinkedList<Integer>();
        while (!pq.isEmpty()) {
            ans.add(0, pq.poll().getKey());
        }
        
        return ans;
    }
}