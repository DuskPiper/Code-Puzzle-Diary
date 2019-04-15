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
    public List<List<Integer>> pathSum(TreeNode root, int sum) { // 99.9, 71
        List<List<Integer>> ans = new LinkedList<>();
        pathSumStep(root, sum, new LinkedList<Integer>(), ans);
        return ans;
    }
    
    private void pathSumStep(TreeNode node, int curTarget, LinkedList<Integer> path, List<List<Integer>> ans) {
        if (node == null)
            return;
        path.add(node.val);
        if (node.val == curTarget && node.left == null && node.right == null) { // is leaf and hits target
            ans.add(new LinkedList<Integer>(path)); // register a copy of cur valid path
        } else {
            pathSumStep(node.left, curTarget - node.val, path, ans);
            pathSumStep(node.right, curTarget - node.val, path, ans);
        }
        path.removeLast(); // re-uses "path" to save much time & space
    }
}