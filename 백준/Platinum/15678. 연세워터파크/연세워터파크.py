from collections import deque

N, D = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
ans = -100000000
dp = [0] * N
for i in range(N):
    while q and q[0] < i-D:
        q.popleft()
    
    best = dp[q[0]] if q else 0
    dp[i] = arr[i] + max(best, 0)
    if dp[i] > ans:
        ans = dp[i]

    while q and dp[q[-1]] <= dp[i]:
        q.pop()

    if dp[i] > 0:
        q.append(i)
        
print(ans)