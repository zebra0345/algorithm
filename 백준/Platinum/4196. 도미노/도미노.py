T = int(input())
out = []
for _ in range(T):
    N, M = map(int, input().split())



    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]
    edges = []


    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        rev_graph[b].append(a)
        edges.append((a, b))
    visited = [False] * (N+1)
    order = []

    for start in range(1, N+1):
        if visited[start]:
            continue

        visited[start] = True
        stack = [(start, 0)]

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
    scc_cnt = 0
    scc_id = [-1] * (N+1)

    for start in reversed(order):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True

        comp = []

        while stack:
            v = stack.pop()
            scc_id[v] = scc_cnt

            comp.append(v)
            for nxt in rev_graph[v]:
                if not visited[nxt]:
                    stack.append(nxt)
                    visited[nxt] = True

        scc_cnt += 1

    indeg = [0] * scc_cnt
    seen = set()

    for a, b in edges:
        sa = scc_id[a]
        sb = scc_id[b]
        if sa != sb:
            key = (sa, sb)
            if key not in seen:
                seen.add(key)
                indeg[sb] += 1
    ans = 0
    for i in range(scc_cnt):
        if indeg[i] == 0:
            ans += 1
    
    out.append(str(ans))

print("\n".join(out))
