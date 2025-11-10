import math

max_val = 10 ** 12
limit = int(math.sqrt(max_val))

is_prime = [True] * (limit+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, limit + 1, i):
            is_prime[j] = False

primes = [i for i, v in enumerate(is_prime) if v]

min_val, max_val = map(int, input().split())
length = max_val - min_val + 1
check = [False] * length  # False면 아직 제곱수로 안 나눠진 수

for p in primes:
    square = p * p
    start = ((min_val + square - 1) // square) * square
    for j in range(start, max_val + 1, square):
        check[j - min_val] = True  

# 제곱수로 나누어지지 않은 수의 개수
print(check.count(False))
