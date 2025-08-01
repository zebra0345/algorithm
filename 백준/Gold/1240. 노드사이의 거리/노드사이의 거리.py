def dfs(current, target, cost, visited):
    if current == target:
        return cost

    visited[current] = True

    for next_node, weight in arr[current]:
        if not visited[next_node]:
            result = dfs(next_node, target, cost + weight, visited)
            if result is not None:
                return result


N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a, b, w = map(int, input().split())
    arr[a].append((b, w))
    arr[b].append((a, w))

for _ in range(M):
    start, end = map(int, input().split())
    visited = [False] * (N + 1)
    print(dfs(start, end, 0, visited))

