class Solution: # 61, 91
    def longestWord(self, words: List[str]) -> str:
        # 这题很坑，必须要从单个字母开始才算
        visited = set([""])
        for w in sorted(words, key=len):
            if w[:-1] in visited:
                visited.add(w)
        return min(visited, key=lambda w : (-len(w), w))
        