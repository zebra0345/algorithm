# y, x
N, M = map(int, input().split())


land = [list(map(int, input().split())) for _ in range(N)]

from collections import deque
from math import degrees

visited = [[0] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

def check(y, x, land_cnt):
    q.append((y, x))
    visited[y][x] = 1
    land[y][x] = land_cnt
    while q:
        y, x = q.popleft()
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and land[ny][nx] != 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
                land[ny][nx] = land_cnt

land_cnt = 1
for i in range(N):
    for j in range(M):
        if land[i][j] != 0 and visited[i][j] == 0:
            check(i, j, land_cnt)
            land_cnt += 1

land_cnt -= 1
edge = set()

for y in range(N):
    for x in range(M):
        if land[y][x] > 0:
            current_id = land[y][x]
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                cost = 0
                
                while 0 <= ny < N and 0 <= nx < M:
                    if current_id == land[ny][nx]:
                        break
                    
                    elif land[ny][nx] == 0:
                        ny += dy[d]
                        nx += dx[d]
                        cost += 1
                    else:
                        if cost >= 2:
                            target = land[ny][nx]
                            edge.add((cost, current_id, target))
                        break

edge = list(edge)
edge.sort()

parent = [i for i in range(land_cnt+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[a] = b
        return False
    
    return True

total_cost = 0
total_bridge = 0
for c, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        total_cost += c
        total_bridge += 1
        

if total_bridge == land_cnt - 1:
    print(total_cost)

else:
    print(-1)