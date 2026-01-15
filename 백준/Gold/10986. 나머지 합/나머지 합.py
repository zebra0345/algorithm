import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = map(int, input().split())

cnt = [0] * M
cnt[0] = 1

s = 0
ans = 0

for x in arr:
    s = (s + x) % M
    ans += cnt[s]
    cnt[s] += 1

print(ans)