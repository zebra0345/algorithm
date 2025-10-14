# 임의의 정점 A 정함 -> B라는 정점에서 가장 먼 정점의 길이가 지름
from collections import deque

V = int(input())

if V == 1:
    print(0)
    exit()
    
tree = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, input().split()))
    v = data[0]
    start = 1

    while start < len(data) and data[start] != -1:
        node1, w = data[start], data[start+1]
        tree[v].append((node1, w))
        tree[node1].append((v, w))
        start += 2
    
    tmp_node = 1

def bfs(start, adj, n):
    dist = [-1] * (n+1)
    dist[start] = 0
    dq = deque([start])

    while dq:
        v = dq.popleft()
        for nv, w in tree[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + w
                dq.append(nv)
    
    far_node = 1
    for i in range(2, n+1):
        if dist[i] > dist[far_node]:
            far_node = i
    
    return far_node, dist[far_node]

# 1번노드 비었니?
while tmp_node <= V and not tree[tmp_node]:
    tmp_node += 1

if tmp_node > V:
    print(0)
    exit()

x, _ = bfs(tmp_node, tree, V)
_, d = bfs(x, tree, V)

print(d)