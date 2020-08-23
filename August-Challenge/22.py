class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # two pointer technique
        # fast ptr that scans the array and slow that maintains the even border
        # 3 2 1 4 - 2 3 1 4 - 2 4 1 3
        # 1 2 3 4 5 - 2 1 3 4 5 - 2 4 3 1 5
        # 2 4 6 1 3 - 2 4 6 1 3
        if not A:
            return A
        
        slow, fast = -1, 0
        while fast < len(A):
            # print(slow, fast)
            if A[fast] % 2 == 0:
                A[slow+1], A[fast] = A[fast], A[slow+1]
                slow += 1
            fast += 1
            
        return A
