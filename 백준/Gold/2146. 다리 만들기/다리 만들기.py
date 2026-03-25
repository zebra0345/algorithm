N = int(input())
from collections import deque

board = [list(map(int, input().split())) for _ in range(N)]

land_cnt = 1
q = deque()
visited = [[False] * N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(start_y, start_x, land_cnt):
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True
    board[start_y][start_x] = land_cnt
    
    while q:
        y, x = q.popleft()
        
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    board[ny][nx] = land_cnt
                    q.append((ny, nx))
                    
land_num = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            check(i, j, land_num)
            land_num += 1
            

min_len = 99999999999

visited = [[False] * N for _ in range(N)]
def bridge_check(start_y, start_x, land_id):
    global min_len
    q = deque([(start_y, start_x, 0)])
    
    bfs_visited = [[False] * N for _ in range(N)]
    bfs_visited[start_y][start_x] = True
    
    while q:
        y, x, length = q.popleft()
        
        if length >= min_len:
            continue
            
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]  
            
            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] > 0 and board[ny][nx] != land_id:
                    min_len = min(min_len, length)
                    return
                    
                elif board[ny][nx] == 0 and not bfs_visited[ny][nx]:
                    bfs_visited[ny][nx] = True
                    q.append((ny, nx, length + 1))
                    
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            is_edge = False
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                    is_edge = True
                    break
            
            if is_edge:
                bridge_check(i, j, board[i][j])


print(min_len)