n = int(input())

a = list(map(int, input().split()))


left = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            left[i] = max(left[i], left[j] + 1)

right = [1] * n

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[j] < a[i]:
            right[i] = max(right[i], right[j] + 1)

ans = 0
for i in range(n):
    ans = max(ans, left[i] + right[i] - 1)

print(ans)