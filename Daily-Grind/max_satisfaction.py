class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # dp with idx and time
        
        def recur(arr, idx, time, dp):
            if idx >= len(arr):
                return 0
            
            key = (idx, time)
            if key not in dp:
                # include
                c1 = arr[idx] * time + recur(arr, idx+1, time + 1, dp)

                # skip
                c2 = recur(arr, idx+1, time, dp)

                dp[key] = max(c1, c2)
                
            return dp[key]
        
        dp = {}
        ans = recur(sorted(satisfaction), 0, 1, dp)
        # print(dp)
        return ans
    