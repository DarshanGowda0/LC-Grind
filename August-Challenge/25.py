from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque()
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node

# second attempt

from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        # consturct trie and store the words in reverse order
        # keep track of incoming char stream and return True if any of the substring is found in trie
        self.trie = {}
        self.charStream = deque([])
        
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word
        
    def query(self, letter: str) -> bool:
        self.charStream.appendleft(letter)
        node = self.trie
        for c in self.charStream:
            # print(c, node)
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)