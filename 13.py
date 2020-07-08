from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def sortChars(string):
            return "".join(sorted(string))
        
        mDict = defaultdict(list)
        for s in strs:
            _key = sortChars(s)
            mDict[_key] += s,
            
        return mDict.values()