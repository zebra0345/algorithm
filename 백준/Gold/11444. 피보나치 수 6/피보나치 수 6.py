n = int(input())

base_mat = [[1, 1], [1, 0]]


def multiply_matrix(mat1, mat2):
    res = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000000007
    return res


def power_mat(a, n):
    if n == 1:
        return a
    
    half = power_mat(a, n // 2)
    
    if n % 2 == 0:
        return multiply_matrix(half, half)
    
    else:
        return multiply_matrix(multiply_matrix(half, half), a)
    
if n == 1:
    print(1)
    
    
else:
    result = power_mat(base_mat, n)
    print(result[0][1])