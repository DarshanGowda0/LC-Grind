class UndergroundSystem:

    def __init__(self):
        self.ledger = {}
        self.avg = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ledger[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t1, source = self.ledger[id]
        timeTaken = t - t1
        if (source, stationName) not in self.avg:
            self.avg[(source, stationName)] = (timeTaken, 1)
        else:
            t, n = self.avg[(source, stationName)]
            self.avg[(source, stationName)] = t + timeTaken, n+1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, n = self.avg[(startStation, endStation)]
        return t/n


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)