# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 10, 31
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf
        
        def findRootMax(root):
            if not root: return 0
            leftMax = max(0, findRootMax(root.left))
            rightMax = max(0, findRootMax(root.right))
            connectLeftToRight = leftMax + rightMax + root.val
            self.ans = max(self.ans, connectLeftToRight)
            return max(leftMax, rightMax) + root.val
        
        findRootMax(root)
        return self.ans
        