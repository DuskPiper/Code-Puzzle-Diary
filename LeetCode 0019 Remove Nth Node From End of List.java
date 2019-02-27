/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 100%, 33%
    // 见到linkedlist就要想到fast和slow两个ptr
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //if (head == null || (head.next == null && n == 1)) return null;
        ListNode start = new ListNode(0); // 用了start接在head之前，最后返回start.next，是避免corner case，head也被删了的情况
        start.next = head;
        ListNode fast = start;
        ListNode slow = start;
        for (int i = 0; i <= n; i ++) {
            fast = fast.next;
        }
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return start.next;
    }
}