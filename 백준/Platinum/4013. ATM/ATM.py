import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]
money = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

for i in range(1, N+1):
    money[i] = int(input())

S, P = map(int, input().split())
is_rest = [False] * (N+1)
rest_nodes = []
while len(rest_nodes) < P:
    rest_nodes.extend(map(int, input().split()))

is_rest = [False] * (N + 1)
for x in rest_nodes[:P]:
    is_rest[x] = True

visited = [False] * (N+1)
order = []


for start in range(1, N+1):
    if visited[start]:
        continue

    stack = [(start, 0)]
    visited[start] = True

    while stack:
        v, idx = stack[-1]
        if idx < len(graph[v]):
            nxt = graph[v][idx]
            stack[-1] = (v, idx+1)
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, 0))
        else:
            stack.pop()
            order.append(v)

visited = [False] * (N+1)
scc_id = [-1] * (N+1)
scc_cnt = 0

# 돈, 레스토랑 포함여부
scc_money = []
scc_has_rest = []

for start in reversed(order):
    if visited[start]:
        continue

    stack = [start]
    visited[start] = True

    comp_sum = 0
    comp_has_rest = False

    while stack:
        v = stack.pop()
        scc_id[v] = scc_cnt

        comp_sum += money[v]
        if is_rest[v]:
            comp_has_rest = True
        for nxt in rev_graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
    
    scc_money.append(comp_sum)
    scc_has_rest.append(comp_has_rest)
    scc_cnt += 1

dag = [[] for _ in range(scc_cnt)]
indeg = [0] * scc_cnt
seen = set()

for v in range(1, N+1):
    sv = scc_id[v]
    for nxt in graph[v]:
        sn = scc_id[nxt]
        if sv != sn:
            key = (sv, sn)
            if key not in seen:
                seen.add(key)
                dag[sv].append(sn)
                indeg[sn] += 1

start_scc = scc_id[S]

dp = [-1] * scc_cnt
dp[start_scc] = scc_money[start_scc]

from collections import deque
q = deque()
for i in range(scc_cnt):
    if indeg[i] == 0:
        q.append(i)

topo = []

while q:
    x = q.popleft()
    topo.append(x)
    for y in dag[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)

for x in topo:
    if dp[x] == -1:
        continue
    base = dp[x]
    for y in dag[x]:
        cand = base + scc_money[y]
        if cand > dp[y]:
            dp[y] = cand

ans = 0
for c in range(scc_cnt):
    if scc_has_rest[c] and dp[c] > ans:
        ans = dp[c]

print(ans)