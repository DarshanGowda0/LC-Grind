class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        letterCount, currentLine, res = 0, [], []
        for word in words:
            if letterCount + len(currentLine) + len(word) > maxWidth:
                for i in range(maxWidth - letterCount):
                    currentLine[i % (len(currentLine) - 1 or 1)] += ' '
                res += "".join(currentLine),
                letterCount = 0
                currentLine = []
            letterCount += len(word)
            currentLine += word,
        return res + [' '.join(currentLine).ljust(maxWidth)]