T = int(input())

for _ in range(T):
    n = int(input())
    parent = [0] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    
    u, v = map(int, input().split())

    visited = set()
    cur = u
    while cur != 0:
        visited.add(cur)
        cur = parent[cur]
    
    cur = v
    while cur not in visited:
        cur = parent[cur]
    
    print(cur)