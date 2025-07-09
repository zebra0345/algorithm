from collections import deque

N, M = map(int, input().split())

information = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    information[a].append((b, c))
    information[b].append((a, c))

factory1, factory2 = map(int, input().split())

def can_carry(weight):
    visited = [False] * (N+1)
    q = deque([factory1])

    visited[factory1] = True

    while q:
        node = q.popleft()

        if node == factory2:
            return True
        
        for n, w in information[node]:
            if not visited[n] and w >= weight:
                visited[n] = True
                q.append(n)
    
    return False

low, high = 0, 100000000000000000000
ans = 0

while low <= high:
    mid = (low + high) // 2

    if can_carry(mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)