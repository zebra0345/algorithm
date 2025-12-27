import sys

input = sys.stdin.readline

def scc_sort_key(comp):
    return comp[0]


V, E = map(int, input().split())

# 원 그래프와 역방향 그래프
graph = [[] for _ in range(V + 1)]
rev_graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

# 1. 종료 순서 만들기
visited = [False] * (V+1)
ordered = [] # DFS 끝난 정점 저장(후위순회)

for start in range(1, V+1):
    if visited[start]:
        continue

    stack = [(start, 0)]
    visited[start] = True

    while stack:
        v, idx = stack[-1]

        # 아직 정점이 있는지
        if idx < len(graph[v]):
            nxt = graph[v][idx]

            # 다음번엔 idx+1 보도록 업데이트
            stack[-1] = (v, idx+1)

            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, 0))
        
        else:
            stack.pop()
            ordered.append(v)

visited = [False] * (V + 1)
scc_list = []


for start in reversed(ordered):
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

    
    comp.sort()
    scc_list.append(comp)

scc_list.sort(key=scc_sort_key)
out_lines = []
out_lines.append(str(len(scc_list)))
for comp in scc_list:
    out_lines.append(" ".join(map(str, comp)) + " -1")

print("\n".join(out_lines))
