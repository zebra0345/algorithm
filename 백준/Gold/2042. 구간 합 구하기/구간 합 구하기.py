# 세그먼트 트리 : 리스트 같은걸 절반으로 나눠 계속
# 더 이상 나눌 수 없을 때 리프에 저장, 그 부모 노드는 리프의 합

import math
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline


N, M, K = map(int, input().split())
arr = [0] * (N+1)

for i in range(1, N+1):
    arr[i] = int(input())

tree = [0] * (4 * (N+1))


def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    left_sum = build(node * 2, start, mid)
    right_sum = build(node * 2 + 1, mid + 1, end)

    tree[node] = left_sum + right_sum

    return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    if start == end:
        return
    
    mid = (start + end) // 2

    update(node * 2, start, mid, idx, diff)
    update(node * 2 + 1, mid+1, end, idx, diff)

def query(node, start, end, left, right):
    # 구간 안겹침
    if right < start or end < left:
        return 0
    
    # 완전히 겹침
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + \
           query(node * 2 + 1, mid + 1, end, left, right)


build(1, 1, N)

out_lines = []

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = b
        new_val = c
        diff = new_val - arr[idx]
        arr[idx] = new_val
        update(1, 1, N, idx, diff)
    else:  # a == 2
            left, right = b, c
            if left > right:
                left, right = right, left
            res = query(1, 1, N, left, right)
            out_lines.append(str(res))

sys.stdout.write("\n".join(out_lines))