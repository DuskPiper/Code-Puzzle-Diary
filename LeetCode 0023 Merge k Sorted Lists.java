/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 81, 60
    // 用PriorityQueue解决，保证里面有每个list的node(除非list已用光)
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        ListNode start = new ListNode(0);
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>() {
            @Override
            public int compare(ListNode n1, ListNode n2) {
                return n1.val - n2.val;
            }
        });
        
        for (ListNode node : lists) {
            if (node != null) pq.offer(node);
        }
        ListNode ptr = start;
        while (!pq.isEmpty()) {
            ptr.next = pq.poll();// ans.length += 1  ptr指向上次循环结束时的list尾巴
            ptr = ptr.next; // ptr = newly appended node  转换ptr为新尾巴
            if (ptr.next != null) pq.offer(ptr.next); // 每次用掉一个node(最小的一个)，就让他继任者进pq
        }
        return start.next;
    }
}