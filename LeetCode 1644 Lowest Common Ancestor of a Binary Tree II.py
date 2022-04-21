# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 5 28
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, target):
            if not root: return None
            if root == target: return [root]
            
            leftRes = dfs(root.left, target)
            if leftRes: return [root] + leftRes
            
            rightRes = dfs(root.right, target)
            if rightRes: return [root] + rightRes
            
            return None
        
        pTrace = dfs(root, p)
        qTrace = dfs(root, q)
        
        if not pTrace or not qTrace: return None
        
        for i in range(min(len(pTrace), len(qTrace))):
            if pTrace[i] != qTrace[i]:
                return pTrace[i - 1]
        return qTrace[-1] if len(pTrace) > len(qTrace) else pTrace[-1]
                           