N = int(input())

left_child = [-1] * (N+1)
right_child = [-1] * (N+1)
has_parent = [False] * (N+1)

for _ in range(N):
    node, left, right = map(int, input().split())
    left_child[node] = left
    right_child[node] = right

    if left != -1:
        has_parent[left] = True
    if right != -1:
        has_parent[right] = True

root = None

for i in range(1, N+1):
    if not has_parent[i]:
        root = i
        break

x = 0
min_x = dict()
max_x = dict()

def inorder(node, depth):
    global x

    # 더이상 없으면
    if node == -1:
        return
    
    # 왼쪽부터
    inorder(left_child[node], depth+1)

    x += 1
    if depth not in min_x:
        min_x[depth] = x

    max_x[depth] = x

    inorder(right_child[node], depth+1)

inorder(root, 1)

best_level = 1
best_width = 1
for lvl in min_x.keys():
    width = max_x[lvl] - min_x[lvl] + 1
    # 더 넓으면 교체, 같으면 레벨이 작은 쪽 유지
    if width > best_width or (width == best_width and lvl < best_level):
        best_width = width
        best_level = lvl

print(best_level, best_width)
