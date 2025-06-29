T = int(input())

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parents[root_y] = root_x
        size[root_x] += size[root_y]

    return size[root_x]

for _ in range(T):
    frends_input = int(input())
    parents = dict()
    size = dict()

    for _ in range(frends_input):
        a, b = input().split()
        for person in (a, b):
            if person not in parents:
                parents[person] = person
                size[person] = 1
        print(union(a, b))