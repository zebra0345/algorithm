import sys

input = sys.stdin.readline

pair = []
T = int(input())

max_n = max_m = 0
for _ in range(T):
    n, m = map(int, input().split())
    max_n = max(n, max_n)
    max_m = max(m, max_m)
    pair.append((n, m))

dp = [[0] * (max_m + 1) for _ in range(max_n+1)]

for i in range(0, max_m+1):
    dp[0][i] = 1

for i in range(1, max_n+1):
    for j in range(1, max_m+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

for n, m in pair:
    print(dp[n][m])
