/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator { // 60, 5
    Stack<TreeNode> stack;
    Set<TreeNode> visited;

    public BSTIterator(TreeNode root) {
        stack = new Stack<TreeNode>();
        visited = new HashSet<TreeNode>();
        if (root != null)
            stack.push(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        while (stack.peek().left != null && !visited.contains(stack.peek().left))
            stack.push(stack.peek().left);
        TreeNode ans = stack.pop();
        if (ans.right != null)
            stack.push(ans.right);
        visited.add(ans);
        return ans.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */