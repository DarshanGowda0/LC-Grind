
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