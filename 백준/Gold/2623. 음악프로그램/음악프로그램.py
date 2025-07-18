from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N+1)
grape = [[] for _ in range(N+1)]
for _ in range(M):
    pd_list = list(map(int, input().split()))
    k = pd_list[0]
    order = pd_list[1:]

    for i in range(k - 1):
        a = order[i]
        b = order[i + 1]
        grape[a].append(b)
        indegree[b] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)


result = []

while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in grape[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if len(result) == N:
    print(*result)
else:
    print(0)