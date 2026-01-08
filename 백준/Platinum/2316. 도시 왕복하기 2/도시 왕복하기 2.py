import sys
from collections import deque

input = sys.stdin.readline
N, P = map(int, input().split())

INF = 10**9
V = 2 * N # 정점 분할 노드 수 2N

g = [[] for _ in range(V+1)]

for v in range(1, N+1):
    cap = INF if v == 1 or v == 2 else 1
    vin = v
    # 1. 왜 v+N이지?
    vout = v+N
    g[vin].append([vout, cap, len(g[vout])])
    g[vout].append([vin, 0, len(g[vin])-1])

for _ in range(P):
    a, b = map(int, input().split())

    a_out = a + N
    b_out = b + N
    a_in = a
    b_in = b

    # aout -> bin
    g[a_out].append([b_in, INF, len(g[b_in])])
    g[b_in].append([a_out, 0, len(g[a_out])-1])

    # bout -> ain
    g[b_out].append([a_in, INF, len(g[a_in])])
    g[a_in].append([b_out, 0, len(g[b_out])-1])

S = 1+N
T = 2
flow = 0

level = [-1] * (V+1)
ptr = [0] * (V+1)

while True:
    for i in range(1, V+1):
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

    for i in range(1, V+1):
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
            break  # 이 레벨 그래프에서 더 이상 경로 없음

        # 찾은 경로로 유량 1 흘리기
        for pu, ei in stack:
            v, cap, rev = g[pu][ei]
            g[pu][ei][1] -= 1
            g[v][rev][1] += 1

        flow += 1

print(flow)