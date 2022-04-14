class UndergroundSystem: # 34, 50

    def __init__(self):
        self.ongoing = {} # id->(name, t)
        self.ave = {} # (start, end)->(aveTime, numRecord)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        travelTime = t - self.ongoing[id][1]
        startStation = self.ongoing[id][0]
        self.ongoing[id] = None
        oldAve, oldCount = self.ave.get((startStation, stationName), (0, 0))
        newAve = oldAve + ((travelTime - oldAve) / (oldCount + 1))  # (oldAve * oldCount + travelTime) / (oldCount + 1)
        self.ave[(startStation, stationName)] = (newAve, oldCount + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.ave[(startStation, endStation)][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)