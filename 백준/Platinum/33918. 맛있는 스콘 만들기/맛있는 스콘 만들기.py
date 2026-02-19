# 스콘만들기
# 0시부터 N-1까지 N번 온도 조절
# 1 ~ M 까지 정수 온도로 조절
# 자유롭게 조절 가능하다
# 제약사항 : 0에서는 자유롭게 조절가능
# 시각 T에서의 최적의 온도를 b 시각 t에서 조절한 오븐의 온도를 k
# 라고한다면 시각 t+1 에서 스콘의 맛은 M - |b - k|
# 풀이 : b-k를 0에 가깝게해서 M을 극대화하면 M이 커짐

import sys
from collections import deque

INF = 10**18
input = sys.stdin.readline

N, M, C, D = map(int, input().split())
b = list(map(int, input().split()))

L = D // C  # 같은 나머지 그룹에서 한 번에 이동 가능한 '칸 수'

groups = []
for r in range(1, C + 1):
    if r > M:
        break
    groups.append(list(range(r, M + 1, C)))

dp_prev = [-INF] * (M + 1)
for temp in range(1, M + 1):
    dp_prev[temp] = M - abs(b[0] - temp)

if N == 1:
    print(max(dp_prev[1:]))
    sys.exit()

for t in range(1, N):
    bt = b[t]
    dp_cur = [-INF] * (M + 1)

    for temps in groups:
        K = len(temps)  

        prev = [dp_prev[temp] for temp in temps]

        dq = deque()

        def push(idx):
            while dq and prev[dq[-1]] <= prev[idx]:
                dq.pop()
            dq.append(idx)

        right0 = min(K - 1, L)
        for j in range(0, right0 + 1):
            push(j)

        for i in range(K):
            left = i - L  # 윈도우 왼쪽 경계

            while dq and dq[0] < left:
                dq.popleft()

            best_prev = prev[dq[0]] 

            temp = temps[i]
            gain = M - abs(bt - temp)  
            dp_cur[temp] = best_prev + gain

            new = i + L + 1
            if new < K:
                push(new)

    dp_prev = dp_cur

print(max(dp_prev[1:]))