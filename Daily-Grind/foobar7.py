def solution(x, y):
    M, F = int(x), int(y)
    res = 0
    while min(M, F) != 1:
        big, small = max(M, F), min(M, F)
        if not big % small:
            return "impossible"

        res += (big//small)
        M, F = (big%small), small

    big = max(M, F)
    return str(res + big - 1)

if __name__ == "__main__":
    print(solution("4","7"))