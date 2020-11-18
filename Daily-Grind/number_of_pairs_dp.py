def numberOfPairs(nums, target):
    
    def recur(nums, idx, remainingSum):
        # we found a subArray which exhausted the target, so that's 1 way
        if remainingSum == 0:
            return 1

        # when idx reaches end of the array and the remainingSum is non-zero
        if idx == len(nums):
            return 0

        count1 = 0
        # include the current number
        if nums[idx] <= remainingSum:
            count1 = recur(nums, idx + 1, remainingSum - nums[idx])

        #ignore the current number
        count2 = recur(nums, idx + 1, remainingSum)

        # total number of ways
        return count1 + count2

    return recur(nums, 0, target)

def numberOfPairsMemoized(nums, target):

    # we can remove the overlapping subproblems if we momize the solution with chaning variables,
    # i.e remamingSum and idx in our case, we could either use a dictionary or array for this
    
    def recur(nums, idx, remainingSum, dp):

        if remainingSum == 0:
            return 1

        if idx == len(nums):
            return 0

        _key = (idx, remainingSum)
        if _key not in dp:

            count1 = 0
            if nums[idx] <= remainingSum:
                count1 = recur(nums, idx + 1, remainingSum - nums[idx], dp)

            count2 = recur(nums, idx + 1, remainingSum, dp)
            dp[_key] = count1 + count2

        return dp[_key]

    return recur(nums, 0, target, {})

# from the above solution, we can get the recurrence relationship and convert it into an iterative solution
# recurrence relation - dp[idx][rSum] = dp[idx - 1][rSum - nums[idx]] + dp[idx - 1][rSum]
def numberOfPairsBottomUp(nums, target):
    n = len(nums)
    # dp array with idx, rSum as indices
    dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

    # base case from recursive soln, when sum is 0, count is 1
    for idx in range(n):
        dp[idx][0] = 1

    # base case to handle idx 0, becuase recurrence relation refers to [idx - 1]
    for rSum in range(1, target + 1):
        # if its a single number, then count is 1 only when number == target
        dp[0][rSum] = 1 if nums[0] == rSum else 0

    for idx in range(1, n):
        for remainingSum in range(1, target+1):
            # include
            count1 = 0
            if nums[idx] <= remainingSum:
                count1 = dp[idx - 1][remainingSum - nums[idx]]
            # ignore
            count2 = dp[idx - 1][remainingSum]
            
            dp[idx][remainingSum] = count1 + count2
    
    return dp[n - 1][target]

if __name__ == "__main__":
    nums = [1, 199, 199, 1, 198, 180, 20, 10, 10, 5, 5, 200]
    # print(nums)
    res = numberOfPairsBottomUp(nums, 200)
    print(res)

