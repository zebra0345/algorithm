import sys

N, M = map(int, input().split())
parent = list(range(N))
rank = [0] * N

constraints = [tuple(input().split()) for _ in range(M)]
constraints = [(int(k), op, int(l)) for k, op, l in constraints]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if rank[a] < rank[b]:
        a, b = b, a
    
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1

adj = [[] for _ in range(N)]
indegree = [0] * N
used = [False] * N

for k, op, l in constraints:
    if op == "=":
        union(k, l)

for k, op, l in constraints:
    rk, rl = find(k), find(l)
    used[rk] = used[rl] = True
    if op == ">":
        if rk == rl:
            print("inconsistent")
            sys.exit()
        adj[rk].append(rl)
        indegree[rl] += 1
from collections import deque

q = deque([i for i in range(N) if used[i] and indegree[i] == 0])


visited = 0
total = sum(used)

while q:
    cur = q.popleft()
    visited += 1
    for nxt in adj[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print("consistent" if visited == total else "inconsistent")