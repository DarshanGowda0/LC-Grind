class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = S.split()
        for idx, word in enumerate(words):
            temp = ""
            if word[0].lower() in vowels:
                temp += word[:]+"ma"
            else:
                temp += word[1:]+word[0]+"ma"
            temp += "".join(['a' for _ in range(idx+1)])
            
            res += temp,
            
        return " ".join(res)
            