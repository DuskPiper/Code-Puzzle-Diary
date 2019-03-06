/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int closestValue(TreeNode root, double target) { // 100, 89
        int ans = root.val;
        double distance = Math.abs(root.val - target);
        TreeNode node = root;
        while (node != null) {
            if (distance > Math.abs(node.val - target)) {
                distance = Math.abs(node.val - target);
                ans = node.val;
            }
            if (target > node.val)
                node = node.right;
            else if (target < node.val)
                node = node.left;
            else
                break;
        }
        return ans;
    }
}