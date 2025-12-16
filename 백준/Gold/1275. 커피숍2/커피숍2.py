import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))

tree = [0] * (4 * N)


def build(node, l, r):
    if l == r:
        tree[node] = arr[l]
        return tree[node]
    
    mid = (l+r)//2
    left = build(node * 2, l, mid)
    right = build(node * 2 + 1, mid+1, r)

    tree[node] = left + right
    return tree[node]

def query(node, l, r, ql, qr):
    # 구간 안겹침
    if ql > r or qr < l:
        return 0
    
    # 완전히 겹침
    if ql <= l and r <= qr:
        return tree[node]
    
    mid = (l+r) // 2

    return query(node*2, l, mid, ql, qr) + query(node*2+1, mid+1, r , ql, qr)

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff

    if start == end:
        return
    mid = (start + end)//2

    update(node * 2, start, mid, idx, diff)
    update(node * 2 + 1, mid+1, end, idx, diff)

build(1, 1, N)

out = []
for _ in range(M):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x

    out.append(str(query(1, 1, N, x, y)))

    diff = b - arr[a]
    arr[a] = b
    update(1, 1, N, a, diff)

print("\n".join(out))