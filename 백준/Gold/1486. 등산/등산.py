import heapq


def get_height(ch):
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a') + 26
    

N, M, T, D = map(int, input().split())
board = [input() for _ in range(N)]
height_map = [[get_height(ch) for ch in row] for row in board]

max_height = 0

def dist(start_y, start_x):
    dist_arr = [[float('inf')] * M for _ in range(N)]
    hq = [(0, start_y, start_x)]

    dist_arr[start_y][start_x] = 0

    while hq:
        cost, y, x = heapq.heappop(hq)

        if cost > dist_arr[y][x]:
            continue

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                diff = abs(height_map[ny][nx] - height_map[y][x])
                if diff <= T:
                    move_cost = 1 if height_map[ny][nx] <= height_map[y][x] else diff ** 2
                    total = cost + move_cost
                    if total < dist_arr[ny][nx]:
                        dist_arr[ny][nx] = total
                        heapq.heappush(hq, (total, ny, nx))
    
    return dist_arr

# 1 호텔에서 각 지점
to_here = dist(0, 0)

for i in range(N):
    for j in range(M):
        # 2 그 지점에서 호텔
        if to_here[i][j] != float('inf'):
            from_here = dist(i, j)
            if from_here[0][0] != float('inf') and to_here[i][j] + from_here[0][0] <= D:
                max_height = max(max_height, height_map[i][j])

print(max_height)