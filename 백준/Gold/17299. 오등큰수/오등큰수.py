import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

check = Counter(arr)
result = [-1] * N
stack = []

for i in range(N):
    while stack and check[arr[stack[-1]]] < check[arr[i]]:
        idx = stack.pop()
        result[idx] = arr[i]

    stack.append(i)

print(*result)