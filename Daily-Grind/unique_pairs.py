from collections import defaultdict
from random import randint

def numberOfPairs(nums, target):
    mDict = defaultdict(int)

    for num in nums:
        if num < target:
            mDict[num] += 1
    print(mDict)

    count = 0
    hCount = 0
    for key, val in mDict.items():
        # edge case for half
        if target - key == key and target - key in mDict:
            hCount += (val * (val - 1)) // 2
        elif target - key in mDict:
            print(key)
            count += val * mDict[target - key]

    print(count, hCount)
    return count // 2 + hCount

if __name__ == "__main__":
    nums = [randint(1, 10) for i in range(10)]
    # print(nums)
    res = numberOfPairs([3, 8, 7, 7, 1, 5, 10, 9, 6, 7], 8)
    print(res)