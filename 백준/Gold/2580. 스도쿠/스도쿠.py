N = 9

board = [list(map(int, input().split())) for _ in range(N)]
blank = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            blank.append((i, j))

def row(a, n):
    for i in range(N):
        if n == board[a][i]:
            return False
    return True

def column(a, n):
    for i in range(N):
        if n == board[i][a]:
            return False
    
    return True

def square(y, x, n):
    for i in range(3):
        for j in range(3):
            if n == board[y//3 * 3 + i][x//3 * 3 + j]:
                return False
    return True

def find(n):
    if n == len(blank):
        for i in board: # 출력 후
            print(*i) 
        exit()
    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            board[y][x] = i
            find(n+1)
            board[y][x] = 0

find(0)