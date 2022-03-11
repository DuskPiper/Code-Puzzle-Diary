class Solution: # 47, 80
    def match(self, slot, word):
        for i in range(len(slot)):
            if slot[i] != ' ' and slot[i] != word[i]:
                return False
        return True
    
    def assessRow(self, row, word):
        wordReversed = word[::-1]
        spaceCounter = 0
        for i in range(len(row)):
            if row[i] == '#':
                spaceCounter = 0
            else:
                spaceCounter += 1
                if spaceCounter == len(word):
                    if i == len(row) - 1 or row[i + 1] == '#':
                        # we have a suitable slot
                        slot = row[i - len(word) + 1 : i + 1]
                        if self.match(slot, word) or self.match(slot, wordReversed):
                            return True
    
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        for row in board:
            if self.assessRow(row, word):
                return True
        for c in range(len(board[0])):
            column = [row[c] for row in board]
            if self.assessRow(column, word):
                return True
        return False
    