import sys
input = sys.stdin.readline

def update(tree, n, idx, val=1):
    i = idx + n
    tree[i] += val
    i //= 2
    while i:
        tree[i] = tree[i*2] + tree[i*2+1]
        i //= 2

def query(tree, n, l, r):
    l += n
    r += n
    s = 0
    while l < r:
        if l & 1:
            s += tree[l]
            l += 1
        if r & 1:
            r -= 1
            s += tree[r]
        l //= 2
        r //= 2
    return s


N = int(input().strip())
A = list(map(int, input().split()))

# 좌표 압축
uniq = sorted(set(A))
M = len(uniq)
rank = {v:i for i, v in enumerate(uniq)}  # 0..M-1

n = 1
while n < M:
    n <<= 1
tree = [0] * (2 * n)

ans = 0
for x in A:
    r = rank[x]  
    ans += query(tree, n, r + 1, M)
    update(tree, n, r, 1)

print(ans)


