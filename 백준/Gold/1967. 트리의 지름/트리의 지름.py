import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

# DFS 구현
def dfs(node, dist, visited):
    visited[node] = True
    far_node = node
    max_dist = dist

    for neighbor, weight in tree[node]:
        if not visited[neighbor]:
            next_node, next_dist = dfs(neighbor, dist + weight, visited)

            if next_dist > max_dist:
                max_dist = next_dist
                far_node = next_node
        
    return far_node, max_dist

# 1. 임의의 정점(1)에서 가장 먼 정점 A를 찾는다
visited = [False] * (n + 1)
a, _ = dfs(1, 0, visited)


# 2. 정점 A에서 가장 먼 정점 B까지 거리 = 지름
visited = [False] * (n + 1)
_, diameter = dfs(a, 0, visited)

print(diameter)