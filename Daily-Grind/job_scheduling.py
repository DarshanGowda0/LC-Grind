class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # greedy
        # sort by profit/time? and place it from the end
        
        #  1   2    3   4   6
        #  3   5   10   6   9
        # 20  20  100  70  60
        # 6.  6.   1.  35  20 
        
        # doesn't work, use dp with 0/1 knapsack technique
        """TLE n^2
        def dfs(arr, prevEnd, idx, dp={}):
            if idx >= len(arr):
                return 0
            
            key = (idx, prevEnd)
            if key not in dp:
                # include
                include = 0
                if prevEnd == -1 or arr[idx][0] >= prevEnd:
                    include = arr[idx][2] + dfs(arr, arr[idx][1],idx+1, dp)
                
                # skip
                skip = dfs(arr, prevEnd, idx+1, dp)
                
                dp[key] = max(include, skip)
                # print("include {} skip {} at {}".format(include, skip, idx))
            return dp[key]
        
        arr = list(zip(startTime, endTime, profit))
        arr.sort(key = lambda x: x[0])
        # print(arr)
        
        return dfs(arr, -1, 0)
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        hp = []
        total = 0

        for s,e,p in jobs:
            while hp and hp[0][0] <= s:
                popd = heappop(hp)
                total = max(total, popd[1])

            heappush(hp, (e, p + total))

        while hp:
            popd = heappop(hp)
            total = max(total, popd[1])

        return total
        