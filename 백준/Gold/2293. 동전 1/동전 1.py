import sys
input = sys.stdin.readline
# N = 동전의 종류, K = 가치의 합
N, K = map(int, input().split())

coin_list = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for coin in coin_list:
    for i in range(coin, K+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[K])