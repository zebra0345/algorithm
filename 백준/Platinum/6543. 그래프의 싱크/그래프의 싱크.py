import sys
input = sys.stdin.readline

out = []
while True:
    line = input().split()
    while not line:
        line = input().split()
    
    N = int(line[0])
    if N == 0:
        break
    M = int(line[1])

    grape = [[] for _ in range(N+1)]
    rev_grape = [[] for _ in range(N+1)]

    edges = []

    arr = list(map(int, input().split()))

    for i in range(0, len(arr), 2):
        a = arr[i]
        b = arr[i+1]
        grape[a].append(b)
        rev_grape[b].append(a)
        edges.append((a, b))
    
    visited = [False] * (N + 1)
    order = []

    for start in range(1, N+1):
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
    
    visited = [False] * (N+1)
    # 몇번 그래프에 속하는지
    scc_id = [-1] * (N+1)
    scc_groups = []
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
        
        scc_groups.append(comp)
        scc_cnt += 1
    outdeg = [0] * scc_cnt
    seen = set()

    for a, b in edges:
        sa = scc_id[a]
        sb = scc_id[b]

        if sa != sb and (sa, sb) not in seen:
            seen.add((sa, sb))
            outdeg[sa] += 1

    result = []
    for sid in range(scc_cnt):
        if outdeg[sid] == 0:
            result.extend(scc_groups[sid])
    
    result.sort()
    out.append(" ".join(map(str, result)))

sys.stdout.write("\n".join(out))
