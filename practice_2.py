import random

def newMatrix(x,y):
    mat = []
    minv = 0
    maxv = 20
    for i in range(x):
        row = []
        for j in range(y):
            row.append(random.randint(minv, maxv))
        mat.append(row)
    print()
    return mat
def printMatrix(msg, mat):
    print(msg)
    for i in range(len(mat)):
        row = mat[i]
        for j in range(len(row)):
            print(mat[i][j], end=' ')
        print()
    return

def add(mat1, mat2):
    ret = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j]+mat2[i][j])
        ret.append(row)
    print()
    return ret
def minus(mat1, mat2):
    ret = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j]-mat2[i][j])
        ret.append(row)
    print()
    return ret
def multiply(mat1, mat2):
    a=len(mat1)
    b=len(mat2[0])
    ret = [[0]*b for _ in range(a)]

    for i in range(a):
        for j in range(b):
            for k in range(len(mat1[0])):
                ret[i][j] += mat1[i][k]*mat2[k][j]
    print()
    return ret

def scalarAdd(mat, value):
    ret = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[i][j]+value)
        ret.append(row)
    print()
    return ret
def scalarMinus(mat, value):
    ret = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[i][j]-value)
        ret.append(row)
    print()
    return ret
def scalarMultiply(mat, value):
    ret = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[i][j]*value)
        ret.append(row)
    print()
    return ret
def scalarDivide(mat, value):
    ret = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[i])):
            row.append(mat[i][j]/value)
        ret.append(row)
    print()
    return ret

def transpose(mat):
    ret = []
    col_num = max([len(a) for a in mat])
    for i in range(col_num):
        row = []
        for j in range(len(mat)):
            row.append(mat[j][i])
        ret.append(row)
    print()
    return ret
def equal(mat1,mat2):
    print()
    ret = (mat1 == mat2)
    return ret

print("-"*25,"테스트","-"*25)

m1 = newMatrix(3,4)
printMatrix("m1 is:", m1)
m2 = newMatrix(3,4)
printMatrix("m2 is:", m2)
m3 = newMatrix(3,4)
printMatrix("m3 is:", m3)
m4 = newMatrix(4,3)
printMatrix("m4 is:", m4)

m1sa10 = scalarAdd(m1,10)
printMatrix("m1 + 10 is:", m1sa10)
m1sm8 = scalarMinus(m1,8)
printMatrix("m1 - 8 is:", m1sm8)
m2sM5 = scalarMultiply(m2,5)
printMatrix("m2 X 5 is:", m2sM5)
m2sd5 = scalarDivide(m2,5)
printMatrix("m2 / 5 is:", m2sd5)

m1am2 = add(m1,m2)
printMatrix("m1 + m2 is:", m1am2)
m1mm2 = minus(m1,m2)
printMatrix("m1 - m2 is:", m1mm2)
m3Mm4 = multiply(m3,m4)
printMatrix("m3 * m4 is:", m3Mm4)

m1em2 = equal(m1, m2)
print("m1 == m2?", m1em2)
m1t = transpose(m1)
printMatrix("m1 transpose ->", m1t)

print("-"*25,"테스트","-"*25)