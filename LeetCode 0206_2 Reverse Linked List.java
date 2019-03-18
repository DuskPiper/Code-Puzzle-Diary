/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 100, 19
    public ListNode reverseList(ListNode head) {
        /*recursion*/
        if (head == null || head.next == null) 
            return head;
        ListNode next = head.next;
        ListNode newHead = reverseList(head.next);
        next.next = head;
        head.next = null;
        return newHead;
    }
}