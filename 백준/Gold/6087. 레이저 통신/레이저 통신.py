from collections import deque

W, H = map(int, input().split())

board = [input() for _ in range(H)]

c_pos = []
for y in range(H):
    for x in range(W):
        if board[y][x] == "C":
            c_pos.append((y, x))

start = c_pos[0]
end = c_pos[1]

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[[10000000] * 4 for _ in range(W)] for _ in range(H)]

q = deque()

for d in range(len(dy)):
    ny = start[0] + dy[d]
    nx = start[1] + dx[d]

    if 0 <= ny < H and 0 <= nx < W and board[ny][nx] != '*':
        visited[ny][nx][d] = 0
        q.append((ny, nx, d, 0))
    
def bfs():
    while q:
        y, x, d, mirror = q.popleft()

        if (y, x) == end:
            return mirror
        

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] != '*':
                next_mirror = mirror + (0 if d == i else 1)

                if visited[ny][nx][i] > next_mirror:
                    visited[ny][nx][i] = next_mirror
                    if d == i:
                        q.appendleft((ny, nx, i, next_mirror))
                    else:
                        q.append((ny, nx, i, next_mirror))

print(bfs())