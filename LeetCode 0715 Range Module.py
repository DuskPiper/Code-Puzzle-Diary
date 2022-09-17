import bisect # 80 62

class RangeModule:

    def __init__(self):
        self.track = []
        
    def addRange(self, left: int, right: int) -> None:
        if not self.track:
            self.track = [left, right]
            return
        
        leftIndex = bisect.bisect_left(self.track, left)
        rightIndex = bisect.bisect_right(self.track, right)
        
        if leftIndex % 2 == 0:  # "left" is not in an existing range
            newLeftPart = self.track[:leftIndex] + [left]
        else: # "left" is in an existing range
            newLeftPart = self.track[:leftIndex]
            
        if rightIndex % 2 == 0: # "right" is not in an existing range
            newRightPart = [right] + self.track[rightIndex:]
        else: # "right" is in an existing range
            newRightPart = self.track[rightIndex:]
        
        self.track = newLeftPart + newRightPart

            
            
    def queryRange(self, left: int, right: int) -> bool:
        if not self.track: return False
        
        leftIndex = bisect.bisect_right(self.track, left)
        rightIndex = bisect.bisect_left(self.track, right)
        
        return leftIndex % 2 == 1 and rightIndex == leftIndex
        

    def removeRange(self, left: int, right: int) -> None:
        if not self.track: return
        
        leftIndex = bisect.bisect_left(self.track, left)
        rightIndex = bisect.bisect_right(self.track, right)
        
        if leftIndex % 2 == 0:  # "left" is not in an existing range
            newLeftPart = self.track[:leftIndex]
        else: # "left" is in an existing range
            newLeftPart = self.track[:leftIndex] + [left]
            
        if rightIndex % 2 == 0: # "right" is not in an existing range
            newRightPart = self.track[rightIndex:]
        else: # "right" is in an existing range
            newRightPart = [right] + self.track[rightIndex:]
            
        self.track = newLeftPart + newRightPart

        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)