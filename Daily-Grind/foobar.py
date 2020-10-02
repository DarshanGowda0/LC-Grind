def findParent(height, node, dp):
    root = 2**height - 1
    if node >= root:
        return -1

    if node in dp:
        return dp[node]

    offset = 0
    size = root

    while True:
        if size == 0:
            return -1
        
        size = size >> 1

        left = offset + size
        right = left + size
        parent = right + 1
        dp[left] = dp[right] = parent

        if node == left or node == right:
            return parent
        
        if node > left:
            offset = left

    return -1

def solution(h, q):
    return [findParent(h, node, {}) for node in q]

if __name__ == "__main__":
    print(solution(3, [7,5,3,5,1]))
