class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        def backtrack(first = 0, curr = []):
            if len(curr) == k:  
                self.combinations.append(''.join(curr[:]))
                return 
            for i in range(first, n):
                curr.append(characters[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack()
        self.combinations.reverse()

    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations