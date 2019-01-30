/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution { // 92%
    // 完全模拟多位数加法运算
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean carry = false; // 进位与否
        int sum = l1.val + l2.val;
        if (sum >= 10) {
            sum -= 10;
            carry = true;
        }
        ListNode ans = new ListNode(sum);
        ListNode ptr = ans;
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != null || l2 != null || carry) { // 在loop里逐位检查相加
            if (l1 == null && l2 == null) { // CASE1 final add, loop to be ended
                if (carry) { // final carry
                    ptr.next = new ListNode(1);
                    carry = false;
                }
                break;
            } else if (l1 == null) { // CASE2 l1 fully added but l2 remains (l2 >> l1)
                if (carry) { // carry from last loop
                    sum = l2.val + 1;
                    if (sum == 10) { // one more carry
                        sum = 0;
                    } else {
                        carry = false;
                    }
                    ptr.next = new ListNode(sum);
                } else {
                    ptr.next = new ListNode(l2.val);
                }
                ptr = ptr.next;
                l2 = l2.next;
            } else if (l2 == null) { // CASE3 l2 fully added but l1 remains (l1 >> l2)
                if (carry) {
                    sum = l1.val + 1;
                    if (sum == 10) { // one more carry
                        sum = 0;
                    } else {
                        carry = false;
                    }
                    ptr.next = new ListNode(sum);
                } else {
                    ptr.next = new ListNode(l1.val);
                }
                ptr = ptr.next;
                l1 = l1.next;
            } else { // CASE4 add l1 and l2 // most common
                sum = l1.val + l2.val;
                if (carry) sum ++;
                if (sum >= 10) {
                    sum -= 10;
                    carry = true;
                } else {
                    carry = false;
                }
                ptr.next = new ListNode(sum);
                l1 = l1.next;
                l2 = l2.next;
                ptr = ptr.next;
            }
        }
        return ans;
    }
}