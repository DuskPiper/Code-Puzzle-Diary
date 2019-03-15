# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root): // 99.8, 91
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node, parentSum):
            curSum = parentSum * 10 + node.val
            if not node.left and not node.right: return [curSum] # node is a leaf
            ans = []
            if node.left: ans += dfs(node.left, curSum)
            if node.right: ans += dfs(node.right, curSum)
            return ans
        
        if not root: return 0
        return sum(dfs(root, 0))
                