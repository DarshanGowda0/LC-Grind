class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = word

    def search(self, word):
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '$' in node

