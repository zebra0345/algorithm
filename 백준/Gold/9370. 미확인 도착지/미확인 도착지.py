import heapq

T = int(input())


def dist(start, graph, n):
    dist_arr = [100000000] * (n+1)
    dist_arr[start] = 0

    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)
        # 이미 처리
        if dist_arr[now] < cost:
            continue
        for goal, weight in grape[now]:
            # 지금 저장한 거리보다 현재위치에서 가는 길 더한 값이 작으면
            if dist_arr[goal] > dist_arr[now] + weight:
                # 업데이트
                dist_arr[goal] = dist_arr[now] + weight
                # 거리와 노드 번호 저장
                heapq.heappush(heap, (dist_arr[goal], goal))
    
    return dist_arr

for t in range(T):
    # 3개의 정수 n, m, t
    n, m, t = map(int, input().split())

    # 목적지로부터 최단거리 경로값 >=< 반드시 지나야하는 경로값을 비교
    # 반드시 지나야 하는 경로를 거쳐서 목적지 간 값이 더 크다? 그러면 불가능

    # 출발지, 사이 교차로
    s, g, h = map(int, input().split())

    grape = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        grape[a].append((b, c))
        grape[b].append((a, c))

    dist_s = dist(s, grape, n)
    dist_g = dist(g, grape, n)
    dist_h = dist(h, grape, n)


    goals = [int(input()) for _ in range(t)]

    answer = []
    for goal in goals:
        path1 = dist_s[g] + dist_g[h] + dist_h[goal]
        path2 = dist_s[h] + dist_h[g] + dist_g[goal]

        short_w = dist_s[goal]

        if short_w == path1 or short_w == path2:
            answer.append(goal)
    
    answer.sort()
    print(*answer)