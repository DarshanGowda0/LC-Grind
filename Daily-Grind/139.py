from heapq import *

class MyString:
    def __init__(self, s):
        self.s = s
        
    def __lt__(self, other):
        return self.s > other.s
    
    def __eq__(self, other):
        return self.s == other.s

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # construct a normal trie
        # store best three suggestions on each node
        
        def insertToHeap(node, product):
            # insert the word if its smaller than any three
            if '@' not in node:
                node['@'] = [MyString(product)]
            else:
                node['@'].append(MyString(product))
                heapify(node['@'])
                if len(node['@']) > 3:
                    heappop(node['@'])
            # print("product {} heap {}".format(product, [mystring.s for mystring in node['@']]))
        
        trie = {}
        
        for product in products:
            node = trie
            # print('product', product)
            insertToHeap(node, product)
            for c in product:
                if c not in node:
                    node[c] = {}
                node = node[c]
                insertToHeap(node, product)
                # print('at {} heap {}'.format(c, node['@']))
            node['$'] = product
        
        # print(trie)
        res = []
        node = trie
        for c in searchWord:
            if c in node:
                node = node[c]
                li = sorted([myString.s for myString in node['@']])
                res += li,
            else:
                node = {}
                res += [],
            
        
        return res
            
                