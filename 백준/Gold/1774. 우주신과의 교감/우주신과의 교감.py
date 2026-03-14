N, M = map(int, input().split())


coords = [tuple(map(int, input().split())) for _ in range(N)]
parent = list(range(N))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a
        return True
    return False



for _ in range(M):
    a, b = map(int, input().split())
    union(a-1, b-1)
    
edges = []
import math

for i in range(N):
    x1, y1 = coords[i]
    
    for j in range(i+1, N):
        x2, y2 = coords[j]
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
        edges.append((dist, i, j))
        
edges.sort()

answer = 0 

for dist, a, b in edges:

    if union(a, b):
        answer += dist



print(f"{answer:.2f}")