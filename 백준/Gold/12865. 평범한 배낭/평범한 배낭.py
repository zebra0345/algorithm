import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = [0] * (N+1)
value = [0] * (N+1)

for i in range(1, N+1):
    weight[i], value[i] = map(int, input().split())

DP = [[0] * (K + 1) for _ in range(N+1)]
for object in range(1, N+1):
    for limit in range(1, K+1):
        if weight[object] <= limit: # 지금 용량보다 이하라면
            # 물건을 안넣는 경우, 현재 물건의 무게만큼 빼고 넣은 것 중 큰 것
            DP[object][limit] = max(DP[object-1][limit], DP[object-1][limit-weight[object]] + value[object])
        
        else:
            # 넣지 못함
            DP[object][limit] = DP[object-1][limit]

print(DP[-1][-1])