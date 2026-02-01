N, L = map(int, input().split())
arr = list(map(int, input().split()))

from collections import deque

q = deque([])
for i in range(N):
    if q and q[0][0] <= i - L:
        q.popleft()
    
    while len(q) >= 1 and arr[i] < q[-1][1]:
        q.pop()
    
    q.append((i, arr[i]))
    print(q[0][1], end = " ")