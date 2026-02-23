N = int(input())

D = [list(map(int, input().split())) for _ in range(N)]



INF = 100000000
SIZE = 1 << N

dp = [INF] * SIZE
dp[0] = 0

for mas in range(SIZE):
    person = mas.bit_count()
    if person >= N:
        continue
    
    for job in range(N):
        if not (mas & (1 << job)):
            next_mas = mas | (1 << job)
            dp[next_mas] = min(dp[next_mas], dp[mas] + D[person][job])

print(dp[SIZE - 1])