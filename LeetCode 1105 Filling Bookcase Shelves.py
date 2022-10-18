class Solution: # 68 94
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [math.inf] * len(books)  # best answer at 'i'
        
        for i, (w, h) in enumerate(books):
            if i == 0:
                dp[i] = h
                continue
                
            dp[i] = dp[i-1] + h
            rowWidth, rowHeight = w, h   # always keep new book at new row of shelf
            
            for j in range(i-1, -1, -1):  # check backwards if we can move earlier books to this new row. NOTE that the sequence of books shouldn't change
                jw, jh = books[j]
                rowWidth += jw
                if rowWidth > shelfWidth: #  new row is full, stop here
                    break
                rowHeight = max(rowHeight, jh)  # add book to new row, update new row height
                dp[i] = min(dp[i], rowHeight + (dp[j-1] if j else 0))  ## The best answer is either 1.move book to new row 2.not move book to new row
                
        return dp[-1]
                