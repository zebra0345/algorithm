import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1

    for child in adj[node]:
        if not visited[child]:
            dfs(child)
            # 내가 일반인이면 자식은 얼리어답터
            dp[node][0] += dp[child][1]
            # 내가 얼리어답터면 자식은 최소
            dp[node][1] += min(dp[child][0], dp[child][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))