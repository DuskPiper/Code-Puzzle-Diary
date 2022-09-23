class Solution: # 9, 81
    def shortestWay(self, source: str, target: str) -> int:
        
        def movePtr():
            self.sPtr += 1
            if self.sPtr == len(source): 
                    self.sPtr = 0
                    self.counter += 1
        
        sourceChars = set([c for c in source])
        for c in target:
            if c not in sourceChars:
                return -1
            
        self.counter = 0
        self.sPtr = 0
        for c in target:
            while c != source[self.sPtr]:
                movePtr()
            movePtr()
                    
        if self.sPtr != 0: 
            self.counter += 1
        return self.counter
            