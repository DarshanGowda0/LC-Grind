class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True
        

    def search(self, word: str) -> bool:
        def searchInNode(word, node):
            for idx, c in enumerate(word):
                if c not in node:
                    if c == '.':
                        for child in node:
                            if child != '$' and searchInNode(word[idx+1:], node[child]):
                                return True
                    return False
                else:
                    node = node[c]
            return '$' in node
        
        return searchInNode(word, self.trie)

# second attempt

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        
        node['$'] = word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def searchRecur(word, node):
            for idx, c in enumerate(word):
                if c not in node:
                    
                    if c == '.':
                        for child in node:
                            if child != '$' and searchRecur(word[idx+1:], node[child]):
                                return True
                    return False
                else:
                    node = node[c]
            return '$' in node
        
        return searchRecur(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)