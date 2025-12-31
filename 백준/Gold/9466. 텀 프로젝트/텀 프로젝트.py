T = int(input())

out = []
for _ in range(T):
    n = int(input())
    # 학생들 리스트
    std_list = [0] + list(map(int, input().split()))

    # 그래프
    graph = [[] for _ in range(n+1)]

    # 역방향
    rev_graph = [[] for _ in range(n+1)]

    # 그래프설계
    for a in range(1, n+1):
        b = std_list[a]
        graph[a].append(b)
        rev_graph[b].append(a)

    # 방문했느지
    visited = [False] * (n+1)
    order = []

    # 시작
    for start in range(1, n+1):
        # 방문했으면 넘기고
        if visited[start]:
            continue
        
        # 처음정점
        stack = [(start, 0)]
        visited[start] = True

        while stack:
            # 꺼내서
            v, idx = stack[-1]
            # 그래프에 넣었을떄 길이보다 짧으면
            if idx < len(graph[v]):
                # 다음 정점 후보 리스트
                nxt = graph[v][idx]
                # idx+1 을 추가한다
                stack[-1] = (v, idx+1)

                # 현재정점 방문안했으면
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append((nxt, 0))
            
            # 가지고있는 리스트의 길이보다 길면
            else:
                stack.pop()
                order.append(v)
        
    visited = [False] * (n + 1)
    team_cnt = 0

    for start in reversed(order):
        if visited[start]:
            continue

        comp = []
        st = [start]
        visited[start] = True

        while st:
            v = st.pop()
            comp.append(v)
            for nxt in rev_graph[v]:
                if not visited[nxt]:
                    visited[nxt] = True
                    st.append(nxt)
        
        if len(comp) >= 2:
            team_cnt += len(comp)
        else:
            x = comp[0]
            if std_list[x] == x:
                team_cnt += 1
    
    out.append(str(n - team_cnt))

print("\n".join(out))