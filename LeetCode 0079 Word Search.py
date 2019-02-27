class Solution(object): # 51%, 100%
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        if not word: return True
        def dfs(i, j, depth): # depth first search
            if depth == len(word): return True # max depth reached, question answer found
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): return False # index out of range
            if word[depth] != board[i][j]: return False # this step is incorrect
            # This step is correct, walk next step (4 directions)
            tmp = board[i][j] # save current step val for next step
            board[i][j] = "##" # avoid re-visit
            depth += 1
            res = dfs(i - 1, j, depth) or dfs(i, j - 1, depth) or dfs(i + 1, j, depth) or dfs(i, j + 1, depth)
            board[i][j] = tmp
            return res
        
        for i in range(len(board)): 
            for j in range(len(board[i])): # O(mn) scan for starter
                if board[i][j] == word[0]: # found starting letter
                    if dfs(i, j, 0): return True
        return False