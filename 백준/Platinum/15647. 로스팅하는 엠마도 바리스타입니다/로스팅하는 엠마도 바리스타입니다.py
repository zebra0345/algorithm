import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

sub = [0] * (N+1)
dist = [0] * (N+1)

def dfs1(x, parent, depth):
    sub[x] = 1
    dist[1] += depth

    for nx, w in tree[x]:
        if nx == parent:
            continue

        dfs1(nx, x, depth+w)
        sub[x] += sub[nx]

def dfs2(x, parent):
    for nx, w in tree[x]:
        if nx == parent:
            continue
        dist[nx] = dist[x] + (N - sub[nx]) * w - sub[nx] * w
        dfs2(nx, x)

dfs1(1, 0, 0)
dfs2(1, 0)

for i in range(1, N+1):
    print(dist[i])