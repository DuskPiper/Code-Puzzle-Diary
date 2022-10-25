# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # 45 70
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        signature = {}  # Sign string -> node
        
        def signNode(node):
            if not node:
                return 'N'
            leftSign = signNode(node.left)
            rightSign = signNode(node.right)
            nodeSign = str(node.val) + 'L' + leftSign + 'R' + rightSign  # Pre-order. Postorder should also work, but not inorder
            
            if nodeSign not in signature:
                signature[nodeSign] = [node]
            else:
                signature[nodeSign].append(node)
            return nodeSign
        
        signNode(root)
                
        return [v[0] for v in signature.values() if len(v) > 1]