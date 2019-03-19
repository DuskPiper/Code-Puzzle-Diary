/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) { // 82, 5
        ListNode start = new ListNode(0);
        ListNode ptr = start;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                ptr.next = l2;
                l2 = l2.next;
            }
            else {
                ptr.next = l1;
                l1 = l1.next;
            }
            ptr = ptr.next;
        }
        if (l1 != null)
            ptr.next = l1;
        if (l2 != null)
            ptr.next = l2;
        return start.next;
    }
}