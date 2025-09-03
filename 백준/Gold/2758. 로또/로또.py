import sys
input = sys.stdin.readline

T = int(input().strip())

pairs = []
max_pick = 0   # 최대 n (뽑는 개수)
max_val  = 0   # 최대 m (숫자 범위)

for _ in range(T):
    n, m = map(int, input().split())  # n=뽑는 개수, m=숫자 범위(1..m)
    pairs.append((n, m))
    max_pick = max(max_pick, n)
    max_val  = max(max_val,  m)

# dp[i][j]: 1..j에서 i개 뽑는 경우의 수
dp = [[0] * (max_val + 1) for _ in range(max_pick + 1)]

# 아무것도 안 뽑는 경우
for j in range(max_val + 1):
    dp[0][j] = 1

for i in range(1, max_pick + 1):
    for j in range(1, max_val + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j // 2]

result = []
for n, m in pairs:
    result.append(str(dp[n][m]))
print("\n".join(result))
