/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // In-place, O(1) spacial complexity
    // Find and reverse second half of list, and compare with the first half
    public boolean isPalindrome(ListNode head) { // 95, 20
        if (head == null)
            return true;
        ListNode fast = head;
        ListNode slow = head;
        ListNode slowPrev = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slowPrev = slow;
            slow = slow.next;
        }
        if (fast == null && slowPrev != null) { // Even-numbered list length 
            slowPrev.next = null;
        }
        
        ListNode secondHalf = reverseLinkedList(slow);
        
        while (head != null) {
            //System.out.println(secondHalf.val);
            if (secondHalf == null || secondHalf.val != head.val)
                return false;
            head = head.next;
            secondHalf = secondHalf.next;
        }
        return secondHalf == null;
    }
    
    public ListNode reverseLinkedList(ListNode head) {
        // Reverses linked list
        ListNode prev = null;
        ListNode cur = head;
        ListNode after;
        
        while (cur != null) {
            after = cur.next;
            cur.next = prev;
            
            prev = cur;
            cur = after;
        }
        
        return prev;
    }
}