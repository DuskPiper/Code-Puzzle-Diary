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
    public List<List<Integer>> findLeaves(TreeNode root) { // 22, 79
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (root == null)
            return ans;
        Map<TreeNode, Integer> level = new HashMap<TreeNode, Integer>(); // 节点的层级，叶子为0，任何树枝的层级是其儿子层级更大值+1
        Stack<TreeNode> stack = new Stack<TreeNode>();
        int maxLevel = 0;
        
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node.left == null && node.right == null)
                level.put(node, 0);
            else {
                int leftLevel = -1, rightLevel = -1;
                if (node.left != null) {
                    if (level.containsKey(node.left))
                        leftLevel = level.get(node.left);
                    else {
                        stack.push(node);
                        stack.push(node.left);
                        continue;
                    }
                }
                if (node.right != null) {
                    if (level.containsKey(node.right))
                        rightLevel = level.get(node.right);
                    else {
                        stack.push(node);
                        stack.push(node.right);
                        continue;
                    }
                }
                int curLevel = Math.max(leftLevel, rightLevel) + 1; // 算法核心
                maxLevel = Math.max(curLevel, maxLevel);
                level.put(node, curLevel);
            }
        }
        
        for (int i = 0; i < maxLevel + 1; i++)
            ans.add(new LinkedList<Integer>());
        
        for (Map.Entry<TreeNode, Integer> entry : level.entrySet())
            ans.get(entry.getValue()).add(entry.getKey().val);
        
        return ans;
    }
}