import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 쿼리 수
M = int(input().strip())
queries = [tuple(map(int, input().split())) for _ in range(M)]

import math
K = math.ceil(math.log2(N)) if N > 1 else 1

depth = [-1] * (N+1)
parent = [[0]*(N+1) for _ in range(K+1)] 

root = 1
depth[root] = 0
dq = deque([root])
while dq:
    u = dq.popleft()
    for v in adj[u]:
        if depth[v] == -1:
            depth[v] = depth[u] + 1
            parent[0][v] = u 
            dq.append(v)

for k in range(1, K+1):
    up = parent[k-1]
    cur = parent[k]
    for v in range(1, N+1):
        cur[v] = up[ up[v] ]

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    bit = 0
    while diff:
        if diff & 1:
            a = parent[bit][a]
        diff >>= 1
        bit += 1

    if a == b:
        return a

    for k in range(K, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

out = []
for a, b in queries:
    out.append(str(lca(a, b)))
print("\n".join(out))
