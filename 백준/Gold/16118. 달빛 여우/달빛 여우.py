import heapq

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split())
    arr[a].append((b, d))
    arr[b].append((a, d))

INF = 1000000000000
def fox(start):
    q = []
    fox_arr = [1000000000000] * (N+1)
    fox_arr[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        cost, now = heapq.heappop(q)

        if cost > fox_arr[now]:
            continue

        for next, w in arr[now]:
            if fox_arr[next] > cost + w:
                fox_arr[next] = cost + w
                heapq.heappush(q, (cost + w, next))
    
    return fox_arr

def wolf(start):
    q = []
    wolf_arr = [[INF, INF] for _ in range(N+1)]
    wolf_arr[start][0] = 0
    heapq.heappush(q, (0, start, 0))

    while q:
        cost, now, mode = heapq.heappop(q)

        if cost > wolf_arr[now][mode]:
            continue

        for next, w in arr[now]:
            next_mode = 1 - mode

            if mode == 0:
                next_cost = cost + w / 2
            else:
                next_cost = cost + w * 2
            
            if wolf_arr[next][next_mode] > next_cost:
                wolf_arr[next][next_mode] = next_cost
                heapq.heappush(q, (next_cost, next, next_mode))

    return wolf_arr

fox_arr = fox(1)
wolf_arr = wolf(1)

ans = 0
for i in range(1, N+1):
    fox_time = fox_arr[i]
    wolf_time = min(wolf_arr[i])


    if fox_time < wolf_time:
        ans += 1

print(ans)
