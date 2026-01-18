import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

popul = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(cur):
    visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = popul[cur]

    for next in adj[cur]:
        if not visited[next]:
            dfs(next)
            # 내가 우수 마을이 아닌경우 -> 자식은 우수마을 or 아니여도 됨
            dp[cur][0] += max(dp[next][0], dp[next][1])
            dp[cur][1] += dp[next][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))