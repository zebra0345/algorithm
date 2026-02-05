N = int(input())

arr = [0] * (N)
result = [-1] * N
stack = []
ans = 0
for i in range(N):
    height = int(input())
    cnt = 1

    while stack and stack[-1][0] < height:
        ans += stack[-1][1]
        stack.pop()

    if not stack:
        stack.append((height, cnt))
        continue

    if stack[-1][0] == height:
        same_cnt = stack[-1][1]
        ans += same_cnt # 같은 키는 전부 보인다
        stack.pop()
        cnt = same_cnt + 1
        if stack:
            ans += 1
        stack.append((height, cnt))
    else:
        ans += 1
        stack.append((height, cnt))
print(ans)
