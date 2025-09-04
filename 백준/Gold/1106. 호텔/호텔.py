# 도시, 도시별로 홍보하는 비용, 몇명이 들어나냐
# 근데 그 정보에 곱셈해서 고객을 추가로 도입가능하다.

# 호텔의 고객을 적어도 C 명 늘이기, 도시의 갯수 N
C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10000000000
MAX_PERSON = 100
LIMIT = C + MAX_PERSON

dp = [INF] * (LIMIT + 1)
dp[0] = 0

for cost, people in cities:
    for x in range(people, LIMIT+1):
        if dp[x - people] + cost < dp[x]:
            dp[x] = dp[x-people] + cost

print(min(dp[C:]))