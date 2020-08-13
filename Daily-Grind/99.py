from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counter = Counter(nums1)
        counter2 = Counter(nums2)
        
        res = []
        for k, val in counter.items():
            if k in counter2:
                for _ in range(min(val, counter2[k])):
                    res += k,
                    
        return res