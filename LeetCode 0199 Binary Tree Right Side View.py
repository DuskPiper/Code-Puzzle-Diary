# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 19, 98
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        nextRound = [root]
        while nextRound:
            curRound = list(nextRound)
            nextRound = []
            ans.append(curRound[0].val)
            for node in curRound:
                if node.right: nextRound.append(node.right)
                if node.left: nextRound.append(node.left)
        return ans
        