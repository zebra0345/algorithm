from collections import deque

N, P, K = map(int, input().split())

node = [[] for _ in range(N+1)]
max_cost = 0

for _ in range(P):
    a, b ,c = map(int, input().split())
    node[a].append((b, c))
    node[b].append((a, c))
    max_cost = max(max_cost, c)

def bfs(max_cost):
    q = deque()
    visited = [1000000] * (N+1)

    visited[1] = 0
    q.append(1)

    while q:
        current = q.popleft()
        for next, cost in node[current]:
            next_k = visited[current] + (cost > max_cost)
            if next_k <= K and next_k < visited[next]:
                visited[next] = next_k
                q.append(next)
    
    return visited[N] <= K

left, right = 0, max_cost
answer = -1

while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)