N = int(input())

W = [list(map(int, input().split())) for _ in range(N)]

INF = 1000000000
ALL = (1 << N) - 1

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(cur, visited):
    if visited == ALL:
        return W[cur][0] if W[cur][0] != 0 else INF

    if dp[cur][visited] != -1:
        return dp[cur][visited]
    
    res = INF
    row = W[cur]
    
    for nxt in range(N):
        if visited & (1 << nxt):
            continue
        
        if row[nxt] == 0:
            continue
        
        cost = row[nxt] + dfs(nxt, visited | (1 << nxt))
        if cost < res:
            res = cost
    
    dp[cur][visited] = res
    return res

print(dfs(0, 1))