import heapq

N, M = map(int, input().split())


arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
    arr[b].append((a, t))

INF = 1000000

def dist(start, block=None):
    dist_arr = [INF] * (N+1)
    prev = [-1] * (N+1)

    dist_arr[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)
        if dist_arr[now] < cost:
            continue

        for next, w in arr[now]:
            if block == (now, next) or block == (next, now):
                continue

            if dist_arr[next] > dist_arr[now] + w:
                dist_arr[next] = dist_arr[now] + w
                prev[next] = now
                heapq.heappush(heap, (dist_arr[next], next))

    return dist_arr, prev

dist_arr_origin, prev = dist(1)

if dist_arr_origin[N] == INF:
    print(-1)
    exit()


path = []
current = N

while prev[current] != -1:
    path.append((current, prev[current]))
    current = prev[current]
    
max_d = 0

for u, v in path:
    dist_arr, _ = dist(1, block=(u, v))
    if dist_arr[N] == INF:
        print(-1)
        exit()
    
    max_d = max(max_d, dist_arr[N])

print(max_d - dist_arr_origin[N])
