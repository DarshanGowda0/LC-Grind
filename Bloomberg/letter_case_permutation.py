class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        res = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                for j in range(len(res)):
                    copyString = list(res[j])
                    copyString[i] = copyString[i].swapcase()
                    res += "".join(copyString),
                    
        return res
                    
                    