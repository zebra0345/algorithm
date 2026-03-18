N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def bfs(start_y, start_x, island_id):
    q = deque([(start_y, start_x)])
    
    land[start_y][start_x] = island_id
    visited[start_y][start_x] = True
    
    while q:
        y, x = q.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = True
                    land[ny][nx] = island_id
                    q.append((ny, nx))

island_id = 1

for i in range(N):
    for j in range(M):
        if not visited[i][j] and land[i][j] == 1:
            bfs(i, j, island_id)
            island_id += 1
num_islands = island_id - 1
edge = set()

for i in range(N):
    for j in range(M):
        if land[i][j] > 0:
            current_id = land[i][j]
            
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                dist = 0
                while 0 <= ny < N and 0 <= nx < M:
                    if land[ny][nx] == current_id:
                        break
                    
                    elif land[ny][nx] == 0:
                        dist+=1
                        ny += dy[d]
                        nx += dx[d]
                    
                    else:
                        target = land[ny][nx]
                        if dist >= 2:
                            edge.add((dist, current_id, target))
                        break

edge = list(edge)
edge.sort()

parent =[i for i in range(num_islands+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[a] = b
        
total_cost = 0
total_bridge = 0

for dist, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        total_cost += dist
        total_bridge += 1

if total_bridge == num_islands - 1:
    print(total_cost)

else:
    print(-1)