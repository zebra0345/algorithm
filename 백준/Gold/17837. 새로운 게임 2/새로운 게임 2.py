import sys

N, K = map(int, input().split())

color = [list(map(int, input().split())) for _ in range(N)]

pieces = []
for _ in range(K):
    r, c, d = map(int, input().split())
    pieces.append([r - 1, c - 1, d])

board = [[[] for _ in range(N)] for _ in range(N)]
for i, (r, c, _) in enumerate(pieces):
    board[r][c].append(i)

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def reverse_dir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    return 3

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

turn = 0
ans = -1

while turn <= 1000:
    turn += 1
    for i in range(K):
        r, c, d = pieces[i]

        stack = board[r][c]
        idx = stack.index(i)
        moving = stack[idx:]       
        board[r][c] = stack[:idx] 

        nr, nc = r + dr[d], c + dc[d]

        if not in_range(nr, nc) or color[nr][nc] == 2:
            d = reverse_dir(d)
            pieces[i][2] = d
            nr, nc = r + dr[d], c + dc[d]
            if not in_range(nr, nc) or color[nr][nc] == 2:
                board[r][c].extend(moving)
                continue

        if color[nr][nc] == 1:
            moving.reverse()

        board[nr][nc].extend(moving)
        for pid in moving:
            pieces[pid][0] = nr
            pieces[pid][1] = nc

        if len(board[nr][nc]) >= 4:
            ans = turn
            print(ans)
            sys.exit(0)
            
    if turn == 1000:
        break

print(-1)
