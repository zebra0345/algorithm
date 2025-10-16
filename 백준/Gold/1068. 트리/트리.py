N = int(input())
tree_list = list(map(int, input().split()))
target = int(input())

tree = [[] for _ in range(N)]
root = -1
for i in range(N):
    p = tree_list[i]
    if p == -1:
        root = i
    else:
        tree[p].append(i)

if target == root:
    print(0)
    exit()

parent = tree_list[target]
if parent != -1:
    tree[parent] = [c for c in tree[parent] if c != target]


def dfs(depth):
    if not tree[depth]:
        return 1
    cnt = 0
    for v in tree[depth]:
        cnt += dfs(v)
    
    return cnt

print(dfs(root))