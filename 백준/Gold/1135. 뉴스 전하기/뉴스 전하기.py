import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))

tree = [[] for _ in range(n)]
for child in range(1, n):
    tree[parent[child]].append(child)

def dfs(node):
    times = []
    for child in tree[node]:
        times.append(dfs(child))
    
    times.sort(reverse=True)

    max_time = 0
    for i, t in enumerate(times):
        max_time = max(max_time, t + i + 1)

    return max_time

print(dfs(0))