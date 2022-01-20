# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random

class Solution:
    
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None: # 8% 99%
        
        def getMatch(w0, w1):
            match = 0
            for i in range(6):
                if w0[i] == w1[i]:
                    match += 1
            return match
        
        # 找一个词，它和别的词有尽量多的match
        def getMostVersatileWord(wordlist):
            ans = wordlist[0]
            ansMatches = 0
            for word in wordlist:
                goodMatches = 0
                for word1 in wordlist:
                    goodMatches += getMatch(word, word1)
                if goodMatches > ansMatches:
                    ans = word
                    ansMatches = goodMatches
            return ans
        
        # 莫名其妙的hard 逻辑很直观
        for guess in range(10):
            currentGuess = getMostVersatileWord(wordlist) # 选一个尽量多match的词
            matched = master.guess(currentGuess)
            wordlist = list(filter(lambda word: getMatch(word, currentGuess) == matched, wordlist)) # filter到match一致的词，缩减guesslist
            
            
        