# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # 34, 72
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = {} # nested, col -> row -> [nodeVals]
        q = [(root, 0, 0)]
        while q:
            node, row, col = q.pop(0)
            
            if col not in m:
                m[col] = {}
            if row not in m[col]:
                m[col][row] = []
            m[col][row].append(node.val)
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        
        ans = []
        for col in sorted(m.keys()):
            colAns = []
            rows = m[col]
            for row in sorted(rows.keys()):
                colAns += sorted(rows[row])
            ans.append(colAns)
        
        return ans