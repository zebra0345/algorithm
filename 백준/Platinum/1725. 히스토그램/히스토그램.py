# 풀이
# 현재 높이 h[i]를 보며 스택 top 높이보다 크거나 같으면 그냥 push하기
# 높이 h[i] 가 작아지면 pop하면서 넓이 계산

import sys

input = sys.stdin.readline
N = int(input())

h = [0] * (N+1)
for i in range(N):
    h[i] = int(input())

stack = []
ans = 0


for i in range(N+1):
    while stack and h[stack[-1]] > h[i]:
        mid = stack.pop()
        height = h[mid]

        left = stack[-1] + 1 if stack else 0
        width = i - left

        area = height * width
        if area > ans:
            ans = area
    
    stack.append(i)

print(ans)