import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())

MOD = 1_000_000_007

arr = [0] * (N+1)
for i in range(1, N+1):
    arr[i] = int(input())

tree = [1] * (4 * N)

def build(node, l, r):
    if l == r:
        tree[node] = arr[l] % MOD
        return tree[node]
    
    mid = (l+r) // 2
    left_sum = build(node*2, l, mid)
    right_sum = build(node*2+1, mid+1, r)

    tree[node] = (left_sum * right_sum) % MOD

    return tree[node]

def update(node, l, r, idx, val):
    if idx < l or r < idx:
        return tree[node]
    
    if l == r:
        tree[node] = val % MOD
        return tree[node]
    
    mid = (l+r) // 2
    left = update(node * 2, l, mid, idx, val)
    right = update(node * 2 + 1, mid+1, r, idx, val)

    tree[node] = (left * right) % MOD
    return tree[node]

def query(node, l, r, ql, qr):
    if qr < l or r < ql:
        return 1
    if ql <= l and r <= qr:
        return tree[node]
    
    mid = (l+r)//2
    left = query(node*2, l, mid, ql, qr)
    right = query(node*2+1, mid+1, r, ql, qr)
    return (left * right) % MOD

build(1, 1, N)
out = []
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
    else:
        out.append(str(query(1, 1, N, b, c)))

print("\n".join(out))