class Solution: # 17, 57
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLen = len(beginWord)
        wordList = set(wordList)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        q = set([beginWord])
        visited = set()
        step = 0
        while q:
            step += 1
            nextRound = set()
            for word in q:
                visited.add(word)
                if word == endWord:
                    return step
                for i in range(wordLen):
                    for letter in letters:
                        changed = word[:i] + letter + word[i + 1:]
                        if changed not in visited and changed not in nextRound and changed in wordList:
                            nextRound.add(changed)
            q = nextRound
        return 0
                        