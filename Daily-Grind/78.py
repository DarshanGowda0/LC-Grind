from random import choice

class RandomizedSet:

    def __init__(self):
        self.mDict = {}
        self.mList = []
        

    def insert(self, val: int) -> bool:
        if val not in self.mDict:
            self.mDict[val] = len(self.mList)
            self.mList += val,
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.mDict:
            lastElement = self.mList[-1]
            currentIdx = self.mDict[val]
            self.mDict[lastElement] = currentIdx
            self.mList[currentIdx] = lastElement
            self.mList.pop()
            del(self.mDict[val])
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.mList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()