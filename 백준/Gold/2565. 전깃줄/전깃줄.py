N = int(input())

wires = [tuple(map(int, input().split())) for _ in range(N)]

wires.sort()

B = [b for _, b in wires]

dp = [1] * N
for i in range(N):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

lis_len = max(dp)
print(N - lis_len)