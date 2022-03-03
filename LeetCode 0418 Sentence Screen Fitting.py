class Solution: # 58%, 92%
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = '_'.join(sentence) + '_' # _ is space
        ptr = 0
        for r in range(rows):
            ptr += cols - 1
            if s[ptr % len(s)] == '_': # This row ends at a space
                ptr += 1 # Move to start of next word
            elif s[ptr % len(s) + 1] == '_': # This row ends at a word-end
                ptr += 2 # Move to start of next word
            else: # This row ends at mid of a word
                while ptr and s[ptr % len(s) - 1] != '_': # Move to start of cur word, including a corner case where a word is longer than cols
                    ptr -= 1
        return ptr // len(s)
            