case_no = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    
    visited = [False] * (n+1)

    def dfs(u, parent, cyc):
        visited[u] = True

        for v in tree[u]:
            if v == parent:
                continue
            if not visited[v]:
                dfs(v, u, cyc)
            else:
                cyc[0] = True
    
    trees = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            cyc = [False]
            dfs(i, 0, cyc)
            if not cyc[0]:
                trees += 1
    
    if trees == 0:
        print(f"Case {case_no}: No trees.")
    elif trees == 1:
        print(f"Case {case_no}: There is one tree.")
    else:
        print(f"Case {case_no}: A forest of {trees} trees.")
    case_no += 1