MOD = 1000000

def mat_mult(A, B):
    return [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
        ]
    ]

def mat_pow(mat, n):
    if n == 1:
        return mat

    half = mat_pow(mat, n//2)

    result = mat_mult(half, half)

    if n % 2 == 1:
        result = mat_mult(result, mat)

    return result

def fibonacci(n):
    if n == 0:
        return 0

    base = [[1, 1],
            [1, 0]]

    result = mat_pow(base, n)
    return result[0][1]

n = int(input())
print(fibonacci(n) % 1000000)