import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        mSet = set(banned)
        
        mDict = collections.defaultdict(int)
        mostCommonWord, count = "", 0
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        for word in paragraph.lower().split(" "):
            if word not in mSet and word != "":
                mDict[word] += 1
                if mDict[word] > count:
                    count, mostCommonWord = mDict[word], word
        
        # print(mDict)
        return mostCommonWord
                