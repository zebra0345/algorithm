N = int(input())

tree = [[] for _ in range(N+1)]
weight = [0] + list(map(int, input().split()))

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (N+1)
dp = [[0, 0, []] for _ in range(N+1)]

def dfs(cur):
    visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = weight[cur]

    for next in tree[cur]:
        if not visited[next]:
            dfs(next)
            # 1. 부분집합으로 설정안했으면
            dp[cur][0] += max(dp[next][0], dp[next][1])
            # 2. 설정안했으면
            dp[cur][1] += dp[next][0]

dfs(1)
result_node = []
trace_visted = [False] * (N+1)

def trace(cur, include):
    trace_visted[cur] = True
    if include:
        result_node.append(cur)
        for next_node in tree[cur]:
            if not trace_visted[next_node]:
                # 현재 포함했으니 다음은 무조건 x
                trace(next_node, False)
    else:
        for next_node in tree[cur]:
            if not trace_visted[next_node]:
                # 가중치 포함한게 크면
                if dp[next_node][1] > dp[next_node][0]:
                    trace(next_node, True)
                else:
                    trace(next_node, False)

if dp[1][1] > dp[1][0]:
    trace(1, True)
else:
    trace(1, False)

# 3. 출력
print(max(dp[1][0], dp[1][1])) # 최대 가중치 합
result_node.sort() # 오름차순 정렬
print(*result_node) # 노드 번호 출력