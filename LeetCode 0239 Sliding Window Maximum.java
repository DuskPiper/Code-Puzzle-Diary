class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) { // 85, 77
        if (nums == null || nums.length == 0)
            return new int[0];
        Deque<Integer> q = new ArrayDeque<Integer>(); // index 的deque，在后面的循环中我们会保证它是从大到小有序的
        int len = nums.length;
        int[] ans = new int[len - k + 1];
        int ptr = 0;
        
        for (int i = 0; i < len; i++) {
            int cur = nums[i];
            while (!q.isEmpty() && q.peekFirst() < i - k + 1) // 移除虽然最大但是已经在窗口左边以前的
                q.pollFirst();
            while (!q.isEmpty() && nums[q.peekLast()] < cur) // 移除比新元素小的，因为新元素不仅比他们大还比他们消失晚，所以小的都没用
                q.pollLast();
            q.offer(i);
            if (i >= k - 1)
                ans[ptr++] = nums[q.peek()];
        }
        return ans;
    }
}