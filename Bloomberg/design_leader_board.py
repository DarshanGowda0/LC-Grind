from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.hMap = defaultdict(int)        

    def addScore(self, playerId: int, score: int) -> None:
        self.hMap[playerId] += score

    def top(self, K: int) -> int:
        return sum(sorted(self.hMap.values(), key = lambda x: -x)[:K])

    def reset(self, playerId: int) -> None:
        self.hMap[playerId] = 0