import sys
sys.setrecursionlimit(1000000)

k = int(input())

hx, hy = map(int, input().split())

n = 2 ** k
hr, hc = n - hy, hx - 1
board = [[0] * n for _ in range(n)]
board[hr][hc] = -1


tile_num = 0

def find_tromino(r, c, size, hr, hc):
    global tile_num
    if size == 1:
        return
    tile_num += 1
    t = tile_num
    ns = size // 2 # 다음 단계 크기

    if hr < r + ns and hc < c + ns:
        find_tromino(r, c, ns, hr, hc)
    else:
        board[r + ns - 1][c + ns - 1] = t
        find_tromino(r, c, ns, r + ns - 1, c + ns - 1)

    if hr < r + ns and hc >= c + ns:
            find_tromino(r, c + ns, ns, hr, hc)
    else:
        board[r + ns - 1][c + ns] = t
        find_tromino(r, c + ns, ns, r + ns - 1, c + ns)
        
    if hr >= r + ns and hc < c + ns:
        find_tromino(r + ns, c, ns, hr, hc)
    else:
        board[r + ns][c + ns - 1] = t
        find_tromino(r + ns, c, ns, r + ns, c + ns - 1)
        
    if hr >= r + ns and hc >= c + ns:
        find_tromino(r + ns, c + ns, ns, hr, hc)
    else:
        board[r + ns][c + ns] = t
        find_tromino(r + ns, c + ns, ns, r + ns, c + ns)

find_tromino(0, 0, n, hr, hc)
for row in board:
        print(*(row))