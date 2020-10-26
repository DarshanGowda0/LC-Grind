class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        prefMap = {}
        
        for a, b in pairs:
            prefMap[a] = preferences[a][:preferences[a].index(b)]
            prefMap[b] = preferences[b][:preferences[b].index(a)]
            
        ans = 0
        for i in prefMap:
            for x in prefMap[i]:
                if i in prefMap[x]:
                    ans += 1
                    break
                    
        return ans
           
            