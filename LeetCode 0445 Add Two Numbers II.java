/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) { // 76, 13
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        
        int carry = 0; // 进位
        int num1, num2;
        ListNode last = null;
        ListNode cur = null;
        while (!s1.isEmpty() || !s2.isEmpty()) {
            // Construct answer from tail to head
            num1 = s1.isEmpty() ? 0 : s1.pop();
            num2 = s2.isEmpty() ? 0 : s2.pop();
            
            cur = new ListNode((num1 + num2 + carry) % 10);
            carry = (num1 + num2 + carry) / 10;
            cur.next = last;
            last = cur;
        }
        if (carry != 0) {
            cur = new ListNode(carry);
            cur.next = last;
        }
        return cur;
    }
    
    
    
    
    
    
    
    
    
    /*
    // Old Answer
    // Reverse lists -> fit into LeetCode 2 -> reverse back
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) { // 17
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        return reverseList(addTwoNumbersI(l1, l2));
    }
    
    public ListNode reverseList (ListNode l) {
        // Reverse List of Nodes
        ListNode ans = null;
        ListNode next = null;
        while (l != null) {
            next = l.next;
            l.next = ans;
            ans = l;
            l = next;
        }
        return ans;
    }
    
    public ListNode addTwoNumbersI(ListNode l1, ListNode l2) {
        // LeetCode 2 solution 
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
    */
}