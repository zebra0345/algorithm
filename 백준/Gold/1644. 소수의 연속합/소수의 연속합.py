import math

N = int(input())

if N == 1:
    print(0)
    exit()

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, N + 1) if is_prime[i]]

left = 0
right = 0
count = 0
temp_sum = 0

while True:
    if temp_sum >= N:
        if temp_sum == N:
            count += 1
        temp_sum -= primes[left]
        left += 1
    else:
        if right == len(primes):
            break
        temp_sum += primes[right]
        right += 1

print(count)
