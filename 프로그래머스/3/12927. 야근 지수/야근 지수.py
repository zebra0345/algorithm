import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    max_heap = [-w for w in works]
    heapq.heapify(max_heap)
    
    for _ in range(n):
        max_work = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_work + 1)
        
    answer = sum(w ** 2 for w in max_heap)
    
    return answer