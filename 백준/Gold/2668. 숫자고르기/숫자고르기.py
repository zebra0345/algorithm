N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

visited = [False] * (N+1)
finished = [False] * (N+1)

result = []

def dfs(start, current):
    visited[current] = True
    next_node = arr[current]

    if not visited[next_node]:
        dfs(start, next_node)
    elif not finished[next_node]:
        temp = next_node
        result.append(temp)
        while temp != current:
            temp = arr[temp]
            result.append(temp)

    finished[current] = True


for i in range(1, N+1):
    if not visited[i]:
        dfs(i, i)

result.sort()

print(len(result))
for num in result:
    print(num)