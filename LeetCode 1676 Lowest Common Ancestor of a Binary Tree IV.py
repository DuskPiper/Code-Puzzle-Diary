# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): # 100 53
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def lca(root, nodes):
            if not root: return None
            if root in nodes: return root
            
            leftAns = lca(root.left, nodes)
            rightAns = lca(root.right, nodes)
            
            if leftAns and rightAns: return root # tragets fall into either side
            if leftAns: return leftAns # tragets fall into left side
            if rightAns: return rightAns
            return None
        return lca(root, nodes)
            