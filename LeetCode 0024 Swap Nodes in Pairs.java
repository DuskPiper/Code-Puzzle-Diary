/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 99.99, 24
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode start = new ListNode(0);
        start.next = head;
        ListNode prev = start;
        ListNode first = head;
        ListNode second = head.next;
        ListNode after;
        while (true) {
            after = second.next;
            // Now swap(first, second);
            prev.next = second;
            second.next = first;
            first.next = after;
            // Now check if end loop or resume
            if (after == null || after.next == null) {
                break;
            } else {
                prev = first;
                first = after;
                second = after.next;
            }
        }
        return start.next;
    }
}