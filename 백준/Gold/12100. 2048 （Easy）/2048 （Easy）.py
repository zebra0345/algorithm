import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

N = int(input().strip())
board0 = [list(map(int, input().split())) for _ in range(N)]

def merge_line(line):
    nonzero = [x for x in line if x != 0]
    merged = []
    i = 0
    while i < len(nonzero):
        if i + 1 < len(nonzero) and nonzero[i] == nonzero[i + 1]:
            merged.append(nonzero[i] * 2)
            i += 2
        else:
            merged.append(nonzero[i])
            i += 1
    merged += [0] * (N - len(merged))
    return merged

def move(board, dir_idx):
    new = [row[:] for row in board]

    if dir_idx == 0:  # LEFT
        for r in range(N):
            new[r] = merge_line(new[r])

    elif dir_idx == 1:  # RIGHT
        for r in range(N):
            rev = list(reversed(new[r]))
            rev = merge_line(rev)
            new[r] = list(reversed(rev))

    elif dir_idx == 2:  # UP
        for c in range(N):
            col = [new[r][c] for r in range(N)]
            col = merge_line(col)
            for r in range(N):
                new[r][c] = col[r]

    else:  # DOWN
        for c in range(N):
            col = [new[r][c] for r in range(N)][::-1]
            col = merge_line(col)
            col = col[::-1]
            for r in range(N):
                new[r][c] = col[r]

    return new

def max_tile(board):
    return max(max(row) for row in board)

answer = 0

def dfs(board, depth):
    global answer
    if depth == 5:
        answer = max(answer, max_tile(board))
        return

    moved = False
    for d in range(4):
        nxt = move(board, d)
        if nxt != board:
            moved = True
            dfs(nxt, depth + 1)

    # 더 이상 어떤 방향으로도 변화가 없으면(예: N=1, 꽉 막힌 상태)
    if not moved:
        answer = max(answer, max_tile(board))

dfs(board0, 0)
print(answer)
