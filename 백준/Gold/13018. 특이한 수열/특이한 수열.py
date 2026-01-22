n, k = map(int, input().split())

if k == n:
    print("Impossible")
    exit()

ans = list(range(1, n+1))

res = list(range(1, n+1))
target = n-k
milled = res[1:target] + [res[0]]
ans = milled + res[target:]
    
print(*(ans))