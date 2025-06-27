n, m = map(int, input().split())

parents = [i for i in range(n+1)]
rank = [1] * (n+1)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(x, y):
    root_a = find(x)
    root_b = find(y)

    if root_a == root_b:
        return
    
    if rank[root_a] < rank[root_b]:
        parents[root_a] = root_b
    
    else:
        parents[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
            
for i in range(m):
    order, a, b = map(int, input().split())
    if order == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")