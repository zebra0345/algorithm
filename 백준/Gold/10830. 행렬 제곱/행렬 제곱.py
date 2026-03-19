import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
B = int(data[1])

A = []
idx = 2
for _ in range(N):
    A.append([int(x) for x in data[idx:idx+N]])
    idx += N

def multi_matrix(mat1, mat2, n):
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000
    
    return result

def power_mat(a, b, n):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a
    
    temp = power_mat(a, b // 2, n)
    
    if b % 2 == 0:
        return multi_matrix(temp, temp, n)
    else:
        return multi_matrix(multi_matrix(temp, temp, n), a, n)
    
    
result = power_mat(A, B, N)

for row in result:
    print(" ".join(map(str, row)))