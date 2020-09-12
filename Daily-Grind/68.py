class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
        # sort by height
        # [7,0][7,1][6,1][5,0][5,2][4,4]
        # [5,0][7,0][5,2][6,1][4,4][7,1]
        
        people.sort(key=lambda x: (-x[0],x[1]))
        res = []
        for h, k in people:
            res.insert(k,[h,k])
        return res