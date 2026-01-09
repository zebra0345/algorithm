import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())

INF = 10**9

S = 0 # 시작점
B = 1 # 보조 노드
T = N+M+2 # 도착점
V = T # 전체 노드 개수의 마지막 번호

g = [[] for _ in range(V+1)]

for i in range(1, N+1):
    emp = 1 + i
    # 직원에게 기본적으로 일을 1개
    g[S].append([emp, 1, len(g[emp])])
    g[emp].append([S, 0, len(g[S])-1])

g[S].append([B, K, len(g[B])])
g[B].append([S, 0, len(g[S])-1])

for i in range(1, N+1):
    emp = i+1
    g[B].append([emp, K, len(g[emp])])
    g[emp].append([B, 0, len(g[B])-1])

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    emp = i+1
    for j in arr[1:1+cnt]:
        job = (N+1) + j
        g[emp].append([job, 1, len(g[job])])
        g[job].append([emp, 0, len(g[emp])-1])

for j in range(1, M+1):
    job = (N+1)+j
    g[job].append([T, 1, len(g[T])])
    g[T].append([job, 0, len(g[job])-1])

level = [-1] * (V+1)
ptr = [0] * (V+1)
flow = 0

while True:
    for i in range(V+1):
        level[i] = -1
    
    q = deque([S])
    level[S] = 0

    while q:
        u = q.popleft()
        for v, cap, rev in g[u]:
            if cap > 0 and level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)
    
    if level[T] == -1:
        break

    for i in range(V+1):
        ptr[i] = 0
    
    while True:
        u = S
        stack = []

        while u != T:
            found = False
            while ptr[u] < len(g[u]):
                ei = ptr[u]
                v, cap, rev = g[u][ei]

                if cap > 0 and level[v] == level[u] + 1:
                    stack.append((u, ei))
                    u = v
                    found = True
                    break
                ptr[u] += 1
            
            if not found:
                if not stack:
                    u = -1
                    break

                pu, pei = stack.pop()
                ptr[pu] += 1
                u = pu
        
        if u == -1:
            break

        for pu, ei in stack:
            v, cap, rev = g[pu][ei]
            g[pu][ei][1] -= 1
            g[v][rev][1] += 1
            
        flow += 1

print(flow)