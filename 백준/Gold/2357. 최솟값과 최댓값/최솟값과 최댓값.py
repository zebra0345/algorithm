import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] * (N + 1)
for i in range(1, N+1):
    arr[i] = int(input())
INF = 10**18

mn = [INF] * (4 * N)
mx = [-INF] * (4 * N)


def build(node, l, r):
    if l == r:
        mn[node] = arr[l]
        mx[node] = arr[l]
        return

    mid = (l+r)//2
    build(node * 2, l, mid)
    build(node*2 +1, mid+1, r)
    mn[node] = min(mn[node * 2], mn[node*2+1])
    mx[node] = max(mx[node*2], mx[node*2+1])

def query(node, l, r, ql, qr):
    # 겹치지 않음
    if qr < l or r < ql:
        return INF, -INF
    
    if ql <= l and r <= qr:
        return mn[node], mx[node]

    mid = (l + r) // 2
    left_min, left_max = query(node * 2, l, mid, ql, qr)
    right_min, right_max = query(node*2+1, mid+1, r, ql, qr)
    return min(left_min, right_min), max(left_max, right_max)

build(1, 1, N)
out = []
for _ in range(M):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    lo, hi = query(1, 1, N, a, b)
    out.append(f"{lo} {hi}")

print("\n".join(out))