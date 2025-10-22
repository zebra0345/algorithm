import sys
sys.setrecursionlimit(1_000_000)


N = int(input())

sheep = [0] * (N + 1)
wolf  = [0] * (N + 1)
children = [[] for _ in range(N + 1)]

for i in range(2, N+1):
    sw_type, cnt, land_num = input().split()
    cnt = int(cnt)
    land_num = int(land_num)
    if sw_type == "W":
        wolf[i] = cnt
    elif sw_type == "S":
        sheep[i] = cnt
    children[land_num].append(i)

def dfs(u):
    total = 0
    for v in children[u]:
        total += dfs(v)
    
    if sheep[u]:
        total += sheep[u]
    
    elif wolf[u]:
        total -= wolf[u]
        if total < 0:
            total = 0
    return total

print(dfs(1))