import sys
input = sys.stdin.readline
T = int(input())

out = []
for _ in range(T):

    line = input().strip()
    while line == "":
        line = input().strip()

    N, M = map(int, line.split())


    grape = [[] for _ in range(N)]
    rev_grape = [[] for _ in range(N)]
    
    edges = []

    for _ in range(M):
        a, b = map(int, input().split())
        grape[a].append(b)
        rev_grape[b].append(a)
        edges.append((a, b))

    visited = [False] * N
    order = []

    for start in range(N):
        if visited[start]:
            continue

        stack = [(start, 0)]
        visited[start] = True

        while stack:
            v, idx = stack[-1]

            if idx < len(grape[v]):
                nxt = grape[v][idx]
                stack[-1] = (v, idx+1)

                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            else:
                stack.pop()
                order.append(v)
    
    visited = [False] * N
    scc_id = [-1] * N
    scc_grape = []
    scc_cnt = 0

    for start in reversed(order):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        comp = []

        while stack:
            v = stack.pop()
            comp.append(v)
            scc_id[v] = scc_cnt

            for nxt in rev_grape[v]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
        
        scc_grape.append(comp)
        scc_cnt += 1
    
    indeg = [0] * scc_cnt
    seen = set()

    for a, b in edges:
        sa = scc_id[a]
        sb = scc_id[b]
        if sa != sb and (sa, sb) not in seen:
            seen.add((sa, sb))
            indeg[sb] += 1

    zero = [i for i in range(scc_cnt) if indeg[i] == 0]

    if len(zero) != 1:
        out.append("Confused")
    else:
        ans = scc_grape[zero[0]]
        ans.sort()
        for v in ans:
            out.append(str(v))

    out.append("")

print("\n".join(out))