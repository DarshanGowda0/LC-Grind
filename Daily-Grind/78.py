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

# second attempt
from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            lastEle = self.arr[-1]
            idx = self.dict[val]
            self.dict[lastEle] = idx
            self.arr[idx] = lastEle
            
            del self.dict[val]
            self.arr.pop()
            
            return True
        
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()