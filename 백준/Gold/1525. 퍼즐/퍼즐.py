start = ""

for _ in range(3):
    row = input().split()
    start += "".join(row)

target = "123456780"

adj = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7],
    }

from collections import deque

q = deque([start])
visited = {start:0}
answer = 0
while q:
    cur = q.popleft()

    if cur == target:
        print(visited[cur])
        answer = 1
    zero = cur.index("0")    

    for nxt in adj[zero]:
        lst = list(cur)
        lst[zero], lst[nxt] = lst[nxt], lst[zero]
        new_state = "".join(lst)

        if new_state not in visited:
            visited[new_state] = visited[cur] + 1
            q.append(new_state)

if answer == 0:
    print(-1)