/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 100, 30
    public ListNode reverseList(ListNode head) {
        /*iteration*/
        if (head == null)
            return null;
        ListNode prev = null;
        ListNode cur = head;
        ListNode next = cur.next;
        while (next != null) {
            cur.next = prev; // most important
            prev = cur;
            cur = next;
            next = next.next;
        }
        cur.next = prev;
        return cur;
    }
}