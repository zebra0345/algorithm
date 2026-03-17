import sys
sys.setrecursionlimit(100000)

V, E = map(int, input().split())

edge = []

for _ in range(E):
    a, b, w = map(int, input().split())
    
    edge.append((a, b, w))
    
edge.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[a] = b
        return True
    
    return False

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

cost = 0
for eg in edge:
    a, b, w = eg
    
    if union(a, b):
        cost += w
        
print(cost)