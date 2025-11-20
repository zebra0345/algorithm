N, K = map(int, input().split())

import heapq
jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

max_heap = []
j = 0 
answer = 0

for bag in bags:
    while j < N and jewels[j][0] <= bag:
        # max heap
        heapq.heappush(max_heap, -jewels[j][1])
        j += 1
    
    if max_heap:
        answer += -heapq.heappop(max_heap)

print(answer)
