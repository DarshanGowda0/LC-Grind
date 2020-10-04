from fractions import Fraction as frac

def transposeMatrix(m):
    return map(list, zip(*m))

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c] * \
            getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def standardForm(matrix):
    i = 0
    terminatingRows, nonTerminatingRows = [], []
    for idx, row in enumerate(matrix):
        if all([val == 0 for val in row]):
            terminatingRows.append(idx)
        else:
            nonTerminatingRows.append(idx)

    standardRows = terminatingRows + nonTerminatingRows
    standardMatrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(terminatingRows)):
        standardMatrix[i][i] = 1
    
    for i in range(len(terminatingRows), len(standardMatrix)):
        for j in range(len(matrix[0])):
            standardMatrix[i][j] = matrix[standardRows[i]][standardRows[j]]
    
    R, Q = [], []
    for i in range(len(terminatingRows), len(standardMatrix)):
        deno = sum(standardMatrix[i])
        rRow, qRow = [], []
        for j in range(len(standardMatrix[0])):
            if j < len(terminatingRows):
                rRow.append(frac(standardMatrix[i][j], deno))
            else:
                qRow.append(frac(standardMatrix[i][j], deno))
        R.append(rRow)
        Q.append(qRow)

    return R, Q

def invertMatrix(matrix):
    iMatrix = [[frac(0,1) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        iMatrix[i][i] = frac(1,1)

    for x in range(len(matrix)):
        scaler = frac(1,1) / matrix[x][x]
        for j in range(len(matrix)):
            matrix[x][j] *= scaler
            iMatrix[x][j] *= scaler
        for i in list(range(len(matrix)))[0:x] + list(range(len(matrix)))[x+1:]:
            crScaler = matrix[i][x]
            for j in range(len(matrix)):
                matrix[i][j] = matrix[i][j] - crScaler * matrix[x][j]
                iMatrix[i][j] = iMatrix[i][j] - crScaler * iMatrix[x][j]
    return iMatrix

def getInverse(Q):
    # return F = (I - Q) ^ -1
    matrix = [[0 for _ in range(len(Q[0]))] for _ in range(len(Q))]
    for i in range(len(Q)):
        for j in range(len(Q[0])):
            if i == j:
                matrix[i][j] = 1 - Q[i][j]
            else:
                matrix[i][j] = 0 - Q[i][j]
    return getMatrixInverse(matrix)
    
def multiplyMatrices(A, B):
    return [[sum(a*b for a,b in zip(aRow,bCol)) for bCol in zip(*B)] for aRow in A]

def solution(matrix):
    R, Q = standardForm(matrix)
    if len(R) == 0 or len(matrix) == 1:
        return [1,1]
    F = getInverse(Q)
    FR = multiplyMatrices(F, R)
    deno = max([num.denominator for num in FR[0]])
    return [num.numerator*(deno/num.denominator) for num in FR[0]] + [deno]


if __name__ == "__main__":
    # m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    # m = [
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0]
    #     ]
    m = [[0,0,0,0]]
    print(solution(m))


"""
from fractions import Fraction

def transform(mat):
    rowSum = list(map(sum, mat))
    statesBool = list(map(lambda x: x == 0, rowSum))
    indices = set([i for i, x in enumerate(statesBool) if x])
    tempMat = []
    for i in range(len(mat)):
        tempMat.append(list(map(lambda x: Fraction(0, 1) if(rowSum[i] == 0) else simplify(x, rowSum[i]), mat[i])))
    transMatrix = []
    terminatingStates = []
    for i in range(len(tempMat)):
        if i not in indices:
            transMatrix.append(tempMat[i])
        else:
            terminatingStates.append(tempMat[i])
    transMatrix.extend(terminatingStates)
    resMatrix = []
    for i in range(len(transMatrix)):
        resMatrix.append([])
        extend_mat = []
        for j in range(len(transMatrix)):
            if j not in indices:
                resMatrix[i].append(transMatrix[i][j])
            else:
                extend_mat.append(transMatrix[i][j])
        resMatrix[i].extend(extend_mat)
    return [resMatrix, len(terminatingStates)]

def getQR(mat, lenOfR):
    lenOfQ = len(mat) - lenOfR
    Q, R = [], []
    for i in range(lenOfQ):
        Q.append([int(i==j)-mat[i][j] for j in range(lenOfQ)])
        R.append(mat[i][lenOfQ:])
    return Q, R

def invertMatrix(mat):
    res = transposeMatrix(mat)
    invMatrix = []
    for i in range(len(res)):
        values = [Fraction(int(i==j), 1) for j in range(len(mat))]
        invMatrix.append(eliminate(res, values))
    return invMatrix

def nultiplyMatrices(A, B):
    res = []
    for i in range(len(A)):
        res.append([])
        for j in range(len(B[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
    return res

def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def simplify(x, y):
    g = gcd(x, y)
    return Fraction(long(x/g), long(y/g))

def lcm(x, y):
    return long(x*y/gcd(x,y))

def copyMatrix(mat):
    temp = []
    for i in range(len(mat)):
        temp.append([])
        for j in range(len(mat[i])):
            temp[i].append(Fraction(mat[i][j].numerator, mat[i][j].denominator))
    return temp

def eliminate(m, values):
    mat = copyMatrix(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Not allowed!')
        mat[i], mat[index] = mat[index], mat[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i]/mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(mat))]
    for i in range(len(mat)):
        index = len(mat) -1 -i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index]/mat[index][index]
    return res

def transposeMatrix(mat):
    res = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                res.append([])
            res[j].append(mat[i][j])
    return res

def solution(mat):
    res = transform(mat)
    if res[1] == len(mat):
        return [1, 1]
    Q, R = getQR(*res)
    inv = invertMatrix(Q)
    res = nultiplyMatrices(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: int(x.numerator*l/x.denominator), row))
    res.append(int(l))
    return res

if __name__ == "__main__":
    # m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    # m = [[0,0,0,0]]
    print(solution(m))
"""