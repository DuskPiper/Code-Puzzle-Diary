class HitCounter: # 15, 16

    def __init__(self):
        self.history = []

    def hit(self, timestamp: int) -> None:
        self.history.append(timestamp)
        while self.history[0] <= timestamp - 300:
            self.history.pop(0)

    def getHits(self, timestamp: int) -> int:
        i = 0
        while i < len(self.history) and self.history[i] <= timestamp - 300:
            i += 1
        return len(self.history) - i


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)