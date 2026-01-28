N = int(input())
arr = list(map(int, input().split()))

stack = []
result = [-1] * (N)
for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = arr[i]

    stack.append(i)

print(*result)