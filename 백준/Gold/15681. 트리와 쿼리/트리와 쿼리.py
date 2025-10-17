import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline         

N, R, Q = map(int, input().split())

tree = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


# 부모 노드 저장(재방문x)
parent = [0] * (N+1)
sub_size = [0] * (N+1)

def dfs(u):
    sub_size[u] = 1
    for v in tree[u]:
        if v == parent[u]:
            continue
        parent[v] = u
        sub_size[u] += dfs(v)
    return sub_size[u]

parent[R] = -1
dfs(R)
result = []
for _ in range(Q):
    u = int(input())
    result.append(str(sub_size[u]))

print("\n".join(result))