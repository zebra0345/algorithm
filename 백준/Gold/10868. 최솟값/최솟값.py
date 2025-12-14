import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * (N+1)

for i in range(1, N+1):
    arr[i] = int(input())

INF = 10**18
mn = [INF] * (4*N)

def build(node, l, r):
    if l == r:
        mn[node] = arr[l]
        return
    
    mid = (l+r) // 2
    build(node*2, l, mid)
    build(node*2+1, mid+1, r)
    mn[node] = min(mn[node*2], mn[node*2+1])


def query(node, l, r, ql, qr):
    if qr < l or r < ql:
        return INF
    
    if ql <= l and r <= qr:
        return mn[node]
    
    mid = (l + r) // 2
    left_min = query(node * 2, l, mid, ql, qr)
    right_min = query(node * 2 + 1, mid+1, r, ql, qr)
    return min(left_min, right_min)

build(1, 1, N)
out = []

for _ in range(M):
    l, r = map(int, input().split())
    if l > r:
        l, r = r, l
    min_num = query(1, 1, N, l, r)
    out.append(f"{min_num}")

print("\n".join(out))