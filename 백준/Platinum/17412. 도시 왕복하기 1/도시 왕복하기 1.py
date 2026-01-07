import sys
from collections import deque

input = sys.stdin.readline

N, P = map(int, input().split())

g = [[] for _ in range(N+1)]

for _ in range(P):
    # 나중에 더 좋은 경로를 위해 도착점, 용량, 반대편 간선의 인덱스 저장
    a, b = map(int, input().split())
    g[a].append([b, 1, len(g[b])])
    g[b].append([a, 0, len(g[a]) - 1])


S, T = 1, 2
flow = 0

level = [-1] * (N+1)
ptr = [0] * (N+1)

while True:
    for i in range(1, N+1):
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
        break # 유량을 못보낼때

    for i in range(1, N+1):
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
                # 더 갈 곳이 없으면 백트래킹
                if not stack:
                    u = -1
                    break
                pu, pei = stack.pop()
                ptr[pu] += 1
                u = pu

        if u == -1:
            break  # 이 레벨 그래프에서 더 이상 경로 못 찾음

        # 찾은 경로(stack)에 유량 1 흘리기
        for pu, ei in stack:
            v, cap, rev = g[pu][ei]
            g[pu][ei][1] -= 1
            g[v][rev][1] += 1

        flow += 1

print(flow)
