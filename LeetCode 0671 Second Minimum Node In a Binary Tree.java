/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int findSecondMinimumValue(TreeNode root) { // 100, 5
        if (root == null || root.left == null) { // No child at all
            return -1;
        } 
        int ans = -1;
        // BFS
        final Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            final TreeNode cur = q.poll();
            if (cur.left != null) {
                q.offer(cur.left);
                q.offer(cur.right);
            }
            if (cur.val != root.val) {
                ans = ans == -1 ? cur.val : Math.min(ans, cur.val);
            }
        }
        
        return ans;
    }
}
