from collections import deque

def solution(matrix):
    # bfs with count of blockers/flag

    m, n = len(matrix), len(matrix[0])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    # node (x, y, hasOneBlocker, distanceFromOrig)
    que = deque([(0,0,False,0)])
    seen = {(0,0):False}
    while que:
        x, y, hasBlocker, dist = que.popleft()
        # print(x,y,hasBlocker,dist)
        if (x,y) == (m-1, n-1):
            return dist+1
        for p, q in directions:
            nx, ny = p+x, q+y
            
            if 0 <= nx < m and 0 <= ny < n:
                # print(nx, ny)
                if (nx, ny) not in seen or (seen[(nx, ny)] and not hasBlocker):
                    if not hasBlocker:
                        blocker = True if matrix[nx][ny] == 1 else False
                        que += (nx, ny, blocker, dist + 1),
                        seen[(nx,ny)] = blocker
                        # print("adding ", (nx,ny))
                    elif matrix[nx][ny] == 0:
                        que += (nx, ny, True, dist+1),
                        seen[(nx, ny)] = True
                        # print("adding ", (nx,ny))
                    # else:
                        # print("ignoring", (nx, ny))
        
    return -1

NO_PATH_VALUE = -1

def test_solution():
    assert solution([
        [0, 1, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 1, 1], 
        [0, 1, 1, 0],
        [0, 1, 1, 0]
    ]) == 8

    assert solution([
        [0, 1, 0, 0, 1], 
        [0, 1, 1, 1, 0], 
        [0, 1, 1, 0, 0], 
        [0, 1, 1, 0, 0]
    ]) == NO_PATH_VALUE
    
    assert solution([
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 1, 0], 
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 9
    
    assert solution([
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 1, 1], 
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 11
    
    assert solution([
        [0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 1, 1], 
        [0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0]
    ]) == 14
    
    assert solution([
        [0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0], 
        [0, 0, 0, 1, 0], 
        [0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0]
    ]) == 13
    
    assert solution([
        [0, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 0]
    ]) == NO_PATH_VALUE
    
    assert solution([
        [0, 1, 1, 0], 
        [0, 0, 0, 1], 
        [1, 1, 0, 0], 
        [1, 1, 1, 0]
    ]) == 7
    
    assert solution([
        [0, 1, 0, 0, 1], 
        [0, 1, 1, 1, 0], 
        [0, 1, 1, 0, 0], 
        [0, 1, 1, 0, 0]
    ]) == NO_PATH_VALUE

    assert solution([
        [0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0]
    ]) == 11

    assert solution([
        [0, 0],
        [0, 0]
    ]) == 3
    
    assert solution([
        [0, 0],
        [0, 1]
    ]) == 3

if __name__ == "__main__":
    test_solution()